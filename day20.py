n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
target = int(input("Enter the target value: "))

mat = []
for i in range(n):
    row = list(map(int, input(f"Enter the elements of row {i+1} (space separated): ").split()))
    mat.append(row)

found = False
for i in range(n):
    for j in range(m):
        if mat[i][j] == target:
            print(f"true\nIndex of target {target}: ({i}, {j})")
            found = True
            break
    if found:
        break

if not found:
    print("false")







