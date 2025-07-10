from threading import Thread
import os
import time

def square_number():
    for i in range(100):
        i*i
        time.sleep(0.1)

if __name__=="__main__":
    threads=[]
    num_threads=os.cpu_count()

#create processes

for i in range(num_threads):
    t=Thread(target=square_number )
    threads.append(t)

#start
for p in threads:
    p.start()

#join
for p in threads:
    p.join()

print('end main')