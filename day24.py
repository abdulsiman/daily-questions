str=input("Enter a sentence:")
words=str.split()
longest=""
for word in words:
    if len(word)>len(longest):
        longest=word
print(f"The longest word in the given sentence is: {longest}")
