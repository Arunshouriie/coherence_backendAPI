from users.models import *
from users.models import reminder_schedule_groups as schedule
import mysql.connector
import MySQLdb
from datetime import date, timedelta
from datetime import datetime
from twilio.rest import Client



def process_schedule():
    conn = mysql.connector.connect(host="localhost",user="root",password="password@123")
    sql = "select id as dispenseId, schedule_id as sId, dispense_time as dTime, concat(current_date(), ' ', TIME(alarms_start_time)) as start_time, concat(current_date(), ' ', TIME(alarms_end_time)) as end_time   from coherence.users_dispense where now() between concat(current_date(), ' ', TIME(alarms_start_time)) and concat(current_date(), ' ', TIME(alarms_end_time)) ;"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)

    for row in res:
        dispenseId = row["dispenseId"]
        schedule_id = row["sId"]
        dispenseTime = row["dTime"]
        start_time = row["start_time"]
        end_time = row["end_time"]
        print(dispenseId, schedule_id, dispenseTime, start_time, end_time)
        dt = datetime.now()
        schedule_audit_query = "select id, dispense_id, dispense_consumed, date_of_alarms, alarm_count from coherence.users_schedule_audit where dispense_id = " + str(dispenseId) + " and date_of_alarms > '" + str(datetime.combine(dt, datetime.min.time())) + "'"
        print(schedule_audit_query)
        cursor.execute(schedule_audit_query)
        mydata = cursor.fetchall()
        print(mydata)
        for sa in mydata:
            saId = sa["id"]
            dispId = sa["dispense_id"]
            consumed = sa["dispense_consumed"]
            date = sa["date_of_alarms"]
            alarm_count = sa["alarm_count"]
            print(saId, dispId, consumed, date, alarm_count)
            print(alarm_count)
            if consumed == 1:
                print("medicine is consumed")
            else:
                group = schedule.objects.filter(id=schedule_id)
                if not group:
                    print("no group was assigned to dispense")
                else:
                    for sched in group:
                        print(sched)
                        alarms_frequency = sched.time_range_between_alarms
                        print(alarms_frequency)
                        freq_list = alarms_frequency.split(",")
                        print(freq_list)
                        i = 0
                        j = 1
                        mins_to_next_alarm = 0
                        if alarm_count == sched.recurring:
                            print("all alarms sent to the device")
                        else:
                            for freq in freq_list:
                                if(i == alarm_count):
                                    break
                                mins_to_next_alarm = mins_to_next_alarm + int(freq_list[alarm_count - j])
                                i = i + 1
                                j = j + 1
                            print(mins_to_next_alarm)
                            print(type(start_time))
                            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
                            next_alarm_time = start_time + timedelta(minutes=int(mins_to_next_alarm))
                            print(next_alarm_time)
                            print(datetime.now())
                            if(datetime.now() >= next_alarm_time):
                                print("alarms will be sent here")
                                # alarms should send to the end device
                                
                                # alarm_count value in schedule_audit should updated
                                # alarm_audit record should create for the alarm


        

                           

                


