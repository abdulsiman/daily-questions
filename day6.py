n=int(input("Enter n digit number"))
org = n
rev=0
while n!=0:
    remainder=n%10
    rev=(rev*10)+remainder
    n=n//10
if org == rev:
    print(f"{org} is a palindrome.")
else:
    print(f"{org} is not a palindrome.")