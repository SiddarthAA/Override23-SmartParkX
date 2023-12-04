from Computer_Vision import * 
from Slots import * 
from Database import * 
from Misc import * 
import getpass

def P1():
    while True:
        print("\n")
        print("~~~~~~~~~~Initializing~~~~~~~~~~")
        sleep(0.5)
        print("\nEnter Your Login Credentials To Access The Admin Program ")
        
        usr = input("Enter UserID : ")
        psw = getpass.getpass("Enter Password : ")
        sleep(1)
        if CheckLogin(usr,psw) == "In-Valid":
            print("\n")
            print("In-Valid Login Credentials")
            inp = input("Enter Again ? (Enter EXIT To Leave The Program) : ")
            if inp == "EXIT":
                print("\n")
                print("Exiting")
                return("Not-Verified")
                
        elif CheckLogin(usr,psw) == "Valid":
            print("\n")
            print("Valid Credentials")
            sleep(0.5)
            print("Loggin In")
            AsciArt()
            return("Verified")

access = P1()
if access == "Verified":
    flag = "Yes"
    while flag == "Yes":
        print("\nMenu:")
        print("1] Vehicle Scanning ")
        print("2] Parking Slots ")
        print("3] Database / Vehicle Info ")
        print("4] To Exit The Program")

        opt = int(input("\nEnter Option Number : "))
        if opt == 1:
            flag1 = "Yes"
            while flag1=="Yes":
                numplt =  GetNumberPlate()
                if numplt == None:
                    print("---------------------")
                    print("|No Vehicles Scanned|")
                    print("---------------------")
                else:

                    check = CheckRecord(numplt)

                    if (check.split("-"))[0]=="New":
                        EntTime = str(GetTime())
                        Date = str(GetDate())
                        Slot = str(AssignSlot(numplt))
                        Status = "Entry"
                        AddEntry(numplt,EntTime,Slot,Date,Status)
                        print("\n------------------------")
                        print("|Vehicle Record Updated|")
                        print("------------------------")
                        print("|Park The Vehicle At Slot |",Slot)
                        print("------------------------")
                    elif (check.split("-"))[0]=="Existing":
                        info = GetRecord(numplt)
                        np = info[0]
                        EntTime = info[1]       
                        ExtTime = GetTime()
                        slot = info[3]
                        Fare = FareCal(EntTime,ExtTime)
                        UpdateRecord(ExtTime,Fare,np)
                        ClearSlot(slot)
                        print("\n")
                        print("Thank You For Visiting")
                        print("|--------------------------|")
                        print("|Total Payable Fee : ",Fare,"|")
                        print("|--------------------------|")
                flag1 = input("\nEnter Yes To Scan More Vehicles / EXIT To Return To main Menu : ")

        elif opt == 2:
            flag2 = "Yes"
            while flag2=="Yes":
                print("\n----------------------")
                print("Menu: ")
                print("1]Check Parking Space")
                print("2]Check Vehicle Slot")
                print("------------------------")
                opt = int(input("\nEnter Option Number : "))
                if opt == 1: 
                    ShowSlots() 
                elif opt == 2: 
                    np = input("Enter Vehicle NumberPlate : ")
                    slt = SearchVehicle(np)
                    print("Vehicle Parked In Slot |",slt,"|")
                flag2 = input("\nEnter Yes To Go To Slots / EXIT To Return To main Menu : ")
                
        elif opt == 3: 
            flag3 = "Yes"
            while flag3=="Yes":
                print("\n")
                print("Menu : ")
                print("1] Check Database Entries")
                print("2] Check Vehicle Info")
                print("3] Add New Logins")
                opt = int(input("\nEnter Option Number : "))
                if opt == 1: 
                    CheckAllRecords()
                elif opt == 2:
                    np = str(input("\nEnter NumberPlate : "))
                    print("\nVEHICLE INFO")
                    VehicleInfo(np)
                elif opt == 3: 
                    print("------------------")
                    usr = input("Enter UserName : ")
                    pas = input("Enter Password : ")
                    print("------------------")
                    AddLogin(usr,pas)
                    sleep(0.5)
                    print("New Logins Added")
                flag3 = input("\nEnter Yes To Go To Database or EXIT To Go To Main Menu : ")
        
        elif opt == 4:
            print("Exiting")
            sleep(0.5)
            break
#End Of Code 