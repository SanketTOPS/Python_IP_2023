class father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("Enter number of car:")
        self.bal=input("Enter bank balance detail:")

class son(father):
    def printdata(self):
        print("Car:",self.car)
        print("Balance:",self.bal)


sn=son()
sn.getdata()
sn.printdata()