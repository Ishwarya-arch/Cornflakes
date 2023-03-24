

#- - - - - - - - - - - - - imports
from datetime import datetime
import pytz
import os

#- - - - - - - - - - - - - class
class day:


    data = {
            "StartTimeStamp" : 0,
            "Date" : 0,
            "StartTime" : 0,
            "BreakDuration" : 0,
            "EndTime" : 0,
            "WorkDuration": 0,
            }

    TIME_FORMAT = r"%d_%b_%Y__%H_%M"
    status=0
    

    def capturecurrenttime(self):
        #Capturing today's date and time in india
        self.current_time = datetime.now() 
        #Capturing timestamp in floating point format
        self.timestamp = datetime.timestamp(self.current_time)
        return self.current_time, self.timestamp


    def __init__(self):
        self.pause_time=[]
        self.resume_time=[]
        a,b= self.capturecurrenttime()
        self.status= 0


    def start_day(self):
        if self.status == 1:
            self.start_time= self.current_time
            self.start_timestamp= self.timestamp


    def pause_day(self):
        if self.status==1:
           self.pause_time.append(self.current_time)


    def resume_day(self):
        if self.status==2:
            self.resume_time.append(self.current_time)



    def end_day(self):
        if self.status==0:
            self.end_time= self.current_time
            self.end_timestamp= self.timestamp



    def get_break_duration(self):
        self.break_duration_list=[]
        for i in range(len(self.pause_time)):
            duration= self.resume_time[i]-self.pause_time[i]
            self.break_duration_list.append(duration)
        self.total_break_duration = sum(self.break_duration_list) 



    def get_work_duration(self):
        self.work_duration= (self.end_timestamp-self.start_timestamp) - self.total_break_duration
        return(self.work_duration.strftime("%H_%M"))
        

     
