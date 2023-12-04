import mysql.connector as connector
from tabulate import tabulate

passwrd = "Sowmyar0208"
def CheckLogin(a,b):
        mycon = connector.connect(
            host = "localhost",
            user = "root",
            password = passwrd,
            database = "parkingsystem"
        )
        mycursor = mycon.cursor()
        mycursor.execute("SELECT * FROM admininfo")
        result = mycursor.fetchall()
        found = False
        for i in result:
            if i[0]==a and i[1]==b:
                found = True
        if found == True:
            return("Valid")
        else:
            return("In-Valid")

def AddLogin(usr,pas):
        mycon = connector.connect(
            host = "localhost",
            user = "root",
            password = passwrd,
            database = "parkingsystem"
        )
        mycursor = mycon.cursor() 
        cmd = "INSERT INTO admininfo (user, password) VALUES (%s,%s)"
        val = (usr,pas)
        mycursor.execute(cmd,val)
        mycon.commit() 

def CheckRecord(vn):
        mycon = connector.connect(
            host = "localhost",
            user = "root",
            password = passwrd,
            database = "parkingsystem"
        )
        status = "New-Vehicle"
        mycursor = mycon.cursor() 
        mycursor.execute("SELECT * FROM vehicleinfo")
        result = mycursor.fetchall() 
        for i in result:
            if i[0]==vn:
                status = "Existing-Vehicle"
        return(status)


def AddEntry(a,b,c,d,e):
        mycon = connector.connect(
            host = "localhost",
            user = "root",
            password = passwrd,
            database = "parkingsystem"
        )
        mycursor = mycon.cursor() 
        cmd = "INSERT INTO vehicleinfo (NumberPlate,EntryTime,ParkingSlot,Date,VehicleStatus) VALUES (%s,%s,%s,%s,%s)"
        val = (a,b,c,d,e)
        mycursor.execute(cmd,val)
        mycon.commit()

def GetRecord(vn):
    mycon = connector.connect(
        host = "localhost",
        user = "root",
        password = passwrd,
        database = "parkingsystem"
    )
    mycursor = mycon.cursor()
    cmd = "SELECT * FROM vehicleinfo WHERE NumberPlate  = %s"
    val = (vn,)
    mycursor.execute(cmd,val)
    result = mycursor.fetchall()
    return(result[0])

def UpdateRecord(a,b,vn):
    mycon = connector.connect(
        host = "localhost",
        user = "root",
        password = passwrd,
        database = "parkingsystem"
    )
    mycursor = mycon.cursor() 
    cmd = "UPDATE vehicleinfo SET ExitTime = %s, ParkingFee = %s, VehicleStatus = 'Exit' WHERE NumberPlate = %s"
    val = (a,b,vn)
    mycursor.execute(cmd,val)
    mycon.commit() 

def CheckAllRecords():
    mycon = connector.connect(
        host = "localhost",
        user = "root",
        password = passwrd,
        database = "parkingsystem"
    )
    mycursor = mycon.cursor() 
    mycursor.execute("SELECT * FROM vehicleinfo")
    result = mycursor.fetchall() 

    info = ["NumberPlate","EntryTime","ExitTIme","ParkingSlot","Date","ParkingFee","VehicleStatus"]
    np = list() 
    ent = list() 
    ext = list() 
    ps = list() 
    dt = list() 
    pf = list() 
    vs = list() 
    for i in result:
        np.append(i[0])
        ent.append(i[1])
        ext.append(i[2])
        ps.append(i[3])
        dt.append(i[4])
        pf.append(i[5])
        vs.append(i[6])
    table = zip(np,ent,ext,ps,dt,pf,vs)
    print("\n")
    print(tabulate(table,headers=info, floatfmt=".4f", tablefmt="fancy_grid"))

def VehicleInfo(vn):
    mycon = connector.connect(
        host = "localhost",
        user = "root",
        password = passwrd,
        database = "parkingsystem"
    )
    mycursor = mycon.cursor() 
    cmd = "SELECT * FROM vehicleinfo WHERE NumberPlate = %s"
    val = (vn,)
    mycursor.execute(cmd,val)

    result = mycursor.fetchall()[0]
    info = ["NumberPlate","EntryTime","ExitTIme","ParkingSlot","Date","ParkingFee","VehicleStatus"]
    
    print("--------------------------")
    for i in range(0,7):
        print(info[i]," : ",result[i])
    print("--------------------------")

#End