def ams(n):
    digits=str(n)
    power=len(digits)
    
    return n==sum(int(digit)**power for digit in digits)

num=int(input("Enter the number:"))

if ams(num):
    print(f"{num} is a amstrong number..")
else:
    print(f"{num} is not a amstrong number")
    




    
    