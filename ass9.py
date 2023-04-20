import mysql.connector
tea19python = mysql.connector.connect(host="localhost",user="root",password="manager",database="TEA19")
mycursor = tea19python.cursor()
def display():
	mycursor.execute("SELECT * FROM employees")
	for i in mycursor:
		print(i) 
def insertemp():
	empid = int(input("Enter the employee id : "))
	name = input("Enter the name of employee : ")
	salary = int(input("Enter the salary of employee : "))
	sql = "INSERT INTO employees (empid, name, salary) VALUES (%s, %s, %s)"
	values = (empid, name, salary)
	mycursor.execute(sql, values)
	print("Employee record inserted successfully!")
def deleteemp():
	empid = int(input("Enter the employee id : "))
	sql = "DELETE FROM employees WHERE empid=%s"
	values = [empid]
	mycursor.execute(sql, values)
	print("Employee record deleted successfully!")
def salaryemp():
	mycursor.execute("SELECT * FROM employees WHERE salary>50000")
	for i in mycursor:
		print(i) 
def displayemp():
	empid=int(input("Enter the employee id : "))
	sql = "SELECT * FROM employees WHERE empid=%s"
	values=[empid]
	mycursor.execute(sql, values)
	for i in mycursor:
		print(i) 
def createtable():
	mycursor.execute("CREATE TABLE employees (empid int, name VARCHAR(255), salary int)") 
def showtable():
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x) 
def menu():
	print("-----ASS 9 : DATABASE CONNECTIVITY-----")
	print("1. Insert Table Employees")
	print("2. Display Tables in Database")
	print("3. Insert Employee Details")
	print("4. Delete Employee Details")
	print("5. Display Employee Details")
	print("6. Display Employee Details having Salary more than 50,000")
	print("7. Display Specific Employee")
	print("8. Exit")

def main():
	choice = 0
	while(choice<9):
		menu()
		print("Enter your choice : ")
		choice = int(input())
		if(choice == 1):
			createtable()
		elif(choice == 2):
			showtable()
		elif(choice == 3):
			insertemp()
		elif(choice == 4):
			deleteemp()
		elif(choice == 5):
			display()
		elif(choice == 6):
			salaryemp()
		elif(choice == 7):
			displayemp()
		elif(choice == 8):
			exit()
		else:
			print("Enter valid choice.")
	exit()
main()