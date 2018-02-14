from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print_matrix( matrix )

matrix[0][0] = 256
print_matrix( matrix )

ident(matrix)
print_matrix( matrix )

#draw_lines( matrix, screen, color )
#display(screen)
