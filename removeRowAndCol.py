# removeRowAndCol (non-destructive and destructive)
# Here we will write removeRowAndCol(row, col), 
# Do not use copy.deepcopy and directly construct 
# the modified 2d list.

# The function takes a rectangular list L and two ints, 
# row and col. the goal is to obtain a version of the list 
# that has the given row and given column removed. 
# You may assume that row and col are both legal values 
# (that is, they are non-negative integers that are smaller 
# than the largest row and column, respectively). For example, 
# the list shown to the left would lead to the result shown on 
# the right when called with row 1 and column 2.

l= [ [ 2, 3, 4, 5],  [ 8, 7, 6, 5], [ 0, 1, 2, 3] ]
row=1
col=2

# result
# [ [ 2, 3, 5],
#   [ 0, 1, 3] ]

def removeRowAndCol(l, row, col):
    # Your code goes here...
    
    l.remove(l[row])
    #print(l)
    le=len(l)
    for i in range(le):
        l[i].remove(l[i][col])
        
    return l
print(removeRowAndCol(l, row, col))
    

# Write your own test cases.