n=int(input("Enter a number:"))
square=n**2
s1=str(n)
s2=str(square)
if s2.endswith(s1):
    print(f"{n} is automorphic")
else:
    print(f"{n} is not automorphic")
