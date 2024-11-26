def factor_of_number(n):
    f=[]
    for i in range(1,n+1):
        if n%i==0:
            f.append(i)
    return f
c=int(input("Enter a number you want the factor of:"))
s=factor_of_number(c)
print(f"These are the factors of your given number:{s}")

    