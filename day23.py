n=int(input("Enter the number of elements you want to enter: "))
ls=[]
for i in range(n):
    num=int(input("Enter a number: "))
    ls.append(num)
target=int(input("Enter your target: "))
found=False
for i in range(n):
    for j in range(i+1,n):
        if ls[i]+ls[j]==target:
            print(f"Target found by summing {ls[i]} and {ls[j]}")
            found=True
            break
    if found:
        break
if not found:
    print("No pair found that adds up to your target.")


