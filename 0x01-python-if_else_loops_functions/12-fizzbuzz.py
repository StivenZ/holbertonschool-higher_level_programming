#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a != range(1, 101)[-1]:
            if a % 3 == 0:
                print("Fizz ", end='')
                continue
            elif a % 5 == 0:
                print("Buzz ", end='')
                continue
            elif a % 5 == 0 and a % 3 == 0:
                print("FizzBuzz ", end='')
                continue
            else:
                print(a, end=' ')
