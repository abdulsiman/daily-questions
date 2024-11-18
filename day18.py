import math
def square_root(n):
    sqrt = math.isqrt(n)
    if sqrt*sqrt==n:
        return f'Square root of {n} is {sqrt}'
    else:
        return f'{n} is not a perfect square'
num = int(input("Enter the number of your choice: "))
result = square_root(num)
print(result)
