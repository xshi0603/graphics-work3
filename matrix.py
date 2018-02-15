import math


def print_matrix( matrix ):
    retVal = ""
    rows = len(matrix[0])
    cols = len(matrix)
    


    for r in range( rows ):
        for c in range( cols ):
            retVal += str( matrix[c][r])
            retVal += "\t"
        retVal += "\n"

    print retVal

def ident( matrix ):
    rows = len(matrix)
    cols = rows
    for c in range( cols ):
        for r in range( rows ):
            if (c == r):
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    rows = len(m1[0]) #length of a column = rows
    cols = len(m2) #length of a row = columns
    const = len(m1) #using len(m2) should be the same
    temp = 0

    new_m = new_matrix(rows, cols)
    for c in range( cols ):
        for r in range( rows ):#new matrix
            for l in range( const ):#old ones
                temp += m1[l][r]
                temp *= m2[c][l]
                new_m[c][r] += temp
                temp = 0
    #up to here works for all matrices
    #now we are going to assume m1 is a square matrix
    for c in range( cols ):
        for r in range( rows ):
            m2[c][r] = new_m[c][r]



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
