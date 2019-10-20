import os #including Operating System
List_of_codes=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_Names=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_creditHours=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_sem=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stdRegNoList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stdNamesList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stdCourseList=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
def splitting(b):#splitting words in letters
	global array
	array=[]
	a=""
	for letter in b:
		if letter==',':
			array=array + [a]
			a=""
		else:
			a+=letter
	array= array + [a]
def login1(): #loging in admin account
	username=str(input("enter username: "))
	password=str(input("enter password: "))
	with open('admin.txt','r') as file:
		for line in file:
			splitting(line)
			if array[0]==username and array[1]==password:
				print("_You are logged into the system._")
				return True
			else:
				print("_Sorry! you are not signed in._TRY AGAIN_")

def login2(): #loging in student account
	username=str(input("enter reg. #: "))
	password=str(input("enter password: "))
	global op
	op=0
	with open("new.txt","r") as file:
		for line in file:
			splitting(line)
			q=array[1]
			Name=q.split()
			l=Name[0]
			if (array[0]==username) and (l[-3:]):
				print("_You are logged into yhr system._")
				return True
			else:
				print("_Sorry you are not signed in._")
	return(op)
	#splitting function is made too

def save_course(): #each times the modifications are made in any data/file it would be saved
	a=0
	Num=['1','2','3']
	with open('test.txt',"w") as file:
		for i in List_of_codes:
			if List_of_creditHours[a] != 0:
				file.write(str(List_of_codes[a])+','+str(List_of_Names[a])+','+str(List_of_creditHours[a])+','+str(List_of_sem[a]+'\n'))
			a+=1
			
def load_course(): #loding data from external files
	with open('test.txt','r') as file:
		a=0
		s=0
		for line in file:
			a+=1
			if s<a:
				splitting(line)
				List_of_codes[s]=array[0]
				List_of_Names[s]=array[1]
				List_of_creditHours[s]=array[2]
				List_of_sem[s]=array[3]
				s+=1
				
def isValidCourseCode(i): #function for if the course code is valid or not
	Uppercase_Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	Numeric_Characters=['0','1','2','3','4','5','6','7','8','9']
	if (i[0:1] in Uppercase_Characters) and (i[2:3:4] in Numeric_Characters):
		return True
	return(i)
def isValidCourseName(i): #function for if the course name is valid
	Uppercase_Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	if i[0] in Uppercase_Characters:
		return True
	return(i)
def isValidCreditHours(i): #function for if credit hours are valid
	Num=['1','2','3']
	if (i in Num):
		return True
	return(i)
def isValidsemesters(i): #function for if the semster number is valid i.e, upto 8
	available_sem=['0','1','2','3','4','5','6','7','8','0\n','1\n','2\n','3\n','4\n','5\n','6\n','7\n','8\n']
	if (i in available_sem):
		return True
	return(i)
def isLineEmpty(line):
    return len(line.strip()) < 1 
def removeEmptyLines(file):
    lines = []
    out = open(file,'r')
    lines = out.readlines()
    out.close()
    out = open(file,'w')
    t=[]
    for line in lines:
        if not isLineEmpty(line):
            t.append(line)
    out.writelines(t)   
    out.close()
def isValidRegNum(i): #function for checking if the register number entered is valid
	Uppercase_Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	Numeric_Characters=['0','1','2','3','4','5','6','7','8','9']
	a=0
	for letter in i:
		a+=1
	if ((a==11) and(i[0] =='2')and (i[1]=='0') and (i[2:3] in Numeric_Characters)  and (i[4] == '-') and (i[7]=='-') and (i[5:6] in  Uppercase_Characters) and (i[8:9:10] in Numeric_Characters)):
		return True
	return(i)
def isValidName(i): #function for checking if name of student is valid or not
	Uppercase_Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	Numeric_Characters=['0','1','2','3','4','5','6','7','8','9']
	stu=i.split()
	e=stu[0]
	w=stu[1]
	if ((e[0] in Uppercase_Characters) and (w[0] in Uppercase_Characters)):
		return True
	return(i)	
def Add_Course(i): #function for adding course of student
	List_of_codes[i]=x
	List_of_Names[i]=z
	List_of_creditHours[i]=p
	List_of_sem[i]=k
	t=[x,z,p,k]
	print("_Your course details have been submitted as: ",t,"_")
	return()
def Update_Course(i): #function for updatting courses of students
	u=0
	while u<i:
		print(u+1,List_of_codes[u],List_of_Names[u],List_of_creditHours[u],List_of_sem[u])
		u+=1
	d=int(input("Course to be changed: "))
	if d<=i:
		x,z,p,k=input("enter your details(Course Code/Course Name/Credit Hours/Semesters ):  ").split(",")
		if ((isValidCourseCode(x) is True) and (isValidCourseName(z) is True) and (isValidCreditHours(p) is True) and (isValidsemesters(k) is True)):
			List_of_codes[d-1]=x
			List_of_Names[d-1]=z
			List_of_creditHours[d-1]=p
			List_of_sem[d-1]=k
			print("_Your course has been updated._")
		else:
			print("invalid course details")
			x,z,p,k=input("enter your details again(Course Code/Course Name/Credit Hours/Semesters ):  ").split(",")
			if ((isValidCourseCode(x) is True) and (isValidCourseName(z) is True) and (isValidCreditHours(p) is True) and (isValidsemesters(k) is True)):
				List_of_codes[d-1]=x 
				List_of_Names[d-1]=z
				List_of_creditHours[d-1]=p
				List_of_sem[d-1]=k
				print("_Your course has been updated._")
			else:
				print("_Still invalid, couldn't update course._")
	else:
		print("_Entered Course doesn't exxist._")
def Delete_Course(i):#function for deleting courses of students
	u=0
	while u<=i:
		print(u+1,List_of_codes[u],List_of_Names[u],List_of_creditHours[u],List_of_sem[u])
		u+=1
	d=int(input("course to be deleted: "))
	if d<i:
		List_of_codes[d-1]=0
		List_of_Names[d-1]=0
		List_of_creditHours[d-1]=0
		List_of_sem[d-1]=0
		List_of_codes[d-1] = List_of_codes[u-1]
		List_of_Names[d-1]= List_of_Names[u-1]
		List_of_creditHours[d-1] = List_of_creditHours[u-1]
		List_of_sem[d-1] = List_of_sem[u-1]
		List_of_codes[u-1]=0
		List_of_Names[u-1]=0
		List_of_creditHours[u-1]=0
		List_of_sem[u-1]=0
		i-=1
	else:
		print("_course does not exist_")
def View_Courses(i):#function for viewing courses of students
	s=0
	print("COURSE_CODE  ","COURSE_NAME  ","   CREDIT_HOURS  ","      SEMESTER")
	while s<i:
		print(str(List_of_codes[s])+"           "+str(List_of_Names[s])+"               ",str(List_of_creditHours[s])+"             ",str(List_of_sem[s]))
		s+=1
def View_Courses_of_a_semester(i):#function for viewing courses of students in specific semester
		s=str(input("choose semester: "))
		print("COURSE_CODE ","COURSE_NAME ","CREDIT_HOURS ")
		e=0
		while e<i:
			if s+'\n'==(List_of_sem[e]):
				print((List_of_codes[e])+"        "+(List_of_Names[e])+"             "+str(List_of_creditHours[e]))
			e+=1
		if (s+'\n') not in List_of_sem:
			print("no course of semeter "+ s +" exists")
def Add_new_student(i):#function for adding new students
	stdRegNoList[i]=id
	stdNamesList[i]=student
def Update_student():#function for udating student information in record
	u=0
	d=str(input("Reg. # of student whose information to be changed: "))
	if d in stdRegNoList:
		for i in stdRegNoList:
			if stdRegNoList[u]==d:
				new_id,name=input("Enter student information(Reg. number/Name): ").split(',')
				if ((isValidRegNum(new_id) is True) and (isValidName(name) is True)):
					stdRegNoList[u]=new_id
					stdNamesList[u]=name
					print("_Student information has been updated_")

				else:
					print("_Invalid student information._")
					new_id,new_name=input("Enter student information(Reg. number/Name): ").split(',')
					if ((isValidRegNum(new_id) is True) and (isValidName(name) is True)):
						stdRegNoList[u]=new_id
						stdNamesList[u]=name
						print("_Student information has been updated._")
					else:
						print("_Still invalid, couldn't update details._")
			u+=1
	else:
		print("_Either reg. # or name is invalid._")
	return()
def Delete_student():#function for deleting student information
	u=0
	d=str(input("Reg. # of student whose information you want delete: "))
	if d in stdRegNoList:
		for i in stdRegNoList:
			if stdRegNoList[u]==d:
				stdRegNoList[u]=0
				stdNamesList[u]=0
				stdRegNoList[u] = stdRegNoList[r-1]
				stdNamesList[u]= stdNamesList[r-1]
				stdRegNoList[r-1]=0
				stdNamesList[r-1]=0
			u+=1
	else:
		print("_No student has register # :"+str(d)+"_")
def View_students(i):#function for viewing student information
	s=0
	print("sr. #     "+"Reg. #"+"                      "+"Student Name")
	while s<(i):
		print(str(s+1)+':       '+str(stdRegNoList[s])+"                  "+str(stdNamesList[s]))
		s+=1
def register():#function for registration of student
	student=str(input('Enter student reg.:  '))
	course=str(input('Enter course to be registered:  '))
	if student in stdRegNoList:
		if course in List_of_codes:
			s=0
			a=0
			for i in stdRegNoList:
				if stdRegNoList[s]!=student:
					s+=1
				else:
					break
			while stdCourseList[s][a]!=0:
				a+=1
			stdCourseList[s][a]=course
		else:
			print('mistake')
	return()
def unregister():#function to unregister student
	student=str(input('enter student reg.:  '))
	course=str(input('enter course to be registered:  '))
	s=0
	a=0
	o=0
	for i in stdRegNoList:
		if stdRegNoList[s]!=student:
			s+=1
		else:
			break
	if student in stdRegNoList:
		if course in stdCourseList[s]:
			while stdCourseList[s][a]!=course:
				a+=1
			while stdCourseList[s][o]!=0:
				o+=1
			stdCourseList[s][a]=stdCourseList[s][o-1]
			stdCourseList[s][o-1]=0
		else:
			print("either reg. # or course code is wrong.")
	return()
print("***Welcome to the University learning management system***")
#MAIN STARTS HERE
def main():
	with open('test.txt','r') as file:
		a=0
		for line in file:
			a+=1
	with open('new.txt','r') as file:
		b=0
		for line in file:
			b+=1
	global y
	global r
	y=a
	r=b
	print("1 "+" the admin")
	print("2 "+" the user")
	enter=int(input("choose the option for login: "))
	if enter==1:
		while True: 
			if login1() is True:
				print("_____________________________________________________________________________________________")
				while True:
					removeEmptyLines('test.txt')
					removeEmptyLines('new.txt')
					removeEmptyLines('admin.txt')
					load_course()
					print("1 "+"Add Course")
					print("2 "+"Update Course")
					print("3 "+"Delete Course")
					print("4 "+"View all Courses")
					print("5 "+"View courses of a semester")	
					print("6 "+"Add New Student")
					print("7 "+"Update Student")
					print("8 "+"Delete Student")
					print("9 " +"View All Students")
					print("10 "+"Register the course for Student")
					print("11 "+"Unregister the course for Student")
					print("12 "+"Logout of the System")
					print("13 "+"Exit Program")
					g=int(input("Choose the Option: "))
					if g==1:
						global x
						global z
						global p
						global k
						x,z,p,k=input("enter details(Course Code/Course Name/Credit Hours/Semesters ):  ").split(",")
						if x not in List_of_codes:						
							if ((isValidCourseCode(x) is True) and (isValidCourseName(z) is True) and (isValidCreditHours(p) is True) and (isValidsemesters(k) is True)):
								Add_Course(y)
							else:
								print("Invalid Details")
								x,z,p,k=input("enter course details again(Course Code/Course Name/Credit Hours/Semesters ):  ").split(",")
								if ((isValidCourseCode(x) is True) and (isValidCourseName(z) is True) and (isValidCreditHours(p) is True) and (isValidsemesters(k) is True)):
									Add_Course(y)
								else:
									print("still invalid details, couldn't add course")
									y-=1
						else:
							print("_This course cod has already been assigned to subject._")
						y+=1
					if g==2:
						Update_Course(y)
					if g==3:
						Delete_Course(y)
						y-=1
					if g==4:
						View_Courses(y)
					if g==5:
						View_Courses_of_a_semester(y)
					if g==6:
						global id
						global student
						id,student=input("Enter student information(Reg. number/Name): ").split(',')
						if id in stdRegNoList:
							print("This reg. no. already assigned.")
						elif ((isValidRegNum(id) is True) and (isValidName(student) is True)):
							Add_new_student(r)
						else:
							print("invalid details, Enter again: ")
							id,student=input("Enter student information(Reg. number/Name): ").split(',')
							if ((isValidRegNum(id) is True) and (isValidName(student) is True)):
								Add_new_student(r)
							else:
								print("still invalid details")
								r-=1
						r+=1
					if g==7:
						Update_student()
					if g==8:
						Delete_student()
					if g==9:
						View_students(r)
					if g==10:
						register()
					if g==11:
						unregister()
					if g==12:
						main()
					if g==13:
						exit()
					save_course()
					print("_____________________________________________________________________________________________")
	if enter==2:
		while True:
			if login2() is True:
				print("_____________________________________________________________________________________________")
				while True:
					print('1 '+'View Registered Courses')
					print('2 '+'Logout of the System')
					print('3 ','Exit Program')
					t=int(input('choose the option: '))
					if t==1:
							print(stdCourseList[op])
					if t==2:
						main()
					if t==3:
						exit()
					print("_____________________________________________________________________________________________")
main()
#THE END:)#