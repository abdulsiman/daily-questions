def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
a=int(input("Enter the number u want the sum of:"))
print(f"The sum of {a} is {sum(a)}")