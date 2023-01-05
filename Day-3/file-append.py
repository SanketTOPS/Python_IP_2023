fl=open('hello.txt','a')

id=input("Enter ID:")
name=input("Enter Name:")
sub=input("Enter Subject:")

fl.write(f"ID:{id}\nName:{name}\nSubject:{sub}\n")