#this script will use the mysql.connector library to interact with a local database
import mysql.connector

#method for connecting to local host database
def dataPrint(dataUsername,dataPasswd,dataTable):
	mydb=mysql.connector.connect(
	host="localhost",
	user=dataUsername,
	passwd=dataPasswd           )


	dataCursor=mydb.cursor()
	dataCursor.execute("Select * from " + dataTable +";") 
	for d in dataCursor:
		for a in d:
			print(" ")
			print(a)

dataPrint("waagh","Norest2019","prices.models")
