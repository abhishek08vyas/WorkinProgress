from EnLoginUserType import EnLoginUserType

class ReportingAuthority:
	
	# Store login True or False
	bIsLogin = False;
	# Store user type
	enUserType = EnLoginUserType.RA.name;
	# Store user id
	sUserid = ""
	# Store password
	sPassword = ""
	def __init__(self):

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

	def setsPassword(self,  sPassword):
		self.sPassword = sPassword;

	# Employee leave request accept/reject
	def EmployeeLeaveReqAcceptReject(self, lstEmpInfo):
		if (len(lstEmpInfo) == 0):
			print("--------------- EMPLOYEE LIST IS EMPTY ---------------");
			return lstEmpInfo;
		nCount = 0;
		bApplyLeaveFlag = False;
		StoreIndex = []
		i=0
		for i in lstEmpInfo:
			if (lstEmpInfo[i].GetApplyLeave() > 0 and (lstEmpInfo[i].GetRA().equals(self.getsUserid()) == True)
					and lstEmpInfo[i].GetLeaveFlag() != False):
				print("");
				print("------------------------------------------------------");
				nCount = nCount + 1;
				print("                  ID NO. : " , nCount);
				print("USERNAME OF THE EMPLOYEE : " , lstEmpInfo[i].getsUserid());
				print("NO. OF APPLIED LEAVE(S)  : " , lstEmpInfo[i].GetApplyLeave());
				print("------------------------------------------------------\n");
				StoreIndex.add(i);
				bApplyLeaveFlag = True;

		if (bApplyLeaveFlag == False):
			print("------------ CURRENTLY THE LIST IS EMPTY -------------");
			return lstEmpInfo;

		# Scanner sUserInput = new Scanner(System.in);
		print("\nENTER ID FROM THE ABOVE LIST (INTEGER VALUE ACCEPTABLE) : ")
		# Store user choice
		nSelectEmployee = int(input())
		bIsValidSelectEmployee = True;
		while(bIsValidSelectEmployee):
			if (nCount < nSelectEmployee):
				print("------------ SELECTED INPUT NOT IN LIST --------------");
				# continue;
				break;
				print("ENTER NO. OF ACCEPTED LEAVES : ");
				# Store user choice
				nAcceptLeave = int(input())
				nApplyLeave = lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).GetApplyLeave();
				if(nApplyLeave < nAcceptLeave):
					print("\n------------------------------------------------------")
					print("YOU CANNOT ACCEPT MORE THAN " , nApplyLeave , " LEAVE(S).")
					print("------------------------------------------------------\n")
					break;
				elif(nAcceptLeave <= 0):
					print("\n------------------------------------------------------")
					print("ACCEPTED LEAVE(S) SHOULD BE POSITIVE AND GREATER THAN 0.")
				    print("------------------------------------------------------\n")
				else:
					lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).SetAcceptedLeave(nAcceptLeave);
					nGetCurrentLeave = lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).GetLeave();
					nAfterAcceptLeave = nGetCurrentLeave - nAcceptLeave;
					#int nApplyLeave = lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).GetApplyLeave();
					lstEmpInfo.get[StoreIndex.get(nSelectEmployee - 1).SetRejectedLeave(nApplyLeave - nAcceptLeave);
					lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).SetLeave(nAfterAcceptLeave);
					lstEmpInfo.get(StoreIndex.get(nSelectEmployee - 1)).SetLeaveFlag(false);
					StoreIndex = null;
					bIsValidSelectEmployee = true;
					print("-------- LEAVE(S) IS/ARE ACCEPTED SUCCESSFULLY ---------");
			#} catch (Exception ex) {
				#	print("---------- ONLY INTEGER VALUE IS ACCEPTABLE ----------");
				#bIsValidSelectEmployee = false;
				#break;*/
				#continue;
		#} while (bIsValidSelectEmployee != true);
		return lstEmpInfo


# Display employee report
	def DisplayEmployeeReport(self, lstEmpInfo):
		print("Employee Username:"+lstEmpInfo[0].GetRA());
		print("Employee Password:"+self.getsUserid());
		if (len(lstEmpInfo) == 0) :
			print("--------------- EMPLOYEE LIST IS EMPTY ---------------")
			return

		nCount = 0;
		for i in lstEmpInfo:
			if (lstEmpInfo[i].GetRA().equals(self.getsUserid())):
				print("\n");
				print("------------------------------------------------------");
				nCount = nCount + 1;
				print("                   ID NO. : " , nCount);
				print("USERNAME OF THE EMPLOYEE  : " , lstEmpInfo.get(i).getsUserid());
				print("NO. OF REMAINING LEAVE(S) : " , lstEmpInfo.get(i).GetLeave());
				print("------------------------------------------------------");
				print("\n");
			else:
				print("--------------- EMPLOYEE LIST IS EMPTY ---------------")