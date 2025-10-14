import threading
import time
import random

#   function 1:  reading patient sensor data
def read_sensor_data():
    for i in range(5):
        heart_rate = random.randint(60,120)
        temperature = round(random.uniform(36.5, 39.0),1)
        print("f[sensor] reading {i+1}: heart_rate = {heart_rate} bpm, temp = {temperature} c")
        time.sleep(3)

#----function2 :  sending doctor notification-----
def notify_doctor():
    for i in range(3):
        print(f"[notification] docttor notified about patient condition {i+1}")
        time.sleep(3)

#-----function 3: logging data-----
def logging_data():
    for i in range(4):
        print(f"[logger] data saved in system log {i+1}")
        time.sleep(2.5)


#----creating threads--------
t1 = threading.Thread(target=read_sensor_data)
t2 = threading.Thread(target=notify_doctor)
t3 = threading.Thread(target=logging_data)

#------start thread-------
t1.start()
t2.start()
t3.start()

#-------wait until all threads are done---------
t1.join()
t2.join()
t3.join()

print("\nAll hospital monitoring task completed")