import math
print("Welcome to the online banking applicaion")

def signin():
    global name
    global pin
    global cb #current balance
    name=str(input("please enter your name : "))
    pin=str(input("please create 6 digits pin : "))
    if len(pin)==6:
        print("Thanks for creating your bank account")
    else:
        print("The pin has to be in 6 digits")
        newpin=str(input("please create 6 digits pin : "))
        if len(newpin)!=6:
            print("The pin has to be in 6 digits")
            signin()
        else:
            pin=newpin
            print("Thanks for creating your bank account")
    
def forgetpin():
    recovery=str(input("please input new your pin 6 digits : "))
    if len(recovery)!=6:
        print("The pin has to be in 6 digits")
        forgetpin()
    else:
        print("the new pin has been stored,pleas log in")
        pin=recovery
        login()

def depositeinterest(p,r,t):
    p=float(p)
    r=float(r)
    t=float(t)
    rt=r*t
    e=math.exp(rt)
    a = p*e
    return a

def login():
    name1=str(input('please enter your name: '))
    pin1=str(input('please enter your pin: '))
    if name1 == name and pin1 == pin:
        print("welcome online bank "+" "+name1)
        print("please choice the menu down here")
        listmenu=["1-Deposit","2-Withdraw","3-Transfer","4-Check Balance","5-Deposite interest rate","6-Calculate compound interest"]

        for b in listmenu:
            print(b)
        choose=int(input("please enter the number of your choishe: "))
        d=0
        w=0
        cb=0
        if choose == 1:
            d=int(input("enter amount of your deposite: "))
            cb=d
            print("your current balance is" + " "+str(cb))
        elif choose == 2:
            w=int(input("enter the amount of many that you want to withdraw : "))
            if w>cb:
                print("your current balance is not sufficient for this transacsion")
                login()
            else:
                cb=d-w
                print(str(w)+ " " + " has been withdraw from your account "+ " " + "and your current balance is " + " " + str(cb))
        elif choose == 3:
            dest=str(input("Please enter the account number of your destination in 8 digits"))
            if len(dest) == 8:
                amount = int(input("Please enter the amount of money that you want to transfer"))
                if amount > cb:
                    print("Your current balance is not sufficient for this transaction")
                    login()
                else:
                    cb = d - amount
                    print("The transaction of" + " " + str(amount) + " " + "has been transfered to" + " " + str(dest) + " " + " your current balance is" + str(cb))
            else:
                print("The transaction has been rejected since the destination account number is invalid")
                login()
                
        elif choose == 4:
            print("Your current balance is" +" " + str(cb))
            
        elif choose == 5:
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate = 2
            else:
                rate = 1.5
            print("Your current deposit interest rate is" +" "+ str(rate) + " %")
        elif choose == 6:
            listoption = ["1-Calculate your deposit compound interest based on your CB","2-Calculate your deposit compound interest based on your deposit input"]
            for n in listoption:
                print(n)
            choice = int(input("Please enter your choice from the options above"))
            if choice == 1:
                timing = str(input("How many years you want to invest your money"))
                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex = 2/100
                else: 
                    ratex = 1.5/100
                print("Your current balance in" + " " + timing + " " + "years will be")
                print(depositinterest(cb,ratex,timing))
            elif choice == 2:
                timing1 = str(input("How many years you want to invest your money"))
                money = str(input("Please emnter the amount of money you would like to deposit"))
                money = int(money)
                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex = 2/100
                else: 
                    ratex = 1.5/100
                print("Your current balance in" + " " + timing + " " + "years will be")
                print(depositinterest(money,ratex,timing))
        else:
            print("Option is not available, back to main menu")
            login()
            
    else:
        print("either of your username or pin is wrong, did you create your account")
        list1=["1-yes","2-no"]
        for i in list1:
            print(i)
        inp=int(input("enter your choice below: "))
        if inp == 1:
            list2=["1-do you want attemp to log in again?","2-you forget your pin"]
            for e in list2:
                print(e)
            answer=str(input("please enter your choice: "))
            answer=int(answer)
            if answer == 1:
                login()
            elif answer == 2:
                forgetpin()
            else:
                print("option is not avaible")
        elif inp == 2:
            print("pleas create your account")
            signin()

def mainmenu():
    optionone = int(input("Choose 1 to signin \nchoose 2 to log in \n"))
    if optionone == 1:
        signin()
    elif optionone == 2:
        login()
    else:
        print("Option is not available")
        mainmenu()
    exit()
    
def exit():
    answer = str(input("Do you still want to conduct transaction? Yes or No : "))
    if answer == "Yes":
        login()
    elif answer == "No":
        print("Thank you for using this app")
    else: 
        print("Option is not available")
        mainmenu()

mainmenu()


