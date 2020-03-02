import java.util.ArrayList;
import java.util.Scanner;

public class ReportingAuthority {
	
	// Store login true or false
	private boolean bIsLogin = false;
	// Store user type
	private EnLoginUserType enUserType = EnLoginUserType.RA;
	// Store user id
	private String sUserid;
	// Store password
	private String sPassword;
	public ReportingAuthority() {
	}

	public boolean isbIsLogin() {
		return bIsLogin;
	}

	public void setbIsLogin(boolean bIsLogin) {
		this.bIsLogin = bIsLogin;
	}

	public EnLoginUserType getEnUserType() {
		return enUserType;
	}

	public void setEnUserType(EnLoginUserType enUserType) {
		this.enUserType = enUserType;
	}

	public String getsUserid() {
		return sUserid;
	}

	public void setsUserid(String sUserid) {
		this.sUserid = sUserid;
	}

	public String getsPassword() {
		return sPassword;
	}

	public void setsPassword(String sPassword) {
		this.sPassword = sPassword;
	}

	// Employee leave request accept/reject
	public ArrayList<Employee> EmployeeLeaveReqAcceptReject(ArrayList<Employee> lstEmpInfo) {
		if (lstEmpInfo == null || lstEmpInfo.size() == 0) {
			System.out.println("--------------- EMPLOYEE LIST IS EMPTY ---------------");
			return lstEmpInfo;
		}
		
		int nCount = 0;
		boolean bApplyLeaveFlag = false;
		ArrayList<Integer> StoreIndex = new ArrayList<Integer>();
		for (int i = 0; i < lstEmpInfo.size(); i++) {
			if (lstEmpInfo.get(i).GetApplyLeave() > 0 && (lstEmpInfo.get(i).GetRA().equals(this.getsUserid()) == true)
					&& lstEmpInfo.get(i).GetLeaveFlag() != false) {
				System.out.println("");
				System.out.println("------------------------------------------------------");
				nCount = nCount + 1;
				System.out.println("                  ID NO. : " + nCount);
				System.out.println("USERNAME OF THE EMPLOYEE : " + lstEmpInfo.get(i).getsUserid());
				System.out.println("NO. OF APPLIED LEAVE(S)  : " + lstEmpInfo.get(i).GetApplyLeave());
				System.out.println("------------------------------------------------------\n");
				StoreIndex.add(i);
				bApplyLeaveFlag = true;
			}
		}

		if (bApplyLeaveFlag == false) {
			System.out.println("------------ CURRENTLY THE LIST IS EMPTY -------------");
			return lstEmpInfo;
		}

		Scanner sUserInput = new Scanner(System.in);
		System.out.println("\nENTER ID FROM THE ABOVE LIST (INTEGER VALUE ACCEPTABLE) : ");
		// Store user choice
		String sSelectEmployee = sUserInput.nextLine();
		boolean bIsValidSelectEmployee = false;
		do {
			try {
				int nSelectEmployee = Integer.parseInt(sSelectEmployee);
				if (nCount < nSelectEmployee) {
					System.out.println("------------ SELECTED INPUT NOT IN LIST --------------");
					//continue;
					break;
				}
				
				System.out.println("ENTER NO. OF ACCEPTED LEAVES : ");
				// Store user choice
				int nAcceptLeave = sUserInput.nextInt();
				int nApplyLeave = lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).GetApplyLeave();
				if(nApplyLeave < nAcceptLeave)
				{
					System.out.println("\n------------------------------------------------------");
					System.out.println("YOU CANNOT ACCEPT MORE THAN " + nApplyLeave + " LEAVE(S).");
					System.out.println("------------------------------------------------------\n");
					break;
				}
				else if(nAcceptLeave <= 0)
				{
					System.out.println("\n------------------------------------------------------");
					System.out.println("ACCEPTED LEAVE(S) SHOULD BE POSITIVE AND GREATER THAN 0.");
				    System.out.println("------------------------------------------------------\n");

				}
				else
				{
					lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).SetAcceptedLeave(nAcceptLeave);
					int nGetCurrentLeave = lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).GetLeave();
					int nAfterAcceptLeave = nGetCurrentLeave - nAcceptLeave;
					//int nApplyLeave = lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).GetApplyLeave();
					lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).SetRejectedLeave(nApplyLeave - nAcceptLeave);
					lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).SetLeave(nAfterAcceptLeave);
					lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).SetLeaveFlag(false);
					StoreIndex = null;
					bIsValidSelectEmployee = true;
					System.out.println("-------- LEAVE(S) IS/ARE ACCEPTED SUCCESSFULLY ---------");
				}
			} catch (Exception ex) {
				System.out.println("---------- ONLY INTEGER VALUE IS ACCEPTABLE ----------");
				bIsValidSelectEmployee = false;
				break;
				//continue;
			}

		} while (bIsValidSelectEmployee != true);
		return lstEmpInfo;
	}

	// Display employee report
	public void DisplayEmployeeReport(ArrayList<Employee> lstEmpInfo) {
		System.out.println("Employee Username:"+lstEmpInfo.get(0).GetRA());
		System.out.println("Employee Password:"+this.getsUserid());
		if (lstEmpInfo == null || lstEmpInfo.size() == 0) {
			System.out.println("--------------- EMPLOYEE LIST IS EMPTY ---------------");
			return;
		}

		int nCount = 0;
		for (int i = 0; i < lstEmpInfo.size(); i++) {
			if (lstEmpInfo.get(i).GetRA().equals(this.getsUserid())) {
				System.out.print("\n");
				System.out.println("------------------------------------------------------");
				nCount = nCount + 1;
				System.out.println("                   ID NO. : " + nCount);
				System.out.println("USERNAME OF THE EMPLOYEE  : " + lstEmpInfo.get(i).getsUserid());
				System.out.println("NO. OF REMAINING LEAVE(S) : " + lstEmpInfo.get(i).GetLeave());
				System.out.println("------------------------------------------------------");
				System.out.print("\n");

			}
			else
			{
				System.out.println("--------------- EMPLOYEE LIST IS EMPTY ---------------");
			}
		}
	}

}
