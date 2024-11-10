def linear_search(ls, target):
    for index in range(len(ls)):
        if ls[index] == target:
            return index
    else:
        return -1
ls = []
n = int(input("Enter number of elements u want to enter: "))
for i in range(1, n+1):
	num = int(input(f"Enter ur number {i}:"))
	ls.append(num)
print(f"The entered elemnts are:{ls}")
target=int(input("Enter the target element:"))
result = linear_search(ls, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")

        