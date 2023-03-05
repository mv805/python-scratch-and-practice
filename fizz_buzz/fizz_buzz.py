"""
https://leetcode.com/problems/fizz-buzz/description/
412.

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""


def fizzBuzz(n):
    result = []
    for number in range(1, n+1):
        if((number % 3 == 0) and (number % 5 == 0)):
            result.append("FizzBuzz")
        elif(number % 3 == 0):
            result.append("Fizz")
        elif(number % 5 == 0):
            result.append("Buzz")
        else:
            result.append( f"{number}")
    return result

