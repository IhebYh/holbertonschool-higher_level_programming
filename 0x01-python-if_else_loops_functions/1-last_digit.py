#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    nmbr = -number % 10
else:
    nmbr = number % 10
if nmbr > 5:
    print("Last digit of {:d} is {:d}".format(number, nmbr), end=" ")
    print("and is greater than 5")
elif nmbr == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, nmbr))
elif nmbr < 6 and nmbr != 0:
    print("Last digit of {:d} is {:d}".format(number, nmbr), end=" ")
    print("and is less than 6 and not 0")
