#!/usr/bin/python3
Square = __import__('6-square').Square

#my_square_2 = Square(3, (1, 1, 1))
#my_square_2.my_print()

#print("**********3,(1, 1)")
my_square = Square(3,(1,1))
print(my_square.size)
print(my_square.area())
print(my_square.position)
