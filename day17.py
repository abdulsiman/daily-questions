lst = []
n = int(input("Enter number of elements you want to enter in a list: "))
for i in range(0, n):
    inputs = int(input())
    lst.append(inputs)
print(f"Original list:{lst}")

for i in range(0, len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print(f"Sorted list:{lst}")
