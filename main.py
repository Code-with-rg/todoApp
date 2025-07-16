import sqlite3

class StudentLife:
    @staticmethod
    def addData(name, mobile, birthdate):
        
        query = "INSERT INTO students (NAME, MOBIL_NUMBER, BIRTHDATE) VALUES (?,?,?)"
        params = (name, mobile, birthdate)
        query2 = "SELECT ROLL_NO FROM students WHERE MOBIL_NUMBER = ?"
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute(query, params)
        conn.commit()
        conn.close()
        print(f"{name} is added in record")
        return 0
    @staticmethod
    def updateData( rollno,name = None, mobile= None, birthdate= None ,ch = None):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        if ch.lower().strip() == 'name':
            param = (name, rollno)
            c.execute(f"""UPDATE students SET NAME = ? WHERE ROLL_NO = ?""", param)
            
            print(f'CHANGES DONE , NEW NAME AS {name} SET ON ROLL NUMBER {rollno}')
            return
        
        elif ch.lower().strip() == 'birthdate':
            param = (birthdate, rollno)
            c.execute(f"""UPDATE students SET BIRTHDATE = date(?) WHERE ROLL_NO = ? """, param)
            print(f'CHANGES DONE , NEW Birth Date AS {birthdate} SET ON ROLL NUMBER {rollno}')
            return
            
        elif ch.lower().strip() == 'mobile number':
            param = (mobile, rollno)
            c.execute(f"""UPDATE students SET MOBIL_NUMBER = ? WHERE ROLL_NO = ?""", param)
            print(f'CHANGES DONE , NEW MOBILE AS {mobile} SET ON ROLL NUMBER {rollno}')
            return
        else :
            return
    @staticmethod   
    def deleteStudent(rollno):
        param = (rollno)
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute("""DELETE FROM students WHERE ROLL_NO = ?""", param)
        conn.commit()
        conn.close()
        print(f"DELETED {rollno} FROM RECORDS")
    
    def showStudent(self, ch : int = None):
        conn = sqlite3.connect('students.db')
        if ch == '' :
            DATA = conn.execute("SELECT ROLL_NO, NAME, MOBIL_NUMBER FROM students")
            for data in DATA :
                print(f"\nStudent Roll Number : {data[0]}")
                print(f"\nStudent NAME : {data[1]}")    
                print(f"\nStudent MOBILE NUMBER : {data[2]}")
                # print(f"\nStudent BIRTH DATE : {data[3]}")
        else :
            params = (ch)
            DATA = conn.execute("SELECT * FROM students WHERE ROLL_NO = ?",params)
            for data in DATA :
                print(f"\nStudent Roll Number : {data[0]}")
                print(f"\nStudent NAME : {data[1]}")    
                print(f"\nStudent MOBILE NUMBER : {data[2]}")
                print(f"\nStudent BIRTH DATE : {data[3]}")
    @staticmethod
    def getALL():
        conn = sqlite3.connect('students.db')
        DATA = conn.execute("SELECT * FROM students")
        for data in DATA :
            print(f"\nStudent Roll Number : {data[0]}")
            print(f"\nStudent NAME : {data[1]}")    
            print(f"\nStudent MOBILE NUMBER : {data[2]}")
            print(f"\nStudent BIRTH DATE : {data[3]}")



conn = sqlite3.connect('students.db')

student = StudentLife()

Y = True

while Y :
    task = input("""\nEnter the number According to your CHoice 
                 \nAdd New Student --> 1
                 \nUpdate the Student Details --> 2
                 \nView Student details --> 3
                 \nDelete Student --> 4
                 \nExit --> 9
                 """)
    match int(task):
        case 1 :
            name =input("\nEnter the Student Name : ")
            mobile = input("\nEnter the Student Mobile number : ")
            birthdate = input('\nEnter the Birthdate in formate (YYYY-MM-DD) e.g.(2025-07-16) : ')
            student.addData(name, mobile, birthdate)

        case 2:
            rollno = int(input("\nEnter the students Roll Number to whom the update is to be Done : "))
            ch = input("\nEnter the your choice what you want to update (name/mobile number/Birthdate) : ")
            if ch.lower().strip() == 'name' :
                name = input("\nEnter the new Name to add : ")
                student.updateData(rollno,name, ch = ch)

            elif ch.lower().strip() == 'birthdate':
                birthdate = input('\nEnter the Birthdate in formate (YYYY-MM-DD) e.g.(2025-07-16) : ')
                student.updateData(rollno,birthdate = birthdate, ch = ch)
            
            elif ch.lower().strip() == 'mobile number':
                mobile = input('\nEnter the new MOBILE  : ')
                student.updateData(rollno, mobile = mobile, ch = ch)
            
           
            
        case 3:
            ch = input("\nEnter the Roll number to see the specific student's detals else leave blank : ")
            if ch == '':
                student.showStudent()
            student.showStudent(ch=ch)
        
        case 4:
            rollno = input("\nEnter the Roll number : ")
            confirm = input('are you sure?, you want to delete the data : y/n --> ')
            if confirm.lower().strip() == 'y':
                student.deleteStudent(rollno)
        case 9:
            Y = False
        
        case 5:
            student.getALL()
        
        case _:
            print("\nInvalid Choice !!")

