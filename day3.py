n=float(input("Enter your marks out of 100:"))

if 90<n<=100:
    print("You got AA grade..")
elif 80<n<=90:
    print("You got AB grade..")
elif 70<n<=80:
    print("You got BB grade..")
elif 60<n<=70:
    print("You got BC grade..")
elif 50<n<=60:
    print("You got CD grade..")
elif 40<n<=50:
    print("You got DD grade..")
elif n<=40:
    print("You failed..")
else:
    print("You have entered your marks greater than 100.Enter marks between 1 to 100")
