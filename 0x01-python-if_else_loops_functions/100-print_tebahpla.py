#!/usr/bin/python3
for number in range(122, 96, -1):
    print(chr(number)if number % 2 == 0 else chr(number-32), end='')
