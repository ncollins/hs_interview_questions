"""
Rotate a matrix inplace.
This only demonstrates 90 degree clockwise rotation.
Matrix is considered to be a list of row lists,
e.g.
    [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
    ]

It uses 4 temporary values to store a given 'orbit'
of matrix elements. It starts at the outer layer of the
matrix and works inwards.
"""

def rotate(m):
    n = len(m)
    for layer in range(n//2):
        # We move inwards from starting at the outer layer of the matrix.
        # // is the integer division operation, we round down as for an odd
        # sized matrix we don't need to rotate the center element.
        for i in range(n-1-2*layer):
            # We then circle around the current layer, we reduce the upper bound
            # by 2*layer we lose both top/bottom and left/right sides of the
            # outer matrix.
            # FIRST: set up temp variables
            a = m[layer][layer+i] # top left element of orbit
            b = m[layer+i][n-1-layer] # top right
            c = m[n-1-layer][n-1-layer-i] # bottom right
            d = m[n-1-layer-i][layer] # bottom left
            # SECOND: rotate the elements in current orbit
            m[layer][layer+i] = d
            m[layer+i][n-1-layer] = a
            m[n-1-layer][n-1-layer-i] = b
            m[n-1-layer-i][layer] = c
            
 
def print_matrix(m):
    print('[')
    for row in m:
        print(row)
    print(']')

if __name__ == '__main__':
    m3 = [[1,2,3], [4,5,6], [7,8,9]]
    rotate(m3)
    print_matrix(m3)
    m4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    rotate(m4)
    print_matrix(m4)
    m5 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    rotate(m5)
    print_matrix(m5)
