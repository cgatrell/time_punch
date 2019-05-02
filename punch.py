from datetime import datetime
import csv
import sys
import time

fileName = "spring2019_497RSheet1.csv"
seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

if len(sys.argv) != 2:
    print("Error\n usage: punch.py in/out")

if sys.argv[1].lower() == "in":
    with open(fileName, 'a', newline='') as fd:
        cur_time = time.time()
        now = datetime.now()
        list = []
        list.append(now.strftime("%m/%d/%Y"))
        list.append(now.strftime("%H:%M:%S"))
        fd.write(list[0])
        fd.write(',')
        fd.write(str(list[1]))
        fd.write(',')
        index_file = open("index.txt", 'w')
        index_file.write(str(cur_time))
        index_file.close()

        
if sys.argv[1].lower() == "out": 
    index_file = open("index.txt", 'r')
    start_string = index_file.readline()
    index_file.close()
    
    start_time = float(start_string)
    format = '%H:%M:%S'
    elapsed_time = time.time() - start_time

    hours = elapsed_time // seconds_in_hour
    elapsed_time -= (hours * seconds_in_hour)
    minutes = elapsed_time // seconds_in_minute
    elapsed_time -= (minutes * seconds_in_minute)

    time_worked = "{}:{}:{}".format(int(hours), int(minutes), int(elapsed_time))
    
    with open(fileName, 'a', newline='') as fd:
        now = datetime.now()
        list = []
        list.append(now.strftime("%H:%M:%S"))      
        fd.write(list[0])
        fd.write(',')
        fd.write(time_worked)
        fd.write(',,')
        fd.write('\n')
        fd.close()
