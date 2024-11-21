def max_ones(nums):
    max_count=0
    current_count=0
    for num in nums:
        if num==1:
            current_count+=1
            max_count=max(max_count,current_count)
        else:
            current_count=0
    return max_count

n=int(input("Enter the number of elements:"))
ls=[]
for i in range(n):
    while True:
        s=input(f"Enter either 0 or 1 for element {i+1}:")
        if s=='0' or s=='1':
            ls.append(int(s))
            break
        else:
            print("Invalid input! You must enter either 0 or 1.")
print("The list of 0's and 1's is:",ls)
m=max_ones(ls)
print(f"The maximum number of consecutive 1's is: {m}")
