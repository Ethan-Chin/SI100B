## Feel free to import handy built-in modules here

## Self-defined exceptions
## Please **DO NOT MODIFITY** the following exceptions!


class MatrixKeyError(Exception):
    pass

class MatrixValueError(Exception):
    pass

class MatrixSizeError(Exception):
    pass

class ObjectError(Exception):
    pass

class SizeUnmatchedError(Exception):
    pass

class ScalarTypeError(Exception):
    pass

class NotSquaredError(Exception):
    pass

class NotInvertibleError(Exception):
    pass

class IndexSyntaxError(Exception):
    pass

## Feel free to define your own functions here
def caldet(mat):

    if len(mat) == 1:
        return mat[0][0]
    
    else:
        result = 0

        for i in range(len(mat)):

            newmat = []

            for j in mat[1:]:

                row = []

                for jj in range(len(mat)):

                    if jj != i:
                        row.append(j[jj])
                newmat.append(row)

            if i % 2 == 0:
                result += mat[0][i] * caldet(newmat)
            
            else:
                result -= mat[0][i] * caldet(newmat)
            
        return result



## Your implementations start here
class Matrix:
    def __init__(self, m, n, expr):
        try:
            if type(m) != int or m <= 0 or type(n) != int or n <= 0:
                raise MatrixSizeError
        except:
            raise MatrixSizeError
        ###判断m和n是不是正整数，不是就报SIZE错

        self.matrix = []
        self.m = m
        self.n = n
        self.shape = (m, n)
        ###保存数据

        for i in range(m):

            row = []

            for ii in range(n):
                row.append(0)
            
            self.matrix.append(row)

        ###创建mxn的零矩阵

        temp1 = expr.replace(' ', '')
        temp1 = temp1.replace('\n', '')
        temp1 = temp1.replace('\r', '')
        temp1 = temp1.replace('\t', '')
        ###去掉输入字符串中的空白字符
        
        if '[;' in temp1:
            raise MatrixValueError
        ###排除没有value的情况，发生了就报VALUE错

        temp1 = temp1.replace(';', ',')
        temp = temp1[1:-1]
        temp = temp.replace(']],', ']]?')
        ###把分号全变成逗号，方便之后eval转换
        ###新建一个没有首尾中括号的字符串
        ###新字符串插入标签，方便后面断开

        cuts = temp.split('?')
        ###新字符串断成一节一节，变成list

        for i in range(len(cuts)):
            ###遍历新list的每一块
            end = cuts[i].find(',')
            ###标出每一块里面value结束的位置

            if cuts == ['']:
                cuts = []
                break
            ###排除空字符串的列表，发生了就跳出去

            try:
                eval(cuts[i][1:end])
            except:
                raise MatrixValueError
            ###尝试转换每一行的value，转换不成功就报VALUE错，排除value的转换问题

        try:
            cuts = eval(temp1)
        except:
            raise MatrixKeyError
        ###把原字符串转换，转换不成功就只能是key的问题，报KEY错


        for i in cuts:
            ###开始存数据

            for ii in i:
                if not i.index(ii):
                    value = ii
                ###判断，如果是value的话（即第一个），就存到value中

                    if type(value) != int and type(value) != float:
                        raise MatrixValueError
                    ###如果value不是整数或浮点数，则报VALUE错

                else:
                    ###如果不是value就是key（因为前面已经排除了没有value的情况）
                    try:
                        for iii in ii:
                            ###对于key中的每一个坐标tuple

                            key = iii

                            if type(key) != tuple:
                                raise MatrixKeyError
                                ###不是tuple就报KEY错

                            elif len(key) != 2:
                                raise MatrixKeyError
                                ###tuple不是两个坐标就报KEY错

                            elif type(key[0]) != int or type(key[1]) != int:
                                raise MatrixKeyError
                                ###两个坐标不是整数就报KEY错

                            try:
                                self.matrix[key[0]][key[1]] = value
                            except:
                                raise MatrixKeyError
                            ###给矩阵的第key[0]行第key[1]列赋值为value，越界就报KEY错
                    except:
                        raise MatrixKeyError
                    ###保险起见，一出错必是报KEY错




    def __str__(self):

        result = '['
        ###先搞出中括号

        for i in range(self.m):
            ###进入每一行里面

            for ii in range(self.n):
                ###进入每一行的每一个元素，每一行的元素个数等于列数

                if type(self.matrix[i][ii]) == float:
                    temp = '%.5f' % self.matrix[i][ii]
                    result += str(temp)
                ###判断这个元素是不是浮点数，如果是的话，就保留五位小数，再转换成字符串，加到结果上
                else:
                    result += str(self.matrix[i][ii])
                ###如果不是浮点数就是整数，整数就直接转换成字符串加到结果后面
                if ii != (self.n - 1):
                    result += ','
                ###如果这不是一行的最后一个元素，就加上一个逗号
                else:
                ###如果是这一行的最后一个元素，就分两种情况
                    if i != (self.m - 1):
                        result += ';'
                    ###如果不是最后一行，那就加上一个分号
                    else:
                        result += ']'
                    ###如果是最后一行，就直接加上右中括号


        return result

    def __add__(self, other):

        if type(other) != Matrix:
            raise ObjectError

        if self.m != other.m or self.n != other.n:
            raise SizeUnmatchedError
        
        result = Matrix(self.m, self.n, '[]')

        for i in range(self.m):
            for ii in range(self.n):
                result.matrix[i][ii] = self.matrix[i][ii] + other.matrix[i][ii]
        
        return result


    
    def __sub__(self, other):

        if type(other) != Matrix:
            raise ObjectError

        if self.m != other.m or self.n != other.n:
            raise SizeUnmatchedError
        
        result = Matrix(self.m, self.n, '[]')

        for i in range(self.m):
            for ii in range(self.n):
                result.matrix[i][ii] = self.matrix[i][ii] - other.matrix[i][ii]
        
        return result
    
    def __mul__(self, other):

        if type(other) == Matrix:

            if self.n != other.m:
                raise SizeUnmatchedError

            result = Matrix(self.m, other.n, '[]')

            for i in range(self.m):

                for ii in range(other.n):

                    data = 0
                    for iii in range(self.n):
                        data += (self.matrix[i][iii])*(other.matrix[iii][ii])

                    result.matrix[i][ii] = data
            
            return result



        elif type(other) == int or type(other) == float:

            result = Matrix(self.m, self.n, '[]')

            for i in range(self.m):
                for ii in range(self.n):
                    result.matrix[i][ii] = self.matrix[i][ii] * other
            
            return result



        else:
            raise ObjectError



    def __truediv__(self, other):

        if type(other) != int and type(other) != float:
            raise ObjectError

        result = Matrix(self.m, self.n, '[]')

        for i in range(self.m):
            for ii in range(self.n):
                result.matrix[i][ii] = self.matrix[i][ii] / other
        
        return result


    def __eq__(self, other):
        
        if type(other) != Matrix:
            raise ObjectError

        if self.m != other.m or self.n != other.n:
            return False

        try:
            for i in range(self.m):
                for ii in range(self.n):
                    if self.matrix[i][ii] != other.matrix[i][ii]:
                        return False
        except:
            return False

        return True


    
    def transpose(self):

        result = Matrix(self.n, self.m, '[]')

        for i in range(self.m):
            for ii in range(self.n):
                result.matrix[ii][i] = self.matrix[i][ii]
        
        return result



    def det(self):
        
        if self.m != self.n:
            raise NotSquaredError
        
        return caldet(self.matrix)          



    def inv(self):

        try:
            det = self.det()
        except:
            raise NotSquaredError

        if not det:
            raise NotInvertibleError
        
        NonTAdjmat = Matrix(self.m, self.n, '[]')

        for i in range(self.m):
            for j in range(self.n):

                co = []

                for ii in range(self.m):

                    if ii != i:

                        corow = []

                        for jj in range(self.n):
                            if jj != j:
                                corow.append(self.matrix[ii][jj])

                        co.append(corow)
                
                NonTAdjmat.matrix[i][j] = ((-1)**(i+j))*caldet(co)
        
        Adjmat = NonTAdjmat.transpose()

        return (Adjmat / caldet(self.matrix))


    def __getitem__(self, key):
        
        try:
            if type(key) == int:

                result = Matrix(1, self.n, '[]')

                for i in range(self.n):
                    result.matrix[0][i] = self.matrix[key][i]

            
            elif type(key) == tuple:
                if len(key) != 2:
                    raise IndexSyntaxError

                if type(key[0]) == int and type(key[1]) == int:
                    result = self.matrix[key[0]][key[1]]

                elif type(key[0]) == slice and type(key[1]) == slice:
                    rowStart = key[0].start
                    rowStop = key[0].stop
                    rowStep = key[0].step
                    colStart = key[1].start
                    colStop = key[1].stop
                    colStep = key[1].step
                    
                    if rowStep == None:
                        rowStep = 1
                    
                    if colStep == None:
                        colStep = 1
                    
                    sliceMatrix = []

                    for i in range(rowStart, rowStop, rowStep):

                        row = []

                        for j in range(colStart, colStop, colStep):

                            row.append(self.matrix[i][j])
                        
                        sliceMatrix.append(row)
                    
                    m = len(sliceMatrix)
                    n = len(sliceMatrix[0])

                    result = Matrix(m, n, '[]')

                    result.matrix = sliceMatrix

                else:
                    raise IndexSyntaxError

            else:
                raise IndexSyntaxError


            return result

        except:
            raise IndexSyntaxError

    def __setitem__(self, key, value):

        try:
            if type(key) == int:

                
                if type(value) != Matrix:
                    raise IndexSyntaxError

                elif value.m != 1 or value.n != self.n:
                    raise IndexSyntaxError


                for i in range(self.n):
                    self.matrix[key][i] = value.matrix[0][i]


            elif type(key) == tuple:
                if len(key) != 2:
                    raise IndexSyntaxError

                if type(key[0]) == int and type(key[1]) == int:
                    if type(value) != int and type(value) != float:
                        raise MatrixValueError
                    self.matrix[key[0]][key[1]] = value

                elif type(key[0]) == slice and type(key[1]) == slice:

                    if type(value) != Matrix:
                        raise IndexSyntaxError

                    rowStart = key[0].start
                    rowStop = key[0].stop
                    rowStep = key[0].step
                    colStart = key[1].start
                    colStop = key[1].stop
                    colStep = key[1].step

                    if rowStep == None:
                        rowStep = 1
                    
                    if colStep == None:
                        colStep = 1
                    
                    sliceMatrix = []
                    ii = 0
                    for i in range(rowStart, rowStop, rowStep):

                        row = []
                        jj = 0

                        for j in range(colStart, colStop, colStep):

                            row.append(self.matrix[i][j])
                            self.matrix[i][j] = value.matrix[ii][jj]
                            jj += 1
                        
                        sliceMatrix.append(row)
                        ii += 1
                    
                    m = len(sliceMatrix)
                    n = len(sliceMatrix[0])

                    if m != value.m or n != value.n:
                        raise IndexSyntaxError


                else:
                    raise IndexSyntaxError

            else:
                raise IndexSyntaxError



        except MatrixValueError:
            raise MatrixValueError

        except:
            raise IndexSyntaxError


        

    ## Self-defined methods
    ## Feel free to define your own methods for class Matrix here

class KF:
    def predict(self, x_pre, P_pre, u_k, F, B, Q):
        
        n, m = x_pre.shape[0], u_k.shape[0]
        
        if x_pre.shape != (n, 1) or P_pre.shape != (n, n) or u_k.shape != (m, 1) or F.shape != (n, n) or B.shape != (n, m) or Q.shape != (n, n):
            raise SizeUnmatchedError

        x_now = (F * x_pre) + (B * u_k)

        P_now = ((F * P_pre) * F.transpose()) + Q

        return x_now, P_now

    def update(self, x_pre, P_pre, z_k, H, R):

        n, k = x_pre.shape[0], z_k.shape[0]

        if x_pre.shape != (n, 1) or P_pre.shape != (n, n) or z_k.shape != (k, 1) or H.shape != (k, n) or R.shape != (k, k):
            raise SizeUnmatchedError

        K = (P_pre * H.transpose()) * (((H * P_pre) * H.transpose()) + R).inv()

        x_hat = x_pre + (K * (z_k - (H * x_pre)))

        P_hat = P_pre - ((K * H) * P_pre)

        return x_hat, P_hat
        
def postfix_eval(expr):
    
    storeBox = []

    for i in expr:
        try:
            if i == '+':
                storeBox=[storeBox[0] + storeBox[1]]
            elif i == '-':
                storeBox=[storeBox[0] - storeBox[1]]
            elif i == '*':
                if type(storeBox[0]) == int or type(storeBox[0]) == float:
                    storeBox = [storeBox[1] * storeBox[0]]
                else:
                    storeBox = [storeBox[0] * storeBox[1]]
            elif i == '/':
                storeBox = [storeBox[0] / storeBox[1]]
            else:
                storeBox.append(i)
        except:
            storeBox.append(i)

    return storeBox[0]

if __name__ == "__main__":
    
    ## Tests for Task 2
    ## normal test
    test_m1 = 5
    test_n1 = 5
    test_expr1 = \
        '''[[2; [(1, 2); (1, 0)]]; 
            [3; [(0, 2); (1, 1); (2, 0)]]; 
            [4; [(0, 1); (2, 1)]];
            [5; [(2, 2)]]]'''

    mat1 = Matrix(test_m1, test_n1, test_expr1)
    mat1_ans = str(mat1)

    if mat1_ans == '[0,4,3,0,0;2,3,2,0,0;3,4,5,0,0;0,0,0,0,0;0,0,0,0,0]':
        print('Pass normal test of Task 2.')
    else:
        print('Fail normal test of Task 2.')
    
    ## exception tests
    ## MatrixSizeError test
    test_m1_err = 3.0
    try:
        mat1 = Matrix(test_m1_err, test_n1, test_expr1)
    except MatrixSizeError:
        print('Pass MatrixSizeError test of Task 2.')
    except:
        print('Fail MatrixSizeError test of Task 2.')
    else:
        print('Fail MatrixSizeError test of Task 2.')
    
    ## MatrixKeyError test
    test_expr1_err1 = \
        '''[[2; [(0, 1); (1, 0)]]; 
            [3; [(0, 2); (1, 1); (2, 0)]]; 
            [4; [(1, 2.0); (2, 1)]];
            [5; [(2, 2)]]]'''
    try:
        mat1 = Matrix(test_m1, test_n1, test_expr1_err1)
    except MatrixKeyError:
        print('Pass MatrixKeyError test of Task 2.')
    except:
        print('Fail MatrixKeyError test of Task 2.')
    else:
        print('Fail MatrixKeyError test of Task 2.')
    
    ## MatrixValueError test
    test_expr1_err2 = \
        '''[[2; [(0, 1); (1, 0)]]; 
            [3; [(0, 2); (1, 1); (2, 0)]]; 
            [4+1j; [(1, 2); (2, 1)]];
            [5; [(2, 2)]]]'''
    try:
        mat1 = Matrix(test_m1, test_n1, test_expr1_err2)
    except MatrixValueError:
        print('Pass MatrixValueError test of Task 2.')
    except:
        print('Fail MatrixValueError test of Task 2.')
    else:
        print('Fail MatrixValueError test of Task 2.')

    ## Tests for Task 3
    add_res = mat1 + mat1
    sub_res = mat1 - mat1
    if str(add_res) == '[0,8,6,0,0;4,6,4,0,0;6,8,10,0,0;0,0,0,0,0;0,0,0,0,0]':
        print('Pass Addition Test.')
    else:
        print('Fail Addition Test')

    if str(sub_res) == '[0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0]':
        print('Pass Subtraction Test.')
    else:
        print('Fail Subtraction Test')

    mul_res1 = mat1 * mat1
    mul_res2 = mat1 * 1.5

    if str(mul_res1) == '[17,24,23,0,0;12,25,22,0,0;23,44,42,0,0;0,0,0,0,0;0,0,0,0,0]':
        print('Pass Multiplication Test 1.')
    else:
        print('Fail Multiplication Test 1.')
    
    if str(mul_res2) == '[0.00000,6.00000,4.50000,0.00000,0.00000;3.00000,4.50000,3.00000,0.00000,0.00000;4.50000,6.00000,7.50000,0.00000,0.00000;0.00000,0.00000,0.00000,0.00000,0.00000;0.00000,0.00000,0.00000,0.00000,0.00000]':
        print('Pass Multiplication Test 2.')
    else:
        print('Fail Multiplication Test 2.')
    
    div_res = mat1 / 1.5
    if str(div_res) == '[0.00000,2.66667,2.00000,0.00000,0.00000;1.33333,2.00000,1.33333,0.00000,0.00000;2.00000,2.66667,3.33333,0.00000,0.00000;0.00000,0.00000,0.00000,0.00000,0.00000;0.00000,0.00000,0.00000,0.00000,0.00000]':
        print('Pass Division Test.')
    else:
        print('Fail Division Test.')

    if not mat1 == div_res:
        print('Pass Equalization Test 1.')
    else:
        print('Fail Equalization Test 1.')

    if mat1 == mat1:
        print('Pass Equalization Test 2.')
    else:
        print('Fail Equalization Test 2.')

    mat1_2 = Matrix(3, 3, test_expr1)

    if str(mat1_2.transpose()) == '[0,2,3;4,3,4;3,2,5]':
        print('Pass Transpose Test.')
    else:
        print('Fail Transpose Test.')

    ## Test for Task 4
    if mat1_2.det() == -19:
        print('Pass Determinant Test.')
    else:
        print('Fail Determinant Test.')

    if str(mat1_2.inv()) == '[-0.36842,0.42105,0.05263;0.21053,0.47368,-0.31579;0.05263,-0.63158,0.42105]':
        print('Pass Inverse Test.')
    else:
        print('Fail Inverse Test.')

    ## Test for Task 5
    # print('mat1[1]:', mat1[1])
    print(str(mat1))
    if str(mat1[1]) == '[2,3,2,0,0]':
        print('Pass Test 1 for Task 5')
    else:
        print('Fail Test 1 for Task 5')
    
    if mat1[1, 1] == 3:
        print('Pass Test 2 for Task 5')
    else:
        print('Fail Test 2 for Task 5')

    if str(mat1[0:3, 1:4]) == '[4,3,0;3,2,0;4,5,0]':
        print('Pass Test 3 for Task 5')
    else:
        print('Fail Test 3 for Task 5')

    mat2 = Matrix(2, 3,
        '''[[1; [(0, 0)]]; 
            [2; [(0, 1)]]; 
            [3; [(0, 2)]];
            [4; [(1, 0)]]; 
            [5; [(1, 1)]]; 
            [6; [(1, 2)]]]'''
        )
    mat1[0:2,1:4] = mat2
    if str(mat1) == '[0,1,2,3,0;2,4,5,6,0;3,4,5,0,0;0,0,0,0,0;0,0,0,0,0]':
        print('Pass Test 4 for Task 5')
    else:
        print('Fail Test 4 for Task 5')
    
    mat3 = Matrix(1, 5,
        '''[[1; [(0, 0); (0, 1); (0, 2); (0, 3); (0, 4)]]]''')
    mat1[2] = mat3
    if str(mat1) == '[0,1,2,3,0;2,4,5,6,0;1,1,1,1,1;0,0,0,0,0;0,0,0,0,0]':
        print('Pass Test 5 for Task 5')
    else:
        print('Fail Test 5 for Task 5')
    
    mat1[3, 3] = 2.333
    if str(mat1) == '[0,1,2,3,0;2,4,5,6,0;1,1,1,1,1;0,0,0,2.33300,0;0,0,0,0,0]':
        print('Pass Test 6 for Task 5')
    else:
        print('Fail Test 6 for Task 5')

    ## Test for Task 6
    x_pre = Matrix(3, 1, 
        '''[[0; [(0, 0)]]; 
            [1; [(1, 0)]]; 
            [2; [(2, 0)]]]''')
    P_pre = Matrix(3, 3,
        '''[[1; [(0, 0)]];
            [2; [(0, 1)]]; 
            [3; [(0, 2)]];
            [4; [(1, 0)]]; 
            [5; [(1, 1)]];
            [6; [(1, 2)]]; 
            [7; [(2, 0)]]; 
            [8; [(2, 1)]];
            [9; [(2, 2)]]]''')
    u = Matrix(3, 1, 
        '''[[0.1; [(0, 0)]]; 
            [0.2; [(1, 0)]]; 
            [0.3; [(2, 0)]]]''')
    F = Matrix(3, 3,
        '''[[1; [(0, 0); (1, 1); (2, 2)]]]''')
    B = Matrix(3, 3,
        '''[[4; [(0, 0)]];
            [5; [(1, 1)]];
            [6; [(2, 2)]]]''')
    Q = F * 0.02
    z = Matrix(3, 1, 
        '''[[1; [(0, 0)]]; 
            [3; [(1, 0)]]; 
            [4; [(2, 0)]]]''')
    H = F * 2
    R = F * 0.03

    kf = KF()
    x_predicted, P_predicted = kf.predict(x_pre, P_pre, u, F, B, Q)
    x_updated, P_updated = kf.update(x_predicted, P_predicted, z, H, R)
    
    test1 = str(x_predicted) == '[0.40000;2.00000;3.80000]'
    test2 = str(P_predicted) == '[1.02000,2.00000,3.00000;4.00000,5.02000,6.00000;7.00000,8.00000,9.02000]'
    test3 = str(x_updated) == '[0.53589;1.43717;2.02935]'
    test4 = str(P_updated) == '[0.00720,0.00069,-0.00036;0.00069,0.00614,0.00068;-0.00037,0.00067,0.00717]'

    if test1 and test2:
        print('Pass Prediction Test.')
    else:
        print('Fail Prediction Test.')

    if test3 and test4:
        print('Pass Update Test.')
    else:
        print('Fail Update Test.')

    A = Matrix(3, 3,
        '''[[1; [(0, 0)]];
            [2; [(0, 1); (1, 0)]]; 
            [3; [(0, 2); (1, 1); (2, 0)]];
            [4; [(1, 2); (2, 1)]]; 
            [5; [(2, 2)]]]''')
    B = 1.5
    C = Matrix(3, 3,
        '''[[1; [(0, 0); (1, 1); (2, 2)]]]''')
    D = Matrix(3, 3,
        '''[[1; [(0, 0); (1, 1); (2, 2)]]]''')

    test_postfix_expr = [A, B, '*', C, '+', D, '-']
    if postfix_eval(test_postfix_expr) == A*B+C-D:
        print('Pass Postfix Evaluation.')
    else:
        print('Fail Postfix Evaluation.')
