from datetime import datetime


class Bank:
    def __init__(self, name, Balance = 0):
        self.__name = name
        self.__balance = Balance

    

    def Deposit(self, amount):
        print(f"last amount was {self.__balance}, after adding {amount} it is become {self.__balance + amount}")
        self.__balance += amount
    

    def Withdrawl(self, amount):
        if self.__balance <= 0:
            print("Not Enough Balance to Withdrawl")
            return False
        elif self.__balance < amount:
            print(f"You can only wothdrawl the {self.__balance}")
            return False
        print(f"Total Balance was {self.__balance}, after Withdrawl of {amount} it is now {self.__balance - amount}")
        self.__balance -= amount

    def ViewBalance(self):
        print(f"account Holder Name is {self.__name} \nTotal Balance in account is {self.__balance}")
        return f"Total Balance in account was {self.__balance}"

def get_time():
    day, month, year = datetime.now().day, datetime.now().month, datetime.now().year
    hours, minutes, secounds = datetime.now().hour, datetime.now().minute, str(datetime.now().second)
    if int(secounds)  < 10 :
        secounds = "0"+str(secounds)
    time = str(day) +'/'+ str(month) +'/'+ str(year) + "  " + str(hours) +':'+ str(minutes) +':'+secounds
    return time

Y = True
counter = 0
name = input('Enter your Name to Open the Account : \n')
account = Bank(name)

f = open('Transecations.txt', 'r+')

f.seek(0,2)
f.write("\n"+f"\n\nAccount opened By {name}\n\n")
while Y:

    ch = int(input("Enter the Number According to your choice : \n1 --> To Deposite \n2 --> To WithDrawl \n3 --> To View Balance \n9 --> To Exit\n----->   "))
    match ch :
        case 1 :
            amount = int(input("Enter the Total Amount to Deposit : \n"))
            account.Deposit(amount)
            time = get_time()
            f.write("\n"+time + " --> "+f"{amount} Deposited")
            f.write("\n\n---------------------------------------------------------------------\n")

        case 2:
            amount = int(input("Enter the Total Amount to withdrawl : \n"))
            account.Withdrawl(amount)
            time = get_time()
            f.write("\n"+time+ " --> "+f"{amount} Withdrawled")
            f.write("\n\n---------------------------------------------------------------------\n")
        
        case 3:
            account.ViewBalance()
            time = get_time()
            f.write("\n"+time + " --> "+f"Balance Viewd ")
            f.write("\n\n---------------------------------------------------------------------\n")

        case 9:
            time = get_time()
            value = account.ViewBalance()
            f.write("\n"+time + " --> "+f"When Closed, {value}")
            Y = False
        
        
        case _:
            print("Invalid Choice, Please Try again")

f.write("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
f.close()

