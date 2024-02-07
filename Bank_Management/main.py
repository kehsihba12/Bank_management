import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database='bank_management')


def OpenAcc():
    n = input("Enter your full name: ")
    ac = input("Enter The Account Number:")
    db = input("Enter you date of birth:")
    add = input("Enter your address:")
    cn = input("Enter your contact number:")
    ob = int(input("Enter your opening balance:"))
    data1 = (n,ac,db,add,cn,ob)
    data2 = (n,ac,ob)
    sql1 =('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into amount values(%s,%s,%s)')
    x = mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Successfully")
    main()
def Deposit():
    amount = input("Enter The Amount You Deposit")
    ac = input("Enter The Account Number:")
    a = 'select balance from amount where Account_No =%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    t = result[0]+amount
    sql = 'update amount set balance = %s where Account_No = %s'
    d = (t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()
def Withdraw():
    amount = input("Enter The Amount You Want to Withdraw")
    ac = input("Enter The Account Number:")
    a = 'select balance from amount where Account_No =%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = 'update amount set balance = %s where Account_No = %s'
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()

def BalanceEnquiry():
    ac = input("Enter The Account Number:")
    a = 'select * from amount where Account_No =%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    print("Your Current Balance",ac,"is",result[-1])
    main()

def CustomerDel():
    ac = input("Enter The Account Number:")
    a = 'select * from amount where Account_No =%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()
def CloseAcc():
    ac = input("Enter your Account Number:")
    sql1 = 'delete from account where Account_no = %s'
    sql2 = 'delete from amount where Account_no =%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()


def main():
    print('''

    1. Open New Account
    2. Deposit Amount
    3. Withdraw
    4. Balance Enquiry
    5. Display Customer Details
    6. Close an Account

    ''')


    choice = int(input("Enter the Task You Wanted to perform:   "))  # Convert user input to an integer

    if choice == 1:
        OpenAcc()
    elif choice == 2:
        Deposit()
    elif choice == 3:
        Withdraw()
    elif choice == 4:
        BalanceEnquiry()
    elif choice == 5:
        CustomerDel()
    elif choice == 6:
        CloseAcc()
    else:
        print("Please enter the correct option")

main()






