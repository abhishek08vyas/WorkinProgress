from Employee import Employee
from ReportingAuthority import ReportingAuthority


class Login:

    def __init__(self):
        pass

    def checkAdmin(self, userId, userPassword):
        if userId == "admin" and userPassword == "admin":
            print("LOGGED IN SUCCESSFULLY!")
            return True
        else:
            print("INVALID CREDENTIALS")
            return False

    def RALogin(self, raUserName, raPassword, lstRAInfo):
#         if len(lstRAInfo) == 0:
#             print("\nRA USER LIST IS EMPTY.\nCONTACT ADMINISTRATOR TO CREATE NEW REPORTING AUTHORITY USER.\n")
#             return None
        for reportingauthority in lstRAInfo:
            if reportingauthority.getsUserid() == raUserName and reportingauthority.getsPassword() == raPassword:
                reportingAuthority = ReportingAuthority()
                reportingAuthority.setbIsLogin(True)
                reportingAuthority.setEnUserType("RA")
                reportingAuthority.setsUserid(raUserName)
                return reportingAuthority
        return None

    def employeeLogin(self, employeeUserName, employeePassword, lstEmpInfo):
#         if len(lstEmpInfo) == 0:
#             print("\nEMPLOYEE USER LIST IS EMPTY.\nCONTACT ADMINISTRATOR TO CREATE NEW EMPLOYEE USER.\n")
#             return None

        for employeetemp in lstEmpInfo:
            if employeetemp.getsUserid() == employeeUserName and employeetemp.getsPassword() == employeePassword:
                employee = Employee()
                employee.setbIsLogin(True)
                employee.setEnUserType("Employee")
                employee.setsUserid(employeeUserName)
                return employee
        return None