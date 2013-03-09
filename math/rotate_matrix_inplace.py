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
    for level in range(n//2):
        for i in range(n-1-2*level):
            # set up temp variables
            a = m[level][level+i] # top left element of orbit
            b = m[level+i][n-1-level] # top right
            c = m[n-1-level][n-1-level-i] # bottom right
            d = m[n-1-level-i][level] # bottom left
            # rotate the elements in current orbit
            m[level][level+i] = b
            m[level+i][n-1-level] = c
            m[n-1-level][n-1-level-i] = d
            m[n-1-level-i][level] = a
            
 
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
