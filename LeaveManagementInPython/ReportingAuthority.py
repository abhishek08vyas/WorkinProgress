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
        StoreIndex = []
        i = 0
        leave = pd.DataFrame ()
        temp = pd.DataFrame ()
        for employee in lstEmpInfo:
            if (not employee.getleavedf ().empty) and (employee.GetRA () == (self.getsUserid ())):
                l = employee.getleavedf ()
                leave = l.copy ()
                leave['username'] = employee.getsUserid ()
                print (leave)
        empname = ''
        empleave = 0
        bIsValidSelectEmployee = True
        while (bIsValidSelectEmployee):
            bIsValidSelectEmployee = False
            print ("\nENTER SELECT FROM THE ABOVE LIST : ")
            # Store user choice
            empname = input ("ENTER username :")
            empleave = int (input ("ENTER LEAVE ID: "))
            temp = leave.loc[(leave['username'] == empname) & (empleave == leave['Leaveid'])]
            if (temp.empty):
                print ("------------ SELECTED INPUT NOT IN LIST --------------")
                bIsValidSelectEmployee = True
        bIsValidSelectEmployee = True
        while (bIsValidSelectEmployee):
            bIsValidSelectEmployee = False
            nAcceptLeave = int (input ("ENTER NO. OF ACCEPTED LEAVES : "))
            nApplyLeave = temp['AppliedLeave'].item ()
            print (temp['AppliedLeave'].item ())
            if temp['AppliedLeave'].item () < nAcceptLeave:
                print ("\n------------------------------------------------------")
                print ("YOU CANNOT ACCEPT MORE THAN ", nApplyLeave, " LEAVE(S).")
                print ("------------------------------------------------------\n")
                bIsValidSelectEmployee = True
            elif (nAcceptLeave <= 0):
                print ("\n------------------------------------------------------")
                print ("ACCEPTED LEAVE(S) SHOULD BE POSITIVE AND GREATER THAN 0.")
                print ("------------------------------------------------------\n")
                bIsValidSelectEmployee = True
            else:
                rejectedleaves = temp['AppliedLeave'].item () - nAcceptLeave
                if (rejectedleaves > 0):
                    print ("ACCEPTED LEAVE(S) ARE : ", nAcceptLeave, " out of ", temp['AppliedLeave'].item ())
                    temp.loc[temp['Leaveid'], 'Status'] = "Some Rejected"
                    temp.loc[temp['Leaveid'], 'AcceptedLeave'] = nAcceptLeave
                    temp.loc[temp['Leaveid'], 'RejectedLeave'] = rejectedleaves
                    print (temp)
                else:
                    print ("-------- LEAVE(S) IS/ARE ACCEPTED SUCCESSFULLY ---------")
                    temp.loc[temp['Leaveid'], 'Status'] = "Approved"
                    temp.loc[temp['Leaveid'], 'AcceptedLeave'] = nAcceptLeave
                    temp.loc[temp['Leaveid'], 'RejectedLeave'] = rejectedleaves
                    print (temp)
                bIsValidSelectEmployee = False
        for employee in lstEmpInfo:
            if (employee.getsUserid () == temp['username'].item ()):
                leave = employee.getleavedf ()
                if (leave['Leaveid'] == temp['Leaveid'] and leave['Leavetype'] == temp['Leavetype']):
                    leave['Status'] = temp['Status']
                    leave['AcceptedLeave'] = temp['AcceptedLeave']
                    leave['RejectedLeave'] = temp['RejectedLeave']
                    addedleave = leave['RejectedLeave'].values.item ()
                    print (leave['RejectedLeave'].item ())
                    print (leave['RejectedLeave'].values.item ())
                    if (addedleave > 0):
                        if (leave['Leavetype'] == "Sick"):
                            employee.setsickleave (employee.getsickleave () + addedleave)
                        elif (leave['Leavetype'] == "Casual"):
                            employee.setcasualleave (employee.getcasualleave () + addedleave)
                        else:
                            employee.setpriveleageleave (employee.getprivilegeleave () + addedleave)
                print (employee.getleavedf ())
        return lstEmpInfo

    # Display employee report
    def DisplayEmployeeReport(self, lstEmpInfo):
        for employee in lstEmpInfo:
            if (not employee.getleavedf ().empty) and (employee.GetRA () == (self.getsUserid ())):
                l = employee.getleavedf ()
                leave = l.copy ()
                leave['username'] = employee.getsUserid ()
                print (leave)
