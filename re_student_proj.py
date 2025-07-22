# '/home/tusharhedange/ganesh\\ rajput'
import re
import datetime
import sqlite3

class student:

    def __init__(self):
        self.conn, self.cursor = self.connection()

    def connection(self):
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        return (conn, cursor)
    
    def NameCheck(self,name):
        if len(name)<3:
            return False
        elif re.match('([\w]+)\s*([\w]+)', name):
            return True
        

    def BirthdateCheck(self,birthdate):
        if re.match('\d\d-\d\d-\d\d\d\d', birthdate):
            year = int(birthdate.split('-')[-1])
            thisYear = datetime.datetime.now().year
            if thisYear - year >= 18 :
                return True
            else:
                return False
        else:
            return False
    

    def emailCheck(self, email):
        if re.match('([\w]+)@([\w]+).([\w]+)', email):
            return True
        else :
            return False

    def MobileNumberCheck(self, mobile):
        if not len(str(mobile)) == 10:
            return False
        else:
            return True

    def stDataAdd(self, name, birthdate, email, mobile):
        if not self.NameCheck(name):
            return
        elif not self.BirthdateCheck(birthdate):
            return
        elif not self.emailCheck(email):
            return
        elif not self.MobileNumberCheck(mobile):
            return
        else :
            self.cursor.execute('INSERT INTO STUDENTS (NAME, BIRTHDATE, EMAIL, MOBILE_NUMBER) VALUES (?, ?, ?, ?)',(name,birthdate, email, mobile))
            self.conn.commit()
        
    def getStudents(self,email = None):
        if email == None:
            data = self.cursor.execute('SELECT * FROM STUDENTS')
            for student in data:
                print(f"Name : {student[1]}, Birthdate : {student[2]}, Email : {student[3]}, Mobile Number : {student[4]}")
        else:
            student = self.cursor.execute('SELECT * FROM STUDENTS WHERE EMAIL = ?', email)
            print(f"Name : {student[1]}, Birthdate : {student[2]}, Email : {student[3]}, Mobile Number : {student[4]}")

st = student()
x = True
while x :
    ch = int(input("Enter Your Choice : \n1 --> Add Data\n2 --> View Data\n "))
    match ch:
        case 1:
            name = input("\nEnter student's Name : ")
            Birthdate = input("\nEnter student's Birth Date in formate(01-01-2005) : ")
            email = input("\nEnter Student's Email : ")
            mobileNumber = input("\nEnter the Student's Mobile Number : ")
            st.stDataAdd(name, Birthdate, email, mobileNumber)
         
        case 2:
            email = input("\nEnter Student's Email to see the details else leave blank : ")
            if email == '':
                st.getStudents()
            else:
                st.getStudents(email)

        case 9:
            x = False

        case _ :
            continue
            