import mysql.connector
import calendar

con = mysql.connector.connect(host="localhost", user='root', passwd='${{PASS.Pass}}', database='xiia')
cur1 = con.cursor()

def menu():
    print("\t\t\t-----------------------------------------------------------------------")
    print("\t\t\t**********************************MENU*********************************")
    print("\t\t\t-----------------------------------------------------------------------")
    print()
    print("\t\t\t***********************1. REGISTER NEW EMPLOYEES***********************")
    print("\t\t\t********************2. UPDATE DETAILS OF EMPLOYEES*********************")
    print("\t\t\t******************3. DISPLAY DETAILS OF AN EMPLOYEE********************")
    print("\t\t\t*************4. REMOVE AN EMPLOYEE WHO HAVE LEFT OFFICE****************")
    print("\t\t\t******************5. DISPLAY ALL EMPLOYEE DETAILS**********************")
    print("\t\t\t********6. DISPLAY DETAILS OF EMPLOYEES WHO HAVE LEFT THE OFFICE*******")
    print("\t\t\t******************7. DISPLAY SORTED EMPLOYEE DETAILS*******************")
    print("\t\t\t**********8. DISPLAY AVERAGE SALARY THAT AN EMPLOYEE RECEIVES**********")
    print("\t\t\t******************9. CREATE PAY SLIP OF AN EMPLOYEE********************")
    print("\t\t\t******************10. REMOVE ALL EMPLOYEE'S DETAILS********************")
    print("\t\t\t\t********************11. CREATE TABLE*********************")
    print("\t\t\t\t******************12. DISPLAY ALL TABLES****************")

def insert(office):
    while True:
        try:
            Id = input("enter emp_id: (should have unique value)")
            name = input("employee name: ")
            depar = input('enter department: ')
            desig = input('enter designation: ')
            sal = input('enter salary: ')
            mob = input("enter mob: ")
            doj = input("enter date of joining (yyyy-mm-dd): ")
            query = "insert into mdps values('{}','{}','{}','{}','{}','{}','{}','{}')".format(Id, name, depar, desig, sal, mob, doj, office)
            cur1.execute(query)
            con.commit()
            print()
            print("\t\t\t\t*************EMPLOYEE REGISTERED SUCCESSFULLY ;^) ***********")
            print()
            ch = input('do you want to register more employees? y or n: ')
            if ch in 'nN':
                break
        except mysql.connector.errors.IntegrityError:
            print('\t\t\t\t*****Employee ID already exists! Please enter a unique ID.*****')
        except:
            print('\t\t\t\t*****please retry, try to enter field name and value correctly****')

def update():
    while True:
        try:
            name = input("enter name of employee whose details are to be updated: ")
            query1 = "select * from mdps"
            cur1.execute(query1)
            c = cur1.fetchall()
            for i in c:
                if i[1] == name:
                    print('\t\t\tfield names: emp_id, emp_name, department, designation, salary, mob, date_of_joining')
                    print()
                    c_field = input('enter field name to be updated: ')
                    new = input('enter new value: ')
                    query = 'update mdps set {}="{}" where emp_name="{}" '.format(c_field, new, name)
                    cur1.execute(query)
                    con.commit()
                    print('\t\t\t\t*****DETAILS OF EMPLOYEE UPDATED SUCCESSFULLY ;^) *****')
            ch = input('do you want to update more ? y or n: ')
            if ch == 'n':
                break
        except:
            print("\t\t\t\t****enter a valid employee name, the one provided earlier doesn't exist :^( **** ")
            print('\t\t\t\t*****please retry, try to enter field name and value correctly****')

def search():
    while True:
        try:
            print('\t\t\tfield names: emp_id, emp_name, department, designation, salary, mob, date_of_joining')
            print()
            c = input('enter field name on whose basis you wish to display details of the employee: ')
            j = input('enter value: ')
            query = 'select * from mdps where {}="{}"'.format(c, j)
            cur1.execute(query)
            k = cur1.fetchall()
            if len(k) == 0:
                print('\t\t\t\t\t*********EMPLOYEE DETAILS NOT FOUND**********')
            else:
                print("\t\t\t******************DISPLAYING DETAILS OF EMPLOYEE**********************")
                for i in k:
                    print("emp_id : ", i[0])
                    print("emp_name : ", i[1])
                    print("department : ", i[2])
                    print("designation : ", i[3])
                    print("salary : ", i[4])
                    print("mob : ", i[5])
                    print("date_of_joining : ", i[6])
                    print("office : ", i[7])
                    print('\n')
            ch = input('do you want to display more ? y or n: ')
            if ch in 'nN':
                break
        except:
            print('\t\t\t\t*****please retry, try to enter field name and value correctly****')

def delete():
    while True:
        try:
            a = input('enter employee id who have left the office: ')
            query = 'select * from mdps where emp_id="{}"'.format(a)
            cur1.execute(query)
            r = cur1.fetchall()
            if len(r) == 0:
                print('\t\t\t\t\t*********EMPLOYEE NOT FOUND**********')
            else:
                query1 = 'delete from mdps where emp_id={}'.format(a)
                e, f, g, h, i, j, k, l = r[0]
                query3 = 'insert into DEL values("{}","{}","{}","{}","{}","{}","{}","{}")'.format(e, f, g, h, i, j, k, l)
                cur1.execute(query3)
                cur1.execute(query1)
                print('\t\t\t\t**********EMPLOYEE REMOVED SUCCESSFULLY**********')
        except:
            print('\t\t\t\t*************************Sorry Not Possible :( *********************************')
        con.commit()
        ch = input('do you want to remove more employees ? y or n: ')
        if ch == 'n':
            break

def deleten():
    query = 'truncate mdps'
    cur1.execute(query)
    con.commit()
    print('\t\t\t**********ALL THE EMPLOYEE DETAILS ARE DELETED SUCCESSFULLY************')

def display_all():
    query = 'select * from mdps'
    cur1.execute(query)
    k = cur1.fetchall()
    x = len(k)
    if x == 0:
        print('\t\t\t*NO EMPLOYEE DETAILS ARE ENTERED YET... INSERT ONE AND PROCEED*')
    else:
        print("\t\t\t******************DISPLAYING ALL EMPLOYEE DETAILS**********************")
        for i in k:
            print("emp_id : ", i[0])
            print("emp_name : ", i[1])
            print("department : ", i[2])
            print("designation : ", i[3])
            print("salary : ", i[4])
            print("mob : ", i[5])
            print("date_of_joining : ", i[6])
            print("office : ", i[7])
            print('\n')

def display_sorted():
    try:
        print('\t\t\tfield names: emp_id, emp_name, department, designation, salary, mob, date_of_joining, office')
        c = input('enter field name on whose basis sorting should be done: ')
        query = 'select * from mdps order by {}'.format(c)
        cur1.execute(query)
        k = cur1.fetchall()
        x = len(k)
        if x == 0:
            print('\t\t\t*NO EMPLOYEE DETAILS ARE ENTERED YET... INSERT ONE AND PROCEED*')
        else:
            print("\t\t\t******************DISPLAYING SORTED EMPLOYEE DETAILS*******************")
            for i in k:
                print("emp_id : ", i[0])
                print("emp_name : ", i[1])
                print("department : ", i[2])
                print("designation : ", i[3])
                print("salary : ", i[4])
                print("mob : ", i[5])
                print("date_of_joining : ", i[6])
                print("office : ", i[7])
                print('\n')
            x -= 1
    except:
        print('\t\t\t\t*please retry, try to enter field name and value correctly')

def average_sal():
    query1 = 'select sum(salary) from mdps'
    query2 = 'select count(*) from mdps'
    cur1.execute(query1)
    c = cur1.fetchall()
    cur1.execute(query2)
    d = cur1.fetchall()
    print('\t\t\t*************The average salary of employees is: ', c[0][0] // d[0][0], '**********************')

def pay_slip():
    try:
        a = input('enter employee id : ')
        b = input('enter employee name : ')
        c = input('enter Month : ')
        d = int(input('enter pay of that month: '))
        e = int(input('enter BONUS amount (enter "0" if no bonus is awarded) : '))
        f = int(input('enter leaves number of taken : '))
        year, month, _ = map(int, c.split('-'))
        num_days = calendar.monthrange(year, month)[1]
        n = d + e - (f * (d / num_days))
        query = 'insert into pay values("{}","{}","{}",{},{},{},{})'.format(a, b, c, d, e, f, n)
        cur1.execute(query)
        con.commit()
        query = 'select * from pay'
        cur1.execute(query)
        k = cur1.fetchall()
        x = len(k)
        print()
        print()
        print("\t\t\t*******CREATING PAY SLIP FOR ", b.upper(), "*******")
        print()
        print("\t\t\t*******************PLEASE WAIT*******************")
        print()
        print("\t\t\t*************YOUR PAY SLIP IS READY**************")
        for i in k:
            print("Emp_id:", i[0])
            print("Emp_name:", i[1])
            print("Month:", i[2])
            print("Pay( ", c, "):", i[3])
            print("Bonus:", i[4])
            print("Leaves taken:", i[5])
            print("Total pay of ", c, ":", i[6])
            print('\n')
            query = 'truncate pay'
            cur1.execute(query)
            con.commit()
    except:
        print('\t\t\t\t*****please retry, try to enter valid details correctly****')

def left_emp():
    query = 'select * from DEL'
    cur1.execute(query)
    k = cur1.fetchall()
    x = len(k)
    if x == 0:
        print('\t\t\t*NO EMPLOYEE DETAILS ARE ENTERED YET... INSERT ONE AND PROCEED*')
    else:
        print("\t\t\t********DISPLAYING DETAILS OF EMPLOYEES WHO HAVE LEFT THE OFFICE*******")
        for i in k:
            print("emp_id : ", i[0])
            print("emp_name : ", i[1])
            print("department : ", i[2])
            print("designation : ", i[3])
            print("salary : ", i[4])
            print("mob : ", i[5])
            print("date_of_joining : ", i[6])
            print("office : ", i[7])
            print('\n')

def create_table():
    n = input('enter table name: ')
    c = input('enter the name of your office: ')
    print('\t\t\t***** WELCOME USER OF ', c, '. CREATING TABLE, PLEASE WAIT***** ')
    cur1.execute('create table {}(emp_id char(10) primary key,emp_name char(40) not null,department char(40),designation char(40),salary char(14),mob char(10),date_of_joining date, office char(80) default "{}")'.format(n, c))
    con.commit()
    print('\t\t\t\t***************************TABLE CREATED**********************')
    print('\t\t\t\t********************START INSERTING RECORDS ;-) **********')


def show_tables():
    query = 'show tables'
    cur1.execute(query)
    c = cur1.fetchall()
    if len(c) == 0:
        print('\t\t\t***NO TABLES ARE FORMED YET... CREATE ONE TO PROCEED***')
    else:
        for i in c:
            print(i)


print()
print("\t\t\t\t***************************WELCOME***********************")
print()
print("\t\t\t***THIS PROGRAMME ENABLES YOU TO STORE YOUR EMPLOYEE DETAILS SECURELY***")
print()
office = input('enter the name of your office: ')
print()
print()
print('\t\t\t***** WELCOME USER OF ',"< ", office.upper(),' >',' PLEASE WAIT***** ')
print()
k = input("Do you want to begin  :^{)  ? y or n: ")
print()
while k in "yY":
    menu()
    c = input("Enter Your Choice: ")
    try:
        if int(c) == 1:
            insert(office)
            k = input("do you want to do anything else? y or n:")
            print()
        if int(c) == 2:
            update()
            k = input("do you want to do anything else? y or n: ")
            print()
        if int(c) == 3:
            search()
            k = input("do you want to do anything else? y or n: ")
            print()
        if int(c) == 4:
            delete()
            k = input("do you want to do anything else? y or n: ")
            print()
        if int(c) == 5:
            display_all()
            k = input("do you want to do anything else? y or n: ")
            print()
        if int(c) == 6:
            left_emp()
            k = input("do you want to do anything else? y or n: ")
            print()
        if int(c) == 7:
            display_sorted()
            k = input("do you want to do anything else? y or n: ")
            print()
        if int(c) == 8:
            average_sal()
            k = input("do you want to do anything else? y or n: ")
            print()
        if int(c) == 9:
            pay_slip()
            ch = input('do you want to create more pay slips? y or n: ')
            if ch == 'y':
                while True:
                    if ch == 'n':
                        break
                    else:
                        pay_slip()
                        ch = input('do you want to create more pay slips? y or n: ')
            else:
                print()
            k = input("do you want to do anything else? y or n: ")
            print()
        if int(c) == 10:
            deleten()
            k = input("do you want to do anything else? y or n: ")
            print()
        if c == 11:
            create_table()
            k = input("do you want to do anything else? y or n:")
        if c == 12:
            show_tables()
            k = input("do you want to do anything else? y or n: ")

    except:
        print('\t\t\t\t*************please enter a valid choice************')
if k in 'nN':
    print('\t\t\t**************NICE INTERACTION WITH YOU****************')
    print('\t\t\t******************BYE FOR NOW ;-) *********************')
