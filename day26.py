word1=input("enter the first string:")
word2=input("enter the second string:")
word3=''.join(sorted(word1))
word4=''.join(sorted(word2))
if word3==word4:
    print("Its an anagram")
else:
    print('Its not an anagram')