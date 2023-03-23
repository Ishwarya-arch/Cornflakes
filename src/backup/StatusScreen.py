'''#Keys:
currt_dt = current date and time
currt_gmy = current time and date in germany 
ts = timestamp (float number)
'''

#- - - - - - - - - - - - - imports
from datetime import datetime
import pytz
import os



#- - - - - - - - - - - - - functions
def capturecurrenttime():
    #Capturing today's date and time in india and Germany
    currt_dt = datetime.now() 
    currt_dtgmy= datetime.now(pytz.timezone('Europe/Berlin'))
    #Capturing timestamp in floating point format
    ts = datetime.timestamp(currt_dt)
    return currt_dt, currt_dtgmy, ts


def dailyRoutine():
    if os.path.exists(r"C:\Users\thekaushikls\Documents\dailyRoutine.txt"):
        #check here if the log for that day is over.
        return True
        
    else:
        dR= open("dailyRoutine.txt","a")
        dR.write("Date\t\tTime(IST)\t\tTime(CET)\t\tTimeStamp ")
        a,b,c= capturecurrenttime()
        dR.write("\n{}\t{}\t{}\t".format(a,b,c))
        dR.close()


def askUser():
    #prompt from the user
    to_do= input(" > 1.Clock-In <  > 2.Clock-Out <   > 3.Take Break <   > 4.End Break <   > 5.Exit < ")
    return userprompt[to_do]()


def clockIn():
    #dR= open("dailyRoutine.txt", "r")
    a,b,c= capturecurrenttime()
    ci= open('dailyRoutine.txt','a')
    ci.write("\n{}\t{}\t".format(a,b))
    return c

def clockOut():

    a,b,c= capturecurrenttime()
    ci= open('dailyRoutine.txt','a')
    ci.write("\n{}\t{}\t".format(a,b))
    return c

def takeBreak():
    a,b,c= capturecurrenttime()
    ci= open('dailyRoutine.txt','a')
    ci.write("\n{}\t{}\t".format(a,b))
    return c

def endBreak():
    a,b,c= capturecurrenttime()
    ci= open('dailyRoutine.txt','a')
    ci.write("\n{}\t{}\t".format(a,b))
    return c



#- - - - - - - - - - - - - declarations
userprompt= { 1: clockIn,
              2: clockOut,
              3: takeBreak,
              4: endBreak,
              5: "Exit"}

timestampList=[]



if __name__=="__main__":
    #default status screen: 
    print("\n\nStatus of : ", capturecurrenttime().strftime("%d_%b_%Y_%a"))#include timestamp of the first clock-in
    print("\n\t\t Hello Kaushik!")
    print('\n Clock-in Time           :', capturecurrenttime().strftime("%HHrs:%MmIST"))# display time of the first clock-in
    print(" Standard Working Hours  : 8Hrs")
    print(" Total work time elapsed :") #current timestamp-clock-in timestamp
    print(" Working hours left      :" ) # ((clock-in timestamp + 8hrs)-current timestamp)
    print(" Total Break-time taken  :")
    print("\n What would you like to do? ")
    askUser()


input()

