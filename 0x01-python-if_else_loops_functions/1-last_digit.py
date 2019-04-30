#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = number
number2 = 10
while (abs(number1) < 10):
    number1 = number1 // 10
    number2 = number2 * 10

last_num = abs(number) % number2
print("Last digit of {:d} is {:d}".format(number,last_num), end =" ")
if (last_num > 5):
    print("and is greater than 5")
elif(last_num == 0):
    print("and is 0")
else:
    print("and is less than 6 and not 0")
