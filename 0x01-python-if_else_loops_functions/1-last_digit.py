#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if lastdigit > 5:
    print("Last digit of {} is {}".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {} and is 0".format(number))
elif lastdigit < 6 and lastdigit != 0:
    print("Last digit of {} and is less than 6 and not 0".format(number))
