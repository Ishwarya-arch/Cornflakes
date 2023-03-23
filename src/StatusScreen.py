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

def askUser():
    #prompt from the user
    to_do= input(" > 1.Clock-In <  > 2.Clock-Out <   > 3.Take Break <   > 4.End Break <   > 5.Exit < ")
    userprompt[to_do]() #call function here using the key as parameter.

def capturecurrenttime():
    #Capturing today's date and time in india and Germany
    currt_dt = datetime.now() 
    currt_dtgmy= datetime.now(pytz.timezone('Europe/Berlin'))
    #Capturing timestamp in floating point format
    ts = datetime.timestamp(currt_dt)
    return currt_dt

def clockIn():
    #check if a file for the date does not exist. if it doesnt, create file and append time.
    # if file exist: prompt user to select clockout/take a break.

    if os.path.exists('file_path'):
        p= input("You have already ClockedIn. Please select a different prompt :")
        askUser()

    else:
        open('file_path','w')
        capturecurrenttime()


#- - - - - - - - - - - - - declarations
userprompt= { 1: clockIn,
              2: "clockOut",
              3: "takeBreak",
              4: "endBreak",
              5: "Exit"}

timestampList=[]



if __name__=="__main__":
    #default status screen: 
    print("\n\nStatus of : ", capturecurrenttime().strftime("%d_%b_%Y_%a"))#include timestamp of the first clock-in
    print("\n\t\t Hello Kaushik!")
    print('\n Clock-in Time           :', capturecurrenttime().strftime("%HHrs_%Mm_%Ss"))# display time of the first clock-in
    print(" Standard Working Hours  : 8Hrs")
    print(" Total work time elapsed :") #current timestamp-clock-in timestamp
    print(" Working hours left      :" ) # ((clock-in timestamp + 8hrs)-current timestamp)
    print(" Total Break-time taken  :")
    print("\n What would you like to do? ")
    askUser()



input()