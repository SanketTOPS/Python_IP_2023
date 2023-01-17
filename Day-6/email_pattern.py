import re

#sanket2020@gmail.com
email=input("Enter an email:")
email_pattern='^[a-z0-9._]+[@]+[a-z]+[\.]+[a-z]{2,}$'

x=re.findall(email_pattern,email)

if x: #true
    print("Valid Email address!")
else:
    print("Error!Invalid Email Address")