import datetime
from datetime import date
from time import sleep


def GetTime():
        tm = str(datetime.datetime.now().strftime("%H:%M:%S"))
        return(tm)
def GetDate():
    dt = str(date.today())
    return(dt)
def FareCal(x,y):
    xlst = x.split(":")
    ylst = y.split(":")

    hr = int(ylst[0])-int(xlst[0])
    mn = (60-int(xlst[1])+int(ylst[1]))/60
    tf = int((hr+mn)*100)
    return(str(tf))
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



#End