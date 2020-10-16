import numpy as np ## You may NOT modify this line, or your assignment may be graded as 0 point.
## Feel free to import other handy built-in modules here

## self-defined constants
err_threshpold = 1e-5

## Self-defined exceptions
## Please **DO NOT MODIFITY** the following exceptions!
class dtypeError(Exception):
	pass

class SizeUnmatchedError(Exception):
	pass
## Self-defined exceptions end here

## Definition for class KF
class KF:
    def predict(self, x_pre, P_pre, u_k, F, B, Q):

        if x_pre.dtype != 'float64' or P_pre.dtype != 'float64' or u_k.dtype != 'float64' or F.dtype != 'float64' or B.dtype != 'float64' or Q.dtype != 'float64':
            
            raise dtypeError
        
        n, m = x_pre.shape[0], u_k.shape[0]
        
        if x_pre.shape != (n, 1) or P_pre.shape != (n, n) or u_k.shape != (m, 1) or F.shape != (n, n) or B.shape != (n, m) or Q.shape != (n, n):

            raise SizeUnmatchedError

        x_now = F @ x_pre + B @ u_k

        P_now = F @ P_pre @ F.T + Q

        return x_now, P_now

    def update(self, x_pre, P_pre, z_k, H, R):

        if x_pre.dtype != 'float64' or P_pre.dtype != 'float64' or z_k.dtype != 'float64' or H.dtype != 'float64' or R.dtype != 'float64':
            
            raise dtypeError

        n, k = x_pre.shape[0], z_k.shape[0]

        if x_pre.shape != (n, 1) or P_pre.shape != (n, n) or z_k.shape != (k, 1) or H.shape != (k, n) or R.shape != (k, k):

            raise SizeUnmatchedError

        K = P_pre @ H.T @ np.linalg.inv(H @ P_pre @ H.T + R)

        x_hat = x_pre + K @ (z_k - H @ x_pre)

        P_hat = P_pre - K @ H @ P_pre

        return x_hat, P_hat


if __name__ == "__main__":
    x = [0,1,2]
    P = [[1,2,3],[4,5,6],[7,8,9]]
    x_np = np.array(x, dtype = np.float64).reshape(3, 1)
    P_np = np.array(P, dtype = np.float64)

    u = [0.1, 0.2, 0.3]
    u_np = np.array(u, dtype = np.float64).reshape(3, 1)

    F_np = np.eye(3, dtype = np.float64)
    B_np = np.diag((4,5,6))
    B_np = np.array(B_np, dtype = np.float64)
    Q_np = 0.02 * np.eye(3, dtype = np.float64)

    z_k = [1, 3, 4]
    z_k_np = np.array(z_k, dtype = np.float64).reshape(3, 1)
    H_np = 2 * np.eye(3, dtype = np.float64)
    R_np = 0.03 * np.eye(3, dtype = np.float64)

    ## KF implementation testing
    try:
        kf = KF()
        x_predicted, P_predicted = kf.predict(x_np, P_np, u_np, F_np, B_np, Q_np)
        x_updated, P_updated = kf.update(x_predicted, P_predicted, z_k_np, H_np, R_np)
    except:
        print('Implement Incorrect.')
        exit(0)

    x_predicted_ans = np.array([0.4, 2.0, 3.8], dtype = np.float64).reshape(3, 1)
    P_predicted_ans = np.array(
        [[1.02, 2., 3.],
        [4., 5.02, 6.],
        [7., 8., 9.02]], dtype = np.float64)
    x_updated_ans = np.array(
        [[0.53589339],
        [1.43716531],
        [2.02934631]], dtype = np.float64)
    P_updated_ans = np.array(
        [[0.00719595, 0.00069144, -0.00035852],
        [ 0.00068505, 0.00613639,  0.00067865],
        [-0.00037131, 0.00067225,  0.00717036]], dtype = np.float64)

    diff_1 = x_predicted - x_predicted_ans
    diff_2 = P_predicted - P_predicted_ans
    diff_3 = x_updated - x_updated_ans
    diff_4 = P_updated - P_updated_ans

    if (diff_1 < err_threshpold).all():
        print('x_predict correct.')
    else:
        print('x_predict wrong.')

    if (diff_2 < err_threshpold).all():
        print('P_predict correct.')
    else:
        print('P_predict wrong.')

    if (diff_3 < err_threshpold).all():
        print('x_updated correct.')
    else:
        print('x_updated wrong.')
    
    if (diff_4 < err_threshpold).all():
        print('P_updated correct.')
    else:
        print('P_updated wrong.')

    ## Test exception handling
    x2 = [0,1,2,4]
    x2_np = np.array(x2, dtype = np.float64).reshape(4, 1)

    try:
        x_predicted, P_predicted = kf.predict(x2_np, P_np, u_np, F_np, B_np, Q_np)
    except SizeUnmatchedError:
        print('Pass SizeUnmatchedError test')
    except:
        print('Fail SizeUnmatchedError test')
    else:
        print('Fail SizeUnmatchedError test')

    x_np_2 = np.array(x, dtype = np.float32).reshape(3, 1)
    try:
        x_predicted, P_predicted = kf.predict(x_np_2, P_np, u_np, F_np, B_np, Q_np)
    except dtypeError:
        print('Pass dtypeError test')
    except:
        print('Fail dtypeError test')
    else:
        print('Fail dtypeError test')