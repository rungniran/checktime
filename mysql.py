import pymysql
import datetime

con = pymysql.connect(host = "localhost", user = "root", password = "", db = "checktime" )
while (True) :
	times = datetime.datetime.now()
	mycursor = con.cursor()
	T = times.strftime("%H:%M:%S")
	day = times.strftime("%d")
	namemonth = times.strftime("%B")
	month = times.strftime("%m")
	year = times.strftime("%Y")
	time = times.strftime("%d/%m/%Y")
	print(time)
	name = input("name = ")
	numberPersonnel = input("numberPersonnel = ")
	val = (name, numberPersonnel)
	sql = "SELECT * FROM listpersonnel WHERE name = (%s) and numberPersonnel = (%s)"
	mycursor.execute(sql, val)
	row = mycursor.fetchall()
	result = mycursor.rowcount
	# print (result)
	if result == 1:
		idListPersonnel = row[0][0]
		val = (idListPersonnel, day, month, year)
		sql = "SELECT * FROM worktime WHERE idListPersonnel = (%s) and day = (%s) and month = (%s) and year = (%s)"
		mycursor.execute(sql, val)
		result = mycursor.rowcount
		if result == 0:
			val = (idListPersonnel, T, day, month, year)
			sql = "INSERT INTO worktime (idListPersonnel, T, day, month, year) VALUES (%s, %s, %s, %s, %s)"
			mycursor.execute(sql, val)
			con.commit()
			print(numberPersonnel + " " + name + " " + T )
			print("Success \n")
		else:
		    print("You make a list \n")	
	else:
		print("Not found name or numberPersonnel \n")
	