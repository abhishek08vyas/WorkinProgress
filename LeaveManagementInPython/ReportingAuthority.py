import pandas as pd


class ReportingAuthority:

    def __init__(self):
        self.bIsLogin = False
        enUserType = "RA"
        sUserid = ""
        sPassword = ""

    def isbIsLogin(self):
        return self.bIsLogin

    def setbIsLogin(self, bIsLogin):
        self.bIsLogin = bIsLogin

    def getEnUserType(self):
        return self.enUserType

    def setEnUserType(self, enUserType):
        self.enUserType = enUserType

    def getsUserid(self):
        return self.sUserid

    def setsUserid(self, sUserid):
        self.sUserid = sUserid

    def getsPassword(self):
        return self.sPassword

    def setsPassword(self, sPassword):
        self.sPassword = sPassword

    # Employee leave request accept/reject
    def EmployeeLeaveReqAcceptReject(self, lstEmpInfo):
        if (len (lstEmpInfo) == 0):
            print ("--------------- EMPLOYEE LIST IS EMPTY ---------------")
            return lstEmpInfo
        # nCount = 0
        bApplyLeaveFlag = False
        leave = pd.DataFrame()
        for employee in lstEmpInfo:
            if (not employee.getleavedf().empty) and (employee.GetRA () == (self.getsUserid ())):
                l = employee.getleavedf()
                x = l.copy()
                x['username'] = employee.getsUserid()
                leave = leave.append(x)
        print(leave)
        empname = ''
        empleave = 0
        status = ""
        bIsValidSelectEmployee = True
        while (bIsValidSelectEmployee):
            bIsValidSelectEmployee = False
            print("\nENTER SELECT FROM THE ABOVE LIST : ")
            # Store user choice
            empname = input("ENTER username :")
            empleave = int(input ("ENTER LEAVE ID: "))
            temp = leave[(leave.username == empname) & (leave.Leaveid == empleave)]
            if (temp.empty):
                print ("------------ SELECTED INPUT NOT IN LIST --------------")
                bIsValidSelectEmployee = True
            else:
                print(temp)
                leavestatus = int (input ("ENTER 0 to reject leave / 1 to accept leave : "))
                if leavestatus == 1:
                    status = "Approved"
                    print("-------- LEAVE(S) IS/ARE APPROVED SUCCESSFULLY ---------")
                elif leavestatus == 0:
                    status = "Rejected"
                    print("-------- LEAVE(S) IS/ARE REJECTED SUCCESSFULLY ---------")
                else:
                    print("-------- ENTER PROPER INPUT ---------")
                    bIsValidSelectEmployee = True
        for employee in lstEmpInfo:
            if employee.getsUserid() == empname:
                leave = employee.getleavedf()
                leave.at[empleave,'Status'] = status
                print(leave)
                #print(temp)
                if status == "Rejected":
                    print("Reectedklkdsl;;",leave['AppliedLeave'].values[0])
                    addedleave = leave['AppliedLeave'].values[0]
                    type = leave['Leavetype'].values[0]
                    print ("addedleave;;", addedleave)
                    if addedleave > 0:
                        if type == "Sick":
                            employee.setsickleave(employee.getsickleave() + addedleave)
                        elif type == "Casual":
                            employee.setcasualleave(employee.getcasualleave() + addedleave)
                        else:
                            employee.setpriveleageleave(employee.getprivilegeleave() + addedleave)
        return lstEmpInfo

    # Display employee report
    def DisplayEmployeeReport(self, lstEmpInfo):
        leave = pd.DataFrame()
        for employee in lstEmpInfo:
            if (not employee.getleavedf().empty) and (employee.GetRA() == (self.getsUserid ())):
                l = employee.getleavedf()
                x = l.copy()
                x['username'] = employee.getsUserid()
                leave = leave.append(x)
        print(leave)
