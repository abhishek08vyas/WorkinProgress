import java.util.ArrayList;

public class Login {

	public boolean checkadmin(String userId, String userPassword){
		if (userId.equals(null) ||userPassword.equals(null) || 
				!userId.equals("admin") || !userPassword.equals("admin")) {
			return false;
		}
		return true;
	}
	// Employee Login

	public Employee employeeLogin(String employeeUserName, String employeePassword, ArrayList<Employee>lstEmpInfo) {
		if (lstEmpInfo == null || lstEmpInfo.size() == 0) {
			System.out.println("\nEMPLOYEE USER LIST IS EMPTY.\nCONTACT ADMINISTRATOR TO CREATE NEW EMPLOYEE USER.\n");
			return null;
		}
		for (int i = 0; i < lstEmpInfo.size(); i++) {
			if (lstEmpInfo.get(i).getsUserid().equals(employeeUserName)
					&& lstEmpInfo.get(i).getsPassword().equals(employeePassword)) {
				Employee employee = new Employee();
				employee.setbIsLogin(true);
				employee.setEnUserType(EnLoginUserType.Employee);
				employee.setsUserid(employeeUserName);
				employee.SetLeave(lstEmpInfo.get(i).GetLeave());
				return employee;
			} 
		}
		return null;
	}

	// RA Login
	public ReportingAuthority RALogin(String raUserName, String raPassword, ArrayList<ReportingAuthority>lstRAInfo) {
		if (lstRAInfo == null || lstRAInfo.size() == 0) {
			System.out.println("\nRA USER LIST IS EMPTY.\nCONTACT ADMINISTRATOR TO CREATE NEW REPORTING AUTHORITY USER.\n");
			return null;
		}
		for (int i = 0; i < lstRAInfo.size(); i++) {
			if (lstRAInfo.get(i).getsUserid().equals(raUserName) == true
					&& lstRAInfo.get(i).getsPassword().equals(raPassword) == true) {
				ReportingAuthority reportingAuthority = new ReportingAuthority();
				reportingAuthority.setbIsLogin(true);
				reportingAuthority.setEnUserType(EnLoginUserType.RA);
				reportingAuthority.setsUserid(raUserName);
				return reportingAuthority;
			} 
		}
		return null;
	}
}
