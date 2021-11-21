#the long method:
'''#creating the reverse word
def palindrome(str):
  bl=[]
  for char in str:
     bl.append(char)
  ty=""
  while len(bl)>0:
    a=bl.pop()
    ty=ty+a
  return ty


#checking if the word and the reveresed word are same/palindrome
a=str(input("enter the word:"))
b=palindrome(a)
#print(b)
if a == b:
    print("yes,the word is palindrome")
else:
    print("the word is not palindrome")

'''

#the short one:
a=str(input("enter the word:"))
b=a[::-1]
#print(b)
if a==b:
  print("the word is palindrome")
else:
  print("its not palindrome")

