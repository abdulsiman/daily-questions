word=input("Enter a word or sentence:") 
res='' 
for i in word: 
 if i not in 'abcdefghijklmnopqrstuvwxyz': 
  res=res+i 
 else: 
  j=ord(i) 
  k=j-32 
  res=res+chr(k) 
print(f"Your given sentence or word in capitalized form is:{res}")
      
    
    