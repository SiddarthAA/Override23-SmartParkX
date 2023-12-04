import csv

def ShowSlots():
    fh = open("Slots.csv")
    r = csv.reader(fh)
    print("\nParking Slots")
    print("------------------------------------------------")
    for i in r:
        
            print("     ".join(i))
    print("------------------------------------------------")

def AssignSlot(vn):
    fh = open("Slots.csv","r+")
    r,w = csv.reader(fh), csv.writer(fh)
    slots = list() 
    for i in r:
        if i != []:
            slots.append(i)
    
    slot = None
    for i in slots:
        ind1 = slots.index(i)
        for j in i:
            ind2 = i.index(j)
            spc = j.split("-")
            if spc[1]=="Empty":
                slot = str(spc[0])
                replc = str(spc[0])+"-"+str(vn)
                slots[ind1][ind2] = replc
                fh.seek(0)
                for x in slots:
                    w.writerow(x)
                fh.close()
                return(slot)


def ClearSlot(sl):
    fh = open("Slots.csv","r+")
    r,w = csv.reader(fh), csv.writer(fh)
    slots = list() 
    for i in r:
        if i != []:
            slots.append(i)
    
    for i in slots:
        ind1 = slots.index(i)
        for j in i:
            ind2 = i.index(j)
            spc = j.split("-")
            if spc[0]==str(sl):
                replc = str(sl+'-Empty')
                slots[ind1][ind2]=replc
                fh.seek(0)
                for x in slots:
                    w.writerow(x)
                fh.close()

def SearchVehicle(vn):
    fh = open("Slots.csv")
    r = csv.reader(fh)
    slots = list() 
    for i in r:
        if i != []:
            slots.append(i)
    found = None
    for i in slots:
        for j in i:
            spc = j.split("-")
            if spc[1]==str(vn):
                found = spc[0]
    if found == None:
        return(False)
    else:
        return(found)
#End

