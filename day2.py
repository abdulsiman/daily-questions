n=int(input("Enter the table you want to print:"))
print("The table in straight order is:")
for i in range(1,11):
    print(f"{n}x{i}={n*i}")
print("The table in reverse order is:")
for i in range(1,11):
    print(f"{n}x{11-i}={n*(11-i)}")