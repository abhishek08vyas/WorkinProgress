
import java.util.ArrayList;
import java.util.Scanner;

public class LeaveManagement {
	public static void main(String[] args) {
		ArrayList<Employee> lstEmpInfo = new ArrayList<Employee>();
		ArrayList<ReportingAuthority> lstRAInfo = new ArrayList<ReportingAuthority>();
		Login login = new Login();

		System.out.println("------------------------------------------------------");
		System.out.println("\t\t\tLOGIN");
		System.out.println("------------------------------------------------------");

		boolean bIsValidChoice = false;
		do {
			System.out.println("\n1. " + "ADMIN");
			System.out.println("2. " + "REPORTING AUTHORITY");
			System.out.println("3. " + "EMPLOYEE\n");
			Scanner sUserInput = new Scanner(System.in);
			System.out.print("LOGIN AS : ");
			String sLoginChoice = sUserInput.nextLine();
			System.out.print("\n");
			if (sLoginChoice == null || sLoginChoice.length() == 0) {
				System.out.println("------------ CHOICE SHOULD NOT BE EMPTY --------------");
				bIsValidChoice = false;
				continue;
			}
			switch (sLoginChoice) {
			case "1":
				Admin adminLgn = new Admin();
				boolean adminchoice = true;
				boolean checklogin = false;
				Scanner adminScanner = new Scanner(System.in);
				String sUserId = null;
				String sPassword = null;
				do {
					checklogin = false;
					System.out.print("\nADMIN USERNAME : ");
					sUserId = adminScanner.nextLine();
					System.out.print("ADMIN PASSWORD : ");
					sPassword = adminScanner.nextLine();
					if(sUserId.length() ==0 || sPassword.length()==0) {
						checklogin = true;
						System.out.println("------------ VALUES CANNOT BE NULL --------------");
					}
					if(!login.checkadmin(sUserId, sPassword)){
						checklogin = true;
						System.out.println("------------ INVALID CREDENIALS --------------");
					}
				}while(checklogin);
				do {
					System.out.println("------------------------------------------------------");
					System.out.println("\t\t\tADMIN");
					System.out.println("------------------------------------------------------");

					System.out.println("\n1. " + "ADD NORMAL EMPLOYEE");
					System.out.println("2. " + "ADD REPORTING AUTHORITY");
					System.out.println("3. " + "LOGOUT\n");
					System.out.print("OPT FOR : ");
					String sChoice = sUserInput.nextLine();
					if (sChoice == null || sChoice.length() == 0) {
						System.out.println("------------ CHOICE SHOULD NOT BE EMPTY --------------");
						bIsValidChoice = false;
						//continue;
					}
					switch (sChoice) {
					case "1":
						boolean firstchoice = false;
						String employeeUserName = null;
						String employeePassword = null;
						String reporting = null;
						do {
							firstchoice = false;
							System.out.print("\nNORMAL EMPLOYEE USERNAME : ");
							employeeUserName = adminScanner.nextLine();
							System.out.print("NORMAL EMPLOYEE PASSWORD : ");
							employeePassword = adminScanner.nextLine();
							System.out.print("REPORTING AUTHORITY : ");
							reporting = adminScanner.nextLine();
							if(employeeUserName.length() ==0 || employeePassword.length()==0) {
								firstchoice = true;
								System.out.println("------------ VALUES CANNOT BE NULL --------------");
							}
						}while(firstchoice);
						if(adminLgn.IsUseridUnique(employeeUserName, EnLoginUserType.Employee.toString(), lstEmpInfo, lstRAInfo)) {
							ReportingAuthority reporter = adminLgn.checkReportingAuthority(reporting, lstRAInfo);
							String r = null;
							if(reporter == null) {
								System.out.println("------------ ADD REPORTING AUTHORITY FIRST --------------");
								boolean secondchoice = false;
								String tempPassword = null;
								do {
									secondchoice = false;
									System.out.print("\nReporting Authority USERNAME : " + reporting);
									System.out.print("\nReporting Authority PASSWORD : ");
									tempPassword = adminScanner.nextLine();
									if(reporting.length() ==0 || tempPassword.length()==0) {
										secondchoice = true;
										System.out.println("------------ VALUES CANNOT BE NULL --------------");
									}
								}while(secondchoice);
								if(adminLgn.IsUseridUnique(reporting,EnLoginUserType.RA.toString(), lstEmpInfo, lstRAInfo)) {
									reporter = adminLgn.addReportingAuthority(reporting,tempPassword);
									if (reporter != null) {
										System.out.println("------------ Reporting Authority IS ADDED SUCCESSFULLY --------------");
										lstRAInfo.add(reporter);
										//continue;
									}
									else {
										System.out.println("------------ Reporting Authority ADDING UNSUCCESSFULLY --------------");
									}	
								}
								else {
									System.out.println("------------ USER ALREADY EXISED --------------");
								}
							}
							Employee employee = adminLgn.addNormalEmployee(employeeUserName,employeePassword,reporter.getsUserid());
							if (employee != null) {
								System.out.println("------------ USER IS ADDED SUCCESSFULLY --------------");
								lstEmpInfo.add(employee);
								//continue;
							}
							else {
								System.out.println("------------ USER ADDING UNSUCCESSFULLY --------------");
							}	
						}
						else {
							System.out.println("------------ USER ALREADY EXISED --------------");
						}
						break;
					case "2":
						boolean secondchoice = false;
						do {
							secondchoice = false;
							System.out.print("\nReporting Authority USERNAME : ");
							employeeUserName = adminScanner.nextLine();
							System.out.print("Reporting Authority PASSWORD : ");
							employeePassword = adminScanner.nextLine();
							System.out.println("\nUsername: " + employeeUserName);
							System.out.println("\nassword: " + employeePassword);
							if(employeeUserName.length() ==0 || employeePassword.length()==0) {
								firstchoice = true;
								System.out.println("------------ VALUES CANNOT BE NULL --------------");
							}
						}while(secondchoice);
						if(adminLgn.IsUseridUnique(employeeUserName,EnLoginUserType.RA.toString(), lstEmpInfo, lstRAInfo)) {
							ReportingAuthority reportingAuthority = adminLgn.addReportingAuthority(employeeUserName,employeePassword);
							if (reportingAuthority != null) {
								System.out.println("\nENTER THE LIST OF EMPLOYEES WORKING UNDER " + employeeUserName
										+ "\nNOTE : IF MORE THAN ONE EMPLOYEE , PLEASE SEPARATE IT USING COMMA.\n");
								String sUsers = adminScanner.nextLine();
								String[] arrUsers = sUsers.split(",");

								for (int i = 0; i < arrUsers.length; i++) {
									if (!adminLgn.IsUseridUnique(arrUsers[i], EnLoginUserType.Employee.toString(),lstEmpInfo, lstRAInfo)) {
										System.out.println("HE/SHE CAN'T BE ASSIGNED TO YOU.\n" + arrUsers[i] + " IS ALREADY WORKING UNDER ANOTHER RA.\n");
										arrUsers[i] = null;
									}
									else {
										String empPassword = null;
										do {
											firstchoice = false;
											System.out.print("\nNORMAL EMPLOYEE USERNAME : " + arrUsers[i]);
											System.out.print("NORMAL EMPLOYEE PASSWORD : ");
											empPassword = adminScanner.nextLine();
											if(employeeUserName.length() ==0 || employeePassword.length()==0) {
												firstchoice = true;
												System.out.println("------------ VALUES CANNOT BE NULL --------------");
											}
										}while(firstchoice);
										if(adminLgn.IsUseridUnique(employeeUserName, EnLoginUserType.Employee.toString(), lstEmpInfo, lstRAInfo)) {
											Employee emp = adminLgn.addNormalEmployee(arrUsers[i], empPassword, employeeUserName);
											lstEmpInfo.add(emp);
											System.out.println("------------ USER IS ADDED SUCCESSFULLY --------------");
										}
									}
								}

								System.out.println("------------ Reporting Authority IS ADDED SUCCESSFULLY --------------");
								lstRAInfo.add(reportingAuthority);
								//continue;
							}
							else {
								System.out.println("------------ Reporting Authority ADDING UNSUCCESSFULLY --------------");
							}	
						}
						else {
							System.out.println("------------ USER ALREADY EXISED --------------");
						}
						break;
					case "3":
						//adminLgn.setbIsLogin(false);
						adminchoice = false;
						adminLgn = null;
						break;
					default:
						System.out.println("---------- THERE'S NO SUCH OPTION AVAILABLE ----------");
						bIsValidChoice = false;
						//                                            continue;
					}

				}while(adminchoice);
				bIsValidChoice = false;
				break;
			case "2":
				ReportingAuthority reportingAuthority = new ReportingAuthority();
				boolean rachoice = true;
				boolean ralogin = false;
				Scanner raScanner = new Scanner(System.in);
				String raUserName = null;
				String raPassword = null;
				do {
					ralogin = false;
					System.out.print("\nREPORTING AUTHORITY USERNAME : ");
					raUserName = raScanner.nextLine();
					System.out.print("REPORTING AUTHORITY PASSWORD : ");
					raPassword = raScanner.nextLine();
					if(raUserName.length() ==0 || raPassword.length()==0) {
						ralogin = true;
						System.out.println("------------ VALUES CANNOT BE NULL --------------");
					}
					reportingAuthority = login.RALogin(raUserName, raPassword, lstRAInfo);
					if(reportingAuthority == null){
						ralogin = true;
						System.out.println("------------ INVALID CREDENIALS --------------");
					}
				}while(ralogin);

				do {
					System.out.println("------------------------------------------------------");
					System.out.println("\t\tREPORTING AUTHORITY");
					System.out.println("------------------------------------------------------");
					System.out.println("\n1. " + "SHOW REPORT");
					System.out.println("2. " + "ACCEPT / REJECT LEAVE");
					System.out.println("3. " + "LOGOUT\n");
					System.out.print("OPT FOR : ");
					String sChoice = raScanner.nextLine(); 
					if (sChoice == null || sChoice.length() == 0) {
						System.out.println("------------ CHOICE SHOULD NOT BE EMPTY --------------");
						bIsValidChoice = false;
						//continue;
					}
					switch (sChoice) {
					case "1":
						System.out.println("Employee Password:"+reportingAuthority.getsUserid());
						reportingAuthority.DisplayEmployeeReport(lstEmpInfo);
						bIsValidChoice = false;
						break;
					case "2":
						lstEmpInfo = reportingAuthority.EmployeeLeaveReqAcceptReject(lstEmpInfo);
						bIsValidChoice = false;
						break;
					case "3":
						bIsValidChoice = false;
						reportingAuthority.setbIsLogin(false);
						reportingAuthority = null;
						rachoice = false;
						break;
						//return;
					default:
						System.out.println("---------- THERE'S NO SUCH OPTION AVAILABLE ----------");
						bIsValidChoice = false;
						rachoice = false;
						//continue;
					}
				}while(rachoice);
				bIsValidChoice = false;
				break;

			case "3":

				Employee employee = new Employee();
				boolean employeechoice = true;
				boolean employeelogin = false;
				Scanner employeeScanner = new Scanner(System.in);
				String employeeUserName = null;
				String employeePassword = null;
				do {
					employeelogin = false;
					System.out.print("\nNORMAL EMPLOYEE USERNAME : ");
					employeeUserName = employeeScanner.nextLine();
					System.out.print("NORMAL EMPLOYEE PASSWORD : ");
					employeePassword = employeeScanner.nextLine();
					if(employeeUserName.length() ==0 || employeePassword.length()==0) {
						employeelogin = true;
						System.out.println("------------ VALUES CANNOT BE NULL --------------");
					}
					employee=  login.employeeLogin(employeeUserName, employeePassword, lstEmpInfo);
					if(employee == null){
						employeelogin = true;
						System.out.println("------------ INVALID CREDENIALS --------------");
					}					
				}while(employeelogin);

				do {
					System.out.println("\n1. " + "SHOW REPORT");
					System.out.println("2. " + "APPLY LEAVE");
					System.out.println("3. " + "LOGOUT\n");
					System.out.print("OPT FOR : ");

					//Scanner sUserInput = new Scanner(System.in);
					// Store user choice
					String sChoice = sUserInput.nextLine();
					if (sChoice == null || sChoice.length() == 0) {
						System.out.println("------------ CHOICE SHOULD NOT BE EMPTY --------------");
						bIsValidChoice = false;
						continue;
					}

					switch (sChoice) {
					case "1":
						employee.DisplayLeaveReport(lstEmpInfo);
						bIsValidChoice = false;
						break;
					case "2":
						lstEmpInfo = employee.ApplyLeave(lstEmpInfo);
						bIsValidChoice = false;
						break;
					case "3":
						bIsValidChoice = false;
						employee.setbIsLogin(false);
						employee = null;
						employeechoice = false;
						//return;
					default:
						System.out.println("---------- THERE'S NO SUCH OPTION AVAILABLE ----------");
						bIsValidChoice = false;
						continue;
					}
				}while(employeechoice);
				bIsValidChoice = false;
				break;
			default:
				System.out.println("---------- THERE'S NO SUCH OPTION AVAILABLE ----------");
				bIsValidChoice = false;
				continue;
			}

		}while(bIsValidChoice != true);
	}
}
