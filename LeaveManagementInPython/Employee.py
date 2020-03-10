import pandas as pd
class Employee:

    def __init__(self):
        self.leaveid = 0
        self.bIsLogin = False
        self.enUserType = "Employee"
        self.sUserid = ""
        self.sPassword = ""
        self.RA = ""
        self.casualleave = 10
        self.sickleave = 10
        self.priveleageleave = 10
        self.leavedf = pd.DataFrame(columns=['Leaveid', 'Leavetype', 'AppliedLeave', 'Status'])

    def isbIsLogin(self):
        return self.bIsLogin

    def setbIsLogin(self, bIsLogin):
        self.bIsLogin = bIsLogin

    def getsUserid(self):
        return self.sUserid

    def setsUserid(self, sUserid):
        self.sUserid = sUserid

    def getsPassword(self):
        return self.sPassword

    def setsPassword(self, sPassword):
        self.sPassword = sPassword
    def getEnUserType(self):
        return self.enUserType

    def setEnUserType(self, enUserType):
        self.enUserType = enUserType

    # Set RA
    def SetRA(self, sRAUnder):
        self.UnderRA = sRAUnder

    # Get RA
    def GetRA(self):
        return self.UnderRA

    def setcasualleave(self, casualleave):
        self.casualleave = casualleave

    def setsickleave(self, sickleave):
        self.sickleave = sickleave

    def setpriveleageleave(self, priveleageleave):
        self.priveleageleave = priveleageleave

    def getprivilegeleave(self):
        return self.priveleageleave

    def getcasualleave(self):
        return self.casualleave

    def getsickleave(self):
        return self.sickleave

    def getleaveid(self):
        return self.leaveid

    def setleaveid(self, leaveid):
        self.leaveid = leaveid

    def setleavedf(self,leavedf):
        self.leavedf = leavedf

    def getleavedf(self):
        return self.leavedf

    # Apply leave for employee
    def ApplyLeave(self, lstEmpInfo):
        for employeetemp in lstEmpInfo:
            print("for here")
            print(employeetemp.getsUserid())
            if (employeetemp.getsUserid() == (self.getsUserid())):
                print("here")
                leavebool= True
                while(leavebool):
                    leavebool = False
                    print("\n1. SICK")
                    print("2. privilege")
                    print("3. CAUSUAL\n")
                    leave = int(input ("OPT FOR : "))
                    if(leave==1):
                        print("IN SICK LEAVE")
                        print("TOTAL REMAINING SICK LEAVE(S) : ", employeetemp.getsickleave())
                        print("NO. OF SICK LEAVE(S) YOU WANT : ")
                        # Store user choice
                        bIsValidInput = True
                        while (bIsValidInput):
                            bIsValidInput = False
                            nLeaveApply = int(input())
                            if employeetemp.getsickleave() == 0:
                                print("\n------------------------------------------------------")
                                print("YOU CAN'T APPLY FOR MORE SICK LEAVE(S).\nYOU HAVE 0 SICK LEAVES LEFT.")
                                print("------------------------------------------------------\n")
                                bIsValidInput = False
                            if nLeaveApply < 0:
                                print("\n------------------------------------------------------")
                                print("APPLIED LEAVE(S) SHOULD BE POSITIVE.")
                                print("------------------------------------------------------\n")
                                bIsValidInput = True
                            if nLeaveApply == 0:
                                print("\n------------------------------------------------------")
                                print("APPLIED LEAVE(S) SHOULD BE MORE THAN 0.")
                                print("------------------------------------------------------\n")
                                bIsValidInput = True
                            if employeetemp.getsickleave() < nLeaveApply:
                                print("\n------------------------------------------------------")
                                print("YOU CAN'T APPLY FOR MORE THAN ", employeetemp.getsickleave(), " LEAVE(S).")
                                print("------------------------------------------------------\n")
                                bIsValidInput = True
                        employeetemp.setleaveid(employeetemp.getleaveid()+1)
                        employeetemp.setsickleave(employeetemp.getsickleave() - nLeaveApply)
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'Leaveid'] = employeetemp.getleaveid()
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'Leavetype'] = "Sick"
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'AppliedLeave'] = nLeaveApply
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'Status'] = "Pending"
                        print("----------------- SUCCESSFULLY APPLIED ---------------")
                    elif leave == 2:
                        print("IN privilege LEAVE")
                        print("TOTAL REMAINING privilege LEAVE(S) : ", employeetemp.getprivilegeleave())
                        # Store user choice
                        bIsValidInput = True
                        while (bIsValidInput):
                            bIsValidInput = False
                            nLeaveApply = int(input("NO. OF PRIVILEGE LEAVE(S) YOU WANT : "))
                            if employeetemp.getprivilegeleave() == 0:
                                print("\n------------------------------------------------------")
                                print("YOU CAN'T APPLY FOR MORE LEAVE(S).\nYOU HAVE 0 LEAVES LEFT.")
                                print("------------------------------------------------------\n")
                                bIsValidInput = False
                            if nLeaveApply < 0:
                                print("\n------------------------------------------------------")
                                print("APPLIED LEAVE(S) SHOULD BE POSITIVE.")
                                print("------------------------------------------------------\n")
                                bIsValidInput = True
                            if nLeaveApply == 0:
                                print("\n------------------------------------------------------")
                                print("APPLIED LEAVE(S) SHOULD BE MORE THAN 0.")
                                print("------------------------------------------------------\n")
                                bIsValidInput = True
                            if employeetemp.getprivilegeleave() < nLeaveApply:
                                print("\n------------------------------------------------------")
                                print("YOU CAN'T APPLY FOR MORE THAN ", employeetemp.getprivilegeleave(), " LEAVE(S).")
                                print("------------------------------------------------------\n")
                                bIsValidInput = True
                        employeetemp.setleaveid(employeetemp.getleaveid() + 1)
                        employeetemp.setpriveleageleave(employeetemp.getprivilegeleave() - nLeaveApply)
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'Leaveid'] = employeetemp.getleaveid()
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'Leavetype'] = "Privilege"
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'AppliedLeave'] = nLeaveApply
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'Status'] = "Pending"
                        print("----------------- SUCCESSFULLY APPLIED ---------------")
                    elif leave == 3:
                        print("IN CAUSAl LEAVE")
                        print("TOTAL REMAINING LEAVE(S) : ", employeetemp.getcasualleave())
                        print()
                        # Store user choice
                        bIsValidInput = True
                        while bIsValidInput:
                            bIsValidInput = False
                            nLeaveApply = int(input("NO. OF SICK LEAVE(S) YOU WANT : "))
                            if employeetemp.getcasualleave() == 0:
                                print("\n------------------------------------------------------")
                                print("YOU CAN'T APPLY FOR MORE LEAVE(S).\nYOU HAVE 0 LEAVES LEFT.")
                                print("------------------------------------------------------\n")
                                bIsValidInput = False
                            if nLeaveApply < 0:
                                print("\n------------------------------------------------------")
                                print("APPLIED LEAVE(S) SHOULD BE POSITIVE.")
                                print("------------------------------------------------------\n")
                                bIsValidInput = True
                            if nLeaveApply == 0:
                                print("\n------------------------------------------------------")
                                print("APPLIED LEAVE(S) SHOULD BE MORE THAN 0.")
                                print("------------------------------------------------------\n")
                                bIsValidInput = True
                            if employeetemp.getcasualleave() < nLeaveApply:
                                print("\n------------------------------------------------------")
                                print("YOU CAN'T APPLY FOR MORE THAN ", employeetemp.getcasualleave(), " LEAVE(S).")
                                print("------------------------------------------------------\n")
                                bIsValidInput = True
                        employeetemp.setleaveid(employeetemp.getleaveid() + 1)
                        employeetemp.setcasualleave(employeetemp.getcasualleave() - nLeaveApply)
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'Leaveid'] = employeetemp.getleaveid()
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'Leavetype'] = "Casual"
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'AppliedLeave'] = nLeaveApply
                        employeetemp.leavedf.loc[employeetemp.getleaveid(), 'Status'] = "Pending"
                        print("----------------- SUCCESSFULLY APPLIED ---------------")
                    else:
                        print("\n---------- THERE'S NO SUCH OPTION AVAILABLE ----------")
                    bIsValidInput = True
        return lstEmpInfo

    # Display employee leave report
    def DisplayLeaveReport(self, lstEmpInfo):
        for employee in lstEmpInfo:
            if employee.getsUserid() == (self.getsUserid()):
                print("\n------------------------------------------------------")
                print("You got Casual Leaves: ", employee.getcasualleave())
                print("You got Sick Leaves: ", employee.getsickleave())
                print("You got Priveleage Leaves: ", employee.getprivilegeleave())
                print(employee.getleavedf())
                print("------------------------------------------------------")