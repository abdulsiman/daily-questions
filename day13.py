l = []
n = int(input("Enter number of elements : "))
for i in range(1, n+1):
	num = int(input(f"Enter ur number {i}:"))
	l.append(num)
print(f"Ur entered numbers are {l}")
l.reverse()
print(f"The enterd numbers in reverse order is {l}")