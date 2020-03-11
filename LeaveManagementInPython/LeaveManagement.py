from Login import Login
from Admin import Admin
from ReportingAuthority import ReportingAuthority
from Employee import Employee


if __name__ == '__main__':
    lstEmpInfo = []
    lstRAInfo = []
    login = Login()

    print("\n------------------------------------------------------")
    print("\t\t\tLOGIN")
    print("------------------------------------------------------")

    bIsValidChoice = True
    while (bIsValidChoice):
        print("\n1. ADMIN")
        print("2. REPORTING AUTHORITY")
        print("3. EMPLOYEE\n")
        sLoginChoice = int(input("LOGIN AS : "))
        if (sLoginChoice == 1):
            adminLgn = Admin()
            adminchoice = True
            checklogin = True
            while (checklogin):
                sUserId = input("\nADMIN USERNAME : ")
                sPassword = input("ADMIN PASSWORD : ")
                if(len(sUserId)==0 or len(sPassword)==0):
                    print("\n------------ VALUES CANNOT BE NULL --------------")
                    checklogin = True
                if login.checkAdmin(sUserId,sPassword):
                    checklogin = False
                #print("------------ INVALID CREDENIALS --------------")
            while (adminchoice):
                print("\n------------------------------------------------------")
                print("\t\t\tADMIN")
                print("------------------------------------------------------")

                print("\n1. ADD NORMAL EMPLOYEE")
                print("2. ADD REPORTING AUTHORITY")
                print("3. LOGOUT\n")
                sChoice = int(input("OPT FOR : "))
                # ADD NORMAL EMPLOYEE
                if (sChoice == 1):
                    firstchoice = True
                    employeeUserName = ''
                    employeePassword = ''
                    reporting = ''
                    while (firstchoice):
                        firstchoice = True
                        employeeUserName = input("\nNORMAL EMPLOYEE USERNAME : ")
                        employeePassword = input("NORMAL EMPLOYEE PASSWORD : ")
                        reporting = input("REPORTING AUTHORITY : ")
                        if (len(employeeUserName) == 0 or len(employeePassword) == 0 or len(reporting) == 0):
                            firstchoice = True
                            print("\n------------ VALUES CANNOT BE NULL --------------")
                        else:
                            firstchoice = False
                    if (adminLgn.IsUseridUnique(employeeUserName, "EMPLOYEE", lstEmpInfo, lstRAInfo)):
                        reporter = adminLgn.checkReportingAuthority(reporting, lstRAInfo)
                        r = ''
                        if (reporter == None):
                            print("\n------------ ADD REPORTING AUTHORITY FIRST --------------")
                            secondchoice = True
                            tempPassword = ''
                            while (secondchoice):
                                secondchoice = True
                                print("\nREPORTING AUTHORITY USERNAME : " + reporting)
                                tempPassword = input("REPORTING AUTHORITY PASSWORD : ")
                                if (len(reporting) == 0 or len(tempPassword) == 0):
                                    secondchoice = True
                                    print("\n------------ VALUES CANNOT BE NULL --------------")
                                else:
                                    secondchoice = False
                            if (adminLgn.IsUseridUnique(reporting, "RA", lstEmpInfo, lstRAInfo)):
                                reporter = adminLgn.addReportingAuthority(reporting, tempPassword)
                                if (reporter != None):
                                    print("\n------------ REPORTING AUTHORITY IS ADDED SUCCESSFULLY --------------")
                                    lstRAInfo.append(reporter)
#                                 else :
#                                     print("\n------------ REPORTING AUTHORITY ADDING UNSUCCESSFULLY --------------")
                            else:
                                print("\n------------ USER ALREADY EXISTED --------------")

                        employee = adminLgn.addNormalEmployee(employeeUserName, employeePassword, reporter.getsUserid())
                        if (employee != None):
                            print("\n------------ USER IS ADDED SUCCESSFULLY --------------")
                            lstEmpInfo.append(employee)
#                         else:
#                             print("\n------------ USER ADDING UNSUCCESSFULLY --------------")
                    else:
                        print("\n------------ USER ALREADY EXISTED --------------")

                #Add Reporting Authority
                elif (sChoice == 2):
                    secondchoice = True
                    while (secondchoice):
                        secondchoice = True
                        employeeUserName = input("\nREPORTING AUTHORITY USERNAME : ")
                        employeePassword = input("REPORTING AUTHORITY PASSWORD : ")
                        if (len(employeeUserName) == 0 or len(employeePassword) == 0):
                            secondchoice = True
                            print("\n------------ VALUES CANNOT BE NULL --------------")
                        else:
                            secondchoice = False

                    if (adminLgn.IsUseridUnique(employeeUserName, "RA", lstEmpInfo, lstRAInfo)):
                        reportingAuthority = adminLgn.addReportingAuthority(employeeUserName, employeePassword)
                        if (reportingAuthority != None):
                            sUsers = input("\nENTER THE LIST OF EMPLOYEES\nNOTE : IF MORE THAN ONE EMPLOYEE , "
                                           "PLEASE SEPARATE IT USING COMMA.\n")
                            arrUsers = sUsers.split(",")
                            for empuser in arrUsers:
                                if (not adminLgn.IsUseridUnique(empuser, "Employee", lstEmpInfo, lstRAInfo)):
                                    print("HE/SHE CAN'T BE ASSIGNED TO YOU.\n %s IS ALREADY WORKING UNDER ANOTHER RA.\n", empuser)
                                    empuser = None
                                else:
                                    empPassword = ''
                                    firstchoice = True
                                    while (firstchoice):
                                        firstchoice = True
                                        print("\nNORMAL EMPLOYEE USERNAME : %s", empuser)
                                        empPassword = input("\nNORMAL EMPLOYEE PASSWORD : ")
                                        if (len(employeePassword) == 0):
                                            firstchoice = False
                                            print("\n------------ VALUES CANNOT BE NULL --------------")
                                        else:
                                            firstchoice = False
                                    if (adminLgn.IsUseridUnique(empuser, "Employee", lstEmpInfo, lstRAInfo)):
                                        emp = adminLgn.addNormalEmployee(empuser, empPassword, employeeUserName)
                                        lstEmpInfo.append(emp)
                                        print("\n------------ USER IS ADDED SUCCESSFULLY --------------")
                            lstRAInfo.append(reportingAuthority)
                            print("\n------------ REPORTING AUTHORITY IS ADDED SUCCESSFULLY --------------")

#                         else:
#                             print("------------ REPORTING AUTHORITY ADDING UNSUCCESSFULLY --------------")

                    else:
                        print("\n------------ USER ALREADY EXISTED --------------")

                #Logout
                elif (sChoice == 3):
                    adminLgn.setbIsLogin(False)
                    adminchoice = False
                    adminLgn = None
                    break
                else:
                    print("\n---------- THERE'S NO SUCH OPTION AVAILABLE ----------")
                    bIsValidChoice = True
            bIsValidChoice = True

        elif(sLoginChoice == 2):
            reportingAuthority = ReportingAuthority()
            rachoice = True
            ralogin = True
            raUserName = ''
            raPassword = ''
            while(ralogin):
                if(len(lstRAInfo) == 0):
                    print("\nRA USER LIST IS EMPTY.\nCONTACT ADMINISTRATOR TO CREATE NEW REPORTING AUTHORITY USER.\n")
                    rachoice = False
                    break
                raUserName = input("\nREPORTING AUTHORITY USERNAME : ")
                raPassword = input("REPORTING AUTHORITY PASSWORD : ")
                if (len(raUserName) == 0 or len(raPassword) == 0):
                    ralogin = True
                    print("\n------------ VALUES CANNOT BE NULL --------------")
                reportingAuthority = login.RALogin(raUserName, raPassword, lstRAInfo)
                if (reportingAuthority == None):
                    ralogin = True
                    print("\n------------ INVALID CREDENTIALS --------------")
                else:
                    ralogin = False
            while(rachoice):
                print("\n------------------------------------------------------")
                print("\t\tREPORTING AUTHORITY")
                print("------------------------------------------------------")
                print("\n1. SHOW REPORT")
                print("2. ACCEPT / REJECT LEAVE")
                print("3. LOGOUT\n")
                print("OPT FOR : ")
                sChoice = int(input())
                # Show Report of the Employees working under RA case
                if (sChoice == 1):
                    reportingAuthority.DisplayEmployeeReport(lstEmpInfo)
                    bIsValidChoice = True
                #Grant Leaves of RA case
                elif(sChoice == 2):
                    lstEmpInfo = reportingAuthority.EmployeeLeaveReqAcceptReject(lstEmpInfo)
                    bIsValidChoice = True
                #Logout of RA case
                elif(sChoice == 3):
                    bIsValidChoice = True
                    reportingAuthority.setbIsLogin(False)
                    reportingAuthority = None
                    rachoice = False
                else:
                    print("\n---------- THERE'S NO SUCH OPTION AVAILABLE ----------")
                    bIsValidChoice = True
        elif(sLoginChoice == 3):
            employee = Employee()
            employeechoice = True
            employeelogin = True
            employeeUserName = None
            employeePassword = None
            while(employeelogin):
                if len(lstEmpInfo) == 0:
                    print("\nEMPLOYEE USER LIST IS EMPTY.\nCONTACT ADMINISTRATOR TO CREATE NEW EMPLOYEE USER.\n")
                    employeechoice = False
                    break
                employeelogin = True
                employeeUserName = input("\nNORMAL EMPLOYEE USERNAME : ")
                employeePassword = input("NORMAL EMPLOYEE PASSWORD : ")
                if (len(employeeUserName) == 0 or len(employeePassword) == 0):
                    employeelogin = True
                    print("\n------------ VALUES CANNOT BE NULL --------------")
                employee = login.employeeLogin(employeeUserName, employeePassword, lstEmpInfo)
                if (employee == None):
                    employeelogin = True
                    print("\n------------ INVALID CREDENTIALS --------------")
                else:
                    employeelogin = False
            employee.setsUserid(employeeUserName)
            employee.setsPassword(employeePassword)
            while(employeechoice):
                print("\n------------------------------------------------------")
                print("\t\tREGULAR EMPLOYEE")
                print("------------------------------------------------------")
                print("\n1. SHOW REPORT")
                print("2. APPLY LEAVE")
                print("3. LOGOUT\n")
                print("OPT FOR : ")
                sChoice = int(input())
                #Show Leave report of Employee
                if (sChoice == 1):
                    employee.DisplayLeaveReport(lstEmpInfo)
                    bIsValidChoice = True
                # Apply Leave of Employee
                elif (sChoice == 2):
                    lstEmpInfo = employee.ApplyLeave(lstEmpInfo)
                    bIsValidChoice = True
                # Logout of Employee
                elif (sChoice == 3):
                    bIsValidChoice = True
                    employee.setbIsLogin(False)
                    employee = None
                    employeechoice = False
                else:
                    print("\n---------- THERE'S NO SUCH OPTION AVAILABLE ----------")
                    bIsValidChoice = True
        else:
            print("\n---------- THERE'S NO SUCH OPTION AVAILABLE ----------")
            bIsValidChoice = True