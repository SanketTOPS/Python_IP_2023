import re

mystr=input("Enter any string:")

#x=re.findall('[A-Z]',mystr)
#x=re.findall('[a-z]',mystr)
#x=re.findall('[A-Za-z]',mystr)
#x=re.findall('[0-9]',mystr)
#x=re.findall('[A-Za-z0-9]',mystr)

#x=re.findall('^This',mystr)
#x=re.findall('!$',mystr)

#x=re.findall('[^A-Z]',mystr)
#x=re.findall('^[A-Z]',mystr)

#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\s',mystr)
x=re.findall('\S',mystr)

print(x)