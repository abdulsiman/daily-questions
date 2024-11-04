string=input("enter ur word here:")
print(string)
vowels='AEIOUaeiou'
v=[]
c=[]
for i in range(len(string)):
    if string[i] in vowels:
        v.append(string[i])
    else:
        c.append(string[i])
print(f'vowels are {v}')
print(f"consonents are {c}")
print(f"number of vowels are {len(v)}")
print(f"number of consonents are {len(c)}")