lst=[]
n=int(input("Enter number of elements you want to enter in a list: "))
for i in range(0, n):
	inputs=(input())
	lst.append(inputs)
print(lst)
for i in set(lst):
    count = lst.count(i)
    print(f"{i}-{count}")

