#process use multi cpu, separate memory space, GIL for on process , 
#dis-- heavy, slower than starting thread, more memory, ipc

'''
 facts:

A new process is started independently from the first process

Takes advantage of multiple CPUs and cores

Separate memory space

Memory is not shared between processes

One GIL (Global interpreter lock) for each process, i.e. avoids GIL limitation

Great for CPU-bound processing

Child processes are interruptable/killable

Starting a process is slower that starting a thread

Larger memory footprint

IPC (inter-process communication) is more complicated

Threads

A thread is an entity within a process that can be scheduled for execution (Also known as "leightweight process"). A Process can spawn multiple threads. The main difference is that all threads within a process share the same memory.

Key facts:

Multiple threads can be spawned within one process

Memory is shared between all threads

Starting a thread is faster than starting a process

Great for I/O-bound tasks

Leightweight - low memory footprint

One GIL for all threads, i.e. threads are limited by GIL

Multithreading has no effect for CPU-bound tasks due to the GIL

Not interruptible/killable -> be careful with memory leaks

increased potential for race conditions
'''


from multiprocessing import Process
import time
import os


def square_number():
    for i in range(100):
        i*i
        time.sleep(0.1)


processes=[]
num_processes=os.cpu_count()

#create processes

for i in range(num_processes):
    p=Process(target=square_number )
    processes.append(p)

#start
for p in processes:
    p.start()

#join
for p in processes:
    p.join()

    print('end main')