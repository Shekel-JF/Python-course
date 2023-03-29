from datetime import datetime
import time
while(1):
    now = datetime.now()
    now.strftime("%HH:%MM:%SS")
    print(str('%02d' %now.hour) + ":" + str('%02d' %now.minute) + ":" + str('%02d' %now.second), end='\r')
    time.sleep(0.333)