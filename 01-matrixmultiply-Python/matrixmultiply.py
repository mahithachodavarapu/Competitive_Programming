# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    row1=len(m1)
    row2=len(m2)
    col1=len(m1[0])
    col2=len(m2[0])
    result=None
    for i in range(row1):
        if(len(m1[i]) != col1):
            return result
    for i in range(row2):
        if(len(m2[i]) != col2):
            return result
    if(col1 != row2):
        return result
    
    a = []
    for row in range(row1):
        a += [[0]*col2]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                a[i][j]+=m1[i][k]*m2[k][j]


    return a



