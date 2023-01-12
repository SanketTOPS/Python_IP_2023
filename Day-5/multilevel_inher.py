class grandfather:
    gold=0
    house=0

    def g_getdata(self):
        self.gold=input("Enter gold details:")
        self.house=input("Enter house details:")

class father(grandfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter car details:")
        self.bal=input("Enter bank balance details:")

class son(father):
    sid=0
    sub=''

    def s_getdata(self):
        self.sid=input("Enter Son ID:")
        self.sub=input("Enter Son Subject:")

    def printdata(self):
        print("Gold:",self.gold)
        print("House:",self.house)
        print("Car:",self.car)
        print("Bank Balance:",self.bal)
        print("Son's ID:",self.sid)
        print("Son's Subject:",self.sub)

sn=son()
sn.g_getdata()
sn.f_getdata()
sn.s_getdata()
sn.printdata()



