l = []
n = int(input("Enter number of elements : "))
for i in range(1, n+1):
	num = int(input(f"Enter ur number {i}:"))
	l.append(num) 
max_num=max(l)
print(f"The maximum number is {max_num}")
