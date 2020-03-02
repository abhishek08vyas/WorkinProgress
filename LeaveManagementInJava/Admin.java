
import java.util.ArrayList;

public class Admin {

	private boolean bIsLogin = false;
	private EnLoginUserType enUserType = EnLoginUserType.Admin;
	
	public boolean isbIsLogin() {
		return bIsLogin;
	}

	public void setbIsLogin(boolean bIsLogin) {
		this.bIsLogin = bIsLogin;
	}

	public Employee addNormalEmployee(String employeeUserName, String employeePassword, String reporting){
			enUserType = EnLoginUserType.Employee;
			Employee employee = new Employee();
			employee.setEnUserType(enUserType);
			employee.setsUserid(employeeUserName);
			employee.setsPassword(employeePassword);
			employee.SetRA(reporting);
			employee.SetLeave(10);
			return employee;
	}
	
	public ReportingAuthority addReportingAuthority(String employeeUserName, String employeePassword){
		enUserType = EnLoginUserType.RA;
		ReportingAuthority reportingAuthority = new ReportingAuthority();
		reportingAuthority.setEnUserType(enUserType);
		reportingAuthority.setsUserid(employeeUserName);
		reportingAuthority.setsPassword(employeePassword);
		return reportingAuthority;
}
	
	public ReportingAuthority checkReportingAuthority(String reporting, ArrayList<ReportingAuthority>lstRAInfo ) {
		
		if(reporting == null || lstRAInfo.isEmpty()) {
			return null;
		}
		for (int i = 0; i < lstRAInfo.size(); i++) {
			if (lstRAInfo.get(i).getsUserid() != null) {
				if (lstRAInfo.get(i).getsUserid().equals(reporting)) {
					return lstRAInfo.get(i);
				}
			}
		}
		return null;
	}


	public boolean IsUseridUnique(String sUserid, String sUserType, ArrayList<Employee>lstEmpInfo, ArrayList<ReportingAuthority>lstRAInfo) {
		if (sUserid == null) {
			return false;
		}

		if (sUserType.equals(EnLoginUserType.Employee.toString()) == true) {
			for (int i = 0; i < lstEmpInfo.size(); i++) {
				if (lstEmpInfo.get(i).getsUserid() != null) {
					if (lstEmpInfo.get(i).getsUserid().equals(sUserid) == true) {
						return false;
					}
				}
			}
		} else if (sUserType.equals(EnLoginUserType.RA.toString()) == true) {
			for (int i = 0; i < lstRAInfo.size(); i++) {
				if (lstRAInfo.get(i).getsUserid() != null) {
					if (lstRAInfo.get(i).getsUserid().equals(sUserid) == true) {
						return false;
					}
				}
			}
		}
		return true;
	} 

}
