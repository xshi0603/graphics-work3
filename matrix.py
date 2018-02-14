import math


def print_matrix( matrix ):
    retVal = ""
    rows = 4
    cols = 4
    for c in range( cols ):
        for r in range( rows ):
            retVal += str( matrix[c][r])
            retVal += "\t"
        retVal += "\n"
    print retVal

def ident( matrix ):
    rows = 4
    cols = 4
    for c in range( cols ):
        for r in range( rows ):
            if (c == r):
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0


#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
