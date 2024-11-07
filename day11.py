start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
for number in range(start,end+1):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(number)
        