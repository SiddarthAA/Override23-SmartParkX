"Modules"
import mysql.connector as connector
import csv
from time import sleep
import getpass


passwrd = "Sowmyar0208"

class SetupDB():
    def CreateDatabase():
        mycon = connector.connect(
            host = "localhost",
            user = "root",
            password = passwrd
        )
        mycursor = mycon.cursor() 
        mycursor.execute("CREATE DATABASE PARKINGSYSTEM")

    def CreateTable1():
        mycon = connector.connect(
            host = "localhost",
            user = "root",
            password = passwrd,
            database = "parkingsystem"
        )
        mycursor = mycon.cursor() 
        mycursor.execute("CREATE TABLE VEHICLEINFO (NumberPlate VARCHAR(13),EntryTime VARCHAR(8), ExitTime VARCHAR(8), ParkingSlot VARCHAR(2), Date DATE, ParkingFee VARCHAR(5), VehicleStatus VARCHAR(10))")
        
    def CreateTabl2():
        mycon = connector.connect(
            host = "localhost",
            user = "root",
            password = passwrd,
            database = "parkingsystem"
        )
        mycursor = mycon.cursor()
        mycursor.execute("CREATE TABLE ADMININFO (user varchar(15),password varchar(15))")

class AdminLogin():
    def AddAdmin():
        user = input("\nEnter Admin UserName : ")
        pswd = getpass.getpass("Enter Admin Password : ")
        mycon = connector.connect(
            host = "localhost",
            user = "root",
            password = passwrd,
            database = "parkingsystem"
        )
        mycursor = mycon.cursor() 
        cmd = "INSERT INTO admininfo (user, password) VALUES (%s,%s)"
        val = (user,pswd)
        mycursor.execute(cmd,val)
        mycon.commit() 

class Slots():
    def CreateSlots():
        fh = open("Slots.csv","w+")
        r,c = int(input("\nEnter No Of Rows : ")), int(input("Enter Number Of Columns : "))
        writer = csv.writer(fh)
        alp =" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        x = list()
        for i in range(1,r+1):
            temp= list()
            for j in range(1,c+1):
                temp.append(str(alp[i])+str(j)+"-Empty")
            x.append(temp)
        writer.writerows(x)

def AsciArt():
    print("""10%
███▒▒▒▒▒▒▒
    """)
    sleep(0.5)
    print("""50%
███████▒▒▒
    """)
    sleep(0.5)
    print("""100%
██████████
    """)
print("""
--------------------------------
|Setting Up Program Environment|
--------------------------------
""")
sleep(5)

print("----------SetUp 1----------")
print("Setting Up Databases")
AsciArt()

SetupDB.CreateDatabase()
SetupDB.CreateTable1()
SetupDB.CreateTabl2() 

print("Completed Setting Up Databases")

print("\n")
print("----------SetUp 2----------")
print("Setting Up Slots")
Slots.CreateSlots()
AsciArt()
print("Completed Setting Up Slots")

print("\n")
print("----------SetUp 3----------")
print("Setting Up Admin-Login")
AdminLogin.AddAdmin()
AsciArt()
print("Completed Setting Up Login")

print("\n")
print("-----SetUp Completed-----")
print("-----Run MainProgram-----")  