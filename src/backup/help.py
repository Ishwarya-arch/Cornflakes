#- - - - - - - - - - - - - imports
from datetime import datetime
import pytz
import os
import milk
#- - - - - - - - - - - - - functions

def clockIn():
    current_time= capturecurrenttime()[2]
    message= "\n", current_time.strftime("%d %a %Y  "), "ClockIn, {}, ".format(current_time.strftime("%H:%M"))

    current_file= open(getfile(), 'a')
    current_file.writelines(message)
    current_file.close()

def clockOut():
    current_time= capturecurrenttime()[2]
    message= "ClockOut, {}\n\n".format(current_time.strftime("%H:%M"))

    current_file= open(getfile(), 'a')
    current_file.writelines(message)
    current_file.close()

def takeBreak():
    current_time= capturecurrenttime()[2]
    message= "takeBreak, {}, ".format(current_time.strftime("%H:%M"))

    current_file= open(getfile(), 'a')
    current_file.writelines(message)
    current_file.close()

def endBreak():
    current_time= capturecurrenttime()[2]
    message= "EndBreak, {}, ".format(current_time.strftime("%H:%M"))

    current_file= open(getfile(), 'a')
    current_file.writelines(message)
    current_file.close()


def askInput():
    userprompt= { '1': clockIn,
                  '2': clockOut,
                  '3': takeBreak,
                  '4': endBreak,
                  '5': "Exit"    }
    
    print("\nPlease select input")
    to_do= input(" > 1.Clock-In <  > 2.Clock-Out <   > 3.Take Break <   > 4.End Break <   > 5.Exit < ")
    
    if to_do in userprompt.keys():
        if to_do == '5':
            return
        else:
            userprompt[to_do]()
    else:
        print("Your input was invalid.")
        askInput()



def capturecurrenttime():
    #Capturing today's date and time in india and Germany
    timeStamp_IST = datetime.now() 
    timestamp_CET= datetime.now(pytz.timezone('Europe/Berlin'))
    #Capturing timestamp in floating point format
    ts = datetime.timestamp(timeStamp_IST)
    return ts, timeStamp_IST, timestamp_CET


def showstatus(file):
    print("\n\nStatus of : ", capturecurrenttime()[2].strftime("%d_%b_%Y_%a"))#include timestamp of the first clock-in
    print("\n\t\t Hello Kaushik!")
    print('\n Clock-in Time           :', capturecurrenttime()[2].strftime("%Hh:%Mm CET"))# display time of the first clock-in
    print(" Standard Working Hours  : 8Hrs")
    print(" Total work time elapsed :") #current timestamp-clock-in timestamp
    print(" Working hours left      :" ) # ((clock-in timestamp + 8hrs)-current timestamp)
    print(" Total Break-time taken  :")
    print("\n What would you like to do? ")


def getfile():
    filename = "dailyroutine.txt"
    directory = r"C:\Users\Ishwarya\Documents\GitHub\cornflakes"
    filepath = os.path.join(directory, filename)

    if not os.path.exists(filepath):
        dR= open(filepath,"x")
        dR.close()
    
    return filepath


def run():
    currentfile= getfile()
    showstatus(currentfile)
    askInput()
    print("***The End***")

#- - - - - - - - - - - - - Runscript
if __name__=="__main__":
    run()



