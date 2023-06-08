# Q7. Calculate the factorial of a number using lambda function.

factorial = lambda number: 1 if number==0 else number * factorial(number-1)

print(factorial(5))
