from display import *
from draw import *
from matrix import *

from decimal import *
getcontext().prec = 2
asd = 0.123123
print(asd)

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print("Testing print_matrix()")
print_matrix( matrix )

print("Testing ident() on 4x4")
ident(matrix)
print_matrix( matrix )

print("Testing ident() on 5x5")
five_matrix = new_matrix(5,5)
ident(five_matrix)
print_matrix( five_matrix )

print("Testing add_point(matrix, 10, 20, 30)")
add_point( matrix, 10, 20, 30 )
print_matrix( matrix )

print("Testing add_point(matrix, 100, 200, 300)")
add_point( matrix, 100, 200, 300 )
print_matrix( matrix )

print("Testing add_edge( matrix, 0, 0, 0, 300, 300, 0)")
add_edge( matrix, 0, 0, 0, 300, 300, 0)
print_matrix( matrix )

print("Testing matrix_mult")

m1 = new_matrix(2, 2) #2x2
m2 = new_matrix(2, 2) #2x2
m1[0][0] = 2
m1[1][0] = -2
m1[0][1] = 5
m1[1][1] = 3
m2[0][0] = -1
m2[1][0] = 4
m2[0][1] = 7
m2[1][1] = -6

print("m1*m2")
print("Printing m1")
print_matrix( m1 )
print("Printing m2")
print_matrix( m2 )

matrix_mult(m1, m2)
print("After multiplication...")
print("Printing m1")
print_matrix( m1 )
print("Printing m2")
print_matrix( m2 )

print("ident*m1")
i1 = new_matrix(2,2)
ident(i1)
print("Printing Ident")
print_matrix( i1 )
print("Printing m1")
print_matrix( m1 )

matrix_mult(i1, m1)
print("After multiplication...")
print("Printing Ident")
print_matrix( i1 )
print("Printing m1")
print_matrix( m1 )

print("Adding many edges...")
add_edge( matrix, 500, 0, 0, 0, 0, 0)
add_edge( matrix, 123, 321, 0, 321, 123, 0)

print("Adding a point")
add_point( matrix, 0, 0, 0)

print("Drawing:")
print_matrix(matrix)
draw_lines( matrix, screen, color )

print("Translating up 250:")
trans = new_matrix()
ident(trans)
trans[3][0] = 0
trans[3][1] = 250
trans[3][2] = 25

print("Translation matrix")
print_matrix(trans)
matrix_mult(trans, matrix)

print("Drawing:")
print_matrix(matrix)
draw_lines( matrix, screen, color )

display(screen)
