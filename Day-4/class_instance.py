class student:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Object of class
"""st=student()
st.getdata()
st.stid=30
st.stnm='Nirav'
st.getdata()"""


#Instance of class
student().getdata()
student().stid=20
student().stnm='Ashok'
student().getdata()


