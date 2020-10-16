import pandas as pd
import numpy as np
from gazelib.utils import decode_base64_img
import copy





def mean_of_tgt_subject(df: pd.core.frame.DataFrame, subject_id: int) -> (float, float):

    return (df.groupby(['subject_id']).mean().loc[subject_id].yaw, df.groupby(['subject_id']).mean().loc[subject_id].pitch)


def count_tgt_subject(df: pd.core.frame.DataFrame, yaw_threshold: float) -> int:

    return len(df[df.yaw > yaw_threshold])


def get_min_val_of_tgt_col(df: pd.core.frame.DataFrame, col: str):
    
    return df[col].min()


def sort_ids_by_stdofcol(df: pd.core.frame.DataFrame, col: str) -> list:
    
    return list(df.groupby(['subject_id']).std().sort_values(by=[col]).index)


def compute_mean_eye(df: pd.core.frame.DataFrame) -> np.ndarray:

    return sum([decode_base64_img(i)/len(df) for i in df.image_base64]).astype('uint8')


def add_glasses_info(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    
    return pd.concat([copy.deepcopy(df), pd.DataFrame({'has_glasses' : [True if (i[1]['subject_id'] in [1, 4, 7, 9, 10]) else False for i in df.iterrows()]})], axis=1)


def KNN_idxs(train_X, val_x, k=1):

    return np.argsort(np.array([np.linalg.norm(val_x - train_X[i]) for i in range(len(train_X))]))[:k]


def oneNN(train_X, train_Y, val_x):
    
    return train_Y[KNN_idxs(train_X, val_x)][0]


def KNN(train_X, train_Y, val_x, k=1):

    return np.array((np.median([train_Y[i][0] for i in KNN_idxs(train_X, val_x, k)]), np.median([train_Y[i][1] for i in KNN_idxs(train_X, val_x, k)])))


def KNN_weighted(train_X, train_Y, val_x, k=1):
    
    return sum(map(lambda x: (1/np.linalg.norm(train_X[x] - val_x))*train_Y[x], KNN_idxs(train_X, val_x, k))) / sum(map(lambda x: 1 / np.linalg.norm(train_X[x] - val_x), KNN_idxs(train_X, val_x, k)))



def conv2d3x3(im: np.ndarray, kernel: np.ndarray):

    assert im.shape[0] >= 3
    assert im.shape[1] >= 3

    ret = np.zeros((im.shape[0] - 2, im.shape[1] - 2), dtype=np.float)

    for i in range(1, im.shape[0] - 1):
        for ii in range(1, im.shape[1] - 1):
            for j in range(3):
                for jj in range(3):
                    ret[i - 1][ii - 1] += kernel[j][jj]*im[i + j - 1][ii+jj-1]


    assert ret.shape[0] == im.shape[0] - 2
    assert ret.shape[1] == im.shape[1] - 2

    return ret

def conv2d3x3_same(im: np.ndarray, kernel: np.ndarray):

    assert im.shape[0] >= 1
    assert im.shape[1] >= 1

    ret = conv2d3x3(np.pad(im, 1, "reflect"), kernel)

    return ret


from gazelib.conv2d import gaussian_knl, sobel_hrztl, sobel_vtcl

def compute_grad(im: np.ndarray):

    im_blur = conv2d3x3_same(im, gaussian_knl)

    Gx, Gy = conv2d3x3_same(im_blur, sobel_hrztl), conv2d3x3_same(im_blur, sobel_vtcl)

    grad_dir = np.array([Gx, Gy])

    grad_mag = np.array([list(map(lambda x, y : np.linalg.norm(np.array([x, y])), Gx[i], Gy[i])) for i in range(im_blur.shape[0])])

    grad_dir_norm = grad_dir / (grad_mag + 1e-3)


    assert grad_dir_norm.shape == (2, im_blur.shape[0], im_blur.shape[1])
    assert grad_mag.shape == im_blur.shape

    return grad_dir_norm, grad_mag


def bilinear_HOG_nonvec(grad_dir, grad_mag, bin_num=12):

    ret_bin = np.zeros((bin_num,), dtype=np.float)
    bin_interval = np.pi * 2 / bin_num


    for i in range(grad_mag.shape[0]):
        for j in range(grad_mag.shape[1]):


            grad_dir_deg = np.arctan2(grad_dir[0, i, j], grad_dir[1, i, j]) + np.pi # -40

            grad_bin_idx_l = int((grad_dir_deg) // bin_interval) % bin_num # -60
            grad_bin_idx_r = int((grad_bin_idx_l + 1)) % bin_num # -30

            grad_bin_lcoeff = grad_dir_deg / bin_interval - grad_bin_idx_l # 1

            grad_bin_rcoeff = 1 - grad_bin_lcoeff # 2

            ret_bin[grad_bin_idx_l] += grad_bin_lcoeff * grad_mag[i, j]
            ret_bin[grad_bin_idx_r] += grad_bin_rcoeff * grad_mag[i, j]


    return ret_bin

    


def bilinear_HOG(grad_dir : np.ndarray, grad_mag : np.ndarray, bin_num=12):

    ret_bin = np.zeros((bin_num,), dtype=np.float)

    bin_interval = np.pi * 2 / bin_num

    grad_dir_deg = np.arctan2(grad_dir[0], grad_dir[1]) + np.pi

    grad_bin_idx_l = ((grad_dir_deg) // bin_interval).astype(np.int16) % bin_num

    grad_bin_idx_r = ((grad_bin_idx_l + 1)).astype(np.int16) % bin_num

    grad_bin_lcoeff = grad_dir_deg / bin_interval - grad_bin_idx_l

    grad_bin_rcoeff = 1 - grad_bin_lcoeff

    l = grad_bin_lcoeff * grad_mag
    r = grad_bin_rcoeff * grad_mag


    for i in range(grad_mag.shape[0]):
        for j in range(grad_mag.shape[1]):
            ret_bin[grad_bin_idx_l[i][j]] += l[i][j]
            ret_bin[grad_bin_idx_r[i][j]] += r[i][j]


    return ret_bin

def bilinear_HOG_DB(im: np.ndarray, patch_num=(3, 4)):

    grad_dir, grad_mag = compute_grad(im)

    patch_size = (30. / patch_num[0], 18. / patch_num[1])
    ret_feature = []

    for idx_h in range(patch_num[1]):
        for idx_w in range(patch_num[0]):
            patch_grad_dir = grad_dir[
                             :,
                int(idx_h * patch_size[1]): int((idx_h + 1) * patch_size[1]),
                int(idx_w * patch_size[0]): int((idx_w + 1) * patch_size[0])
            ]

            patch_grad_mag = grad_mag[
                int(idx_h * patch_size[1]): int((idx_h + 1) * patch_size[1]),
                int(idx_w * patch_size[0]): int((idx_w + 1) * patch_size[0])
            ]

            ret_feature.append(bilinear_HOG(patch_grad_dir, patch_grad_mag))
    ret_feature = np.concatenate(ret_feature)

    assert ret_feature.shape == (patch_num[0] * patch_num[1] * 12,)

    return ret_feature

def KNN_HOG(train_X, train_Y, val_x, k=1):

    vdb = bilinear_HOG_DB(val_x)

    result = np.argsort(np.array([np.linalg.norm(bilinear_HOG_DB(train_X[i]) - vdb) for i in range(len(train_X))]))[:k]

    return sum(map(lambda x: (1/np.linalg.norm(bilinear_HOG_DB(train_X[x]) - vdb))*train_Y[x], result)) / sum(map(lambda x: 1 / np.linalg.norm(bilinear_HOG_DB(train_X[x]) - vdb), result))

