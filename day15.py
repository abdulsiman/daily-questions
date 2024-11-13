num1=int(input("Enter your num1:"))
num2=int(input("Enter your num2:"))
num3=int(input("Enter your num3:"))
def maximum(num1,num2,num3):
    if(num1>=num2 and num1>=num3):
        print(f"{num1} is maximum")
    elif(num2>=num1 and num2>=num3):
        print(f"{num2} is maximum")
    elif(num3>=num2 and num3>=num1):
        print(f"{num3} is maximum")
def minimum(num1,num2,num3):
    if(num1<=num2 and num1<=num3):
        print(f"{num1} is manimum")
    elif(num2<=num1 and num2<=num3):
        print(f"{num2} is manimum")
    elif(num3<=num2 and num3<=num1):
        print(f"{num3} is manimum")
maximum(num1,num2,num3)
minimum(num1,num2,num3)
