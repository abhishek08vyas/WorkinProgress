from Employee import Employee
from ReportingAuthority import ReportingAuthority


class Admin:

    def __init__(self):
        self.bIsLogin = False
        self.enUserType = "Admin"

    def isbIsLogin(self):
        return self.bIsLogin

    def setbIsLogin(self, bIsLogin):
        self.bIsLogin = bIsLogin

    def addNormalEmployee(self, employeeUserName, employeePassword, reporting):
        enUserType = "Employee"
        employee = Employee()
        employee.setEnUserType(enUserType)
        employee.setsUserid(employeeUserName)
        employee.setsPassword(employeePassword)
        employee.SetRA(reporting)
        return employee

    def addReportingAuthority(self, employeeUserName, employeePassword):
        enUserType = "RA"
        reportingAuthority = ReportingAuthority()
        reportingAuthority.setEnUserType(enUserType)
        reportingAuthority.setsUserid(employeeUserName)
        reportingAuthority.setsPassword(employeePassword)
        return reportingAuthority

    def checkReportingAuthority(self, reporting, lstRAInfo):
        if len(reporting) == 0 or len(lstRAInfo) == 0:
            return None
        for reportingauthority in lstRAInfo:
            if len(reportingauthority.getsUserid()) != 0:
                if reportingauthority.getsUserid() == reporting:
                    return reportingauthority
        return None

    def IsUseridUnique(self, sUserid, sUserType, lstEmpInfo, lstRAInfo):
        if len(sUserid) == 0:
            return False
        if sUserType == "Employee":
            for employee in lstEmpInfo:
                if len(employee.getsUserid()) != 0:
                    if (employee.getsUserid() == sUserid):
                        return False
        elif sUserType == "RA":
            for reportingauthority in lstRAInfo:
                if len(reportingauthority.getsUserid()) != 0:
                    if reportingauthority.getsUserid() == sUserid:
                        return False
        return True
