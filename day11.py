start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
        