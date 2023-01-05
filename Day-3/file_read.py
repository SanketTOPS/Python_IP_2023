fl=open('hello.txt','r')

#print(fl.read())
#print(fl.readline())
#print(fl.readlines())

#print(fl.readlines()[4])
n=1
for i in fl:
    #print(i)
    print(f"Line:[{n}] = {i}")
    n+=1

