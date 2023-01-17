import re

mystr=input("Enter any string:")

x=re.search('is',mystr)
print(x)

if x: #true
    print("Yes...is there")
else:
    print("Error!Try again")
