sum=0

while True:
    n=input("Enter your numbers and press 'x' to stop:")
    if n.lower()=='x':
        break
    elif n.isdigit():
        sum+=int(n)
    else:
        print("Enter a valid number...")
print(f"The sum of your number is {sum}")