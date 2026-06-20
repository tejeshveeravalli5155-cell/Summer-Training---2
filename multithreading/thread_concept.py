# '''
# what is a program?
# A program is a set of instructions stored on a disk

# print("hello")

# storing on a disk???

# what is process?
# when a program starts execuiting it becomes a process

# running?
# python hello.py
# hello

# OS --Operating System

# Chrome:
# VS code:
# Spotify:
# each one is a separate process

# Characteristics:
# 1.Independent
# 2.Separate memory
# 3.Heavy a weight : Due to memory allocations,resource allocation,cpu scheduling

# What is a thread?
# A thread is smallest unit of execution inside a process

# Process                     Thread
# 1.Independent               Part of process
# 2.Heavy weight              Light weight
# 3.Separate memory           Shared memory
# 4.Slow                      Fast
# 5.Expensive                 Cheap
# 6.Communication difficult   Easy

# Why threads are fast?
# Threads will share memory
# Process needs separate memory allocation

# Concurrency?
# Teacher checking the notebooks
# student A
# student B
# student C

# coccurrency?
# A
# B
# C
# A
# B
# C

# one at a time
# rapidly switching
# appears simultaneously
# CPU --> only one

# Parallelism:
# cashier 1 --> customer 1
# cashier 2 --> customer 2
# cashier 3 --> customer 3

# truly simultaneous

# Python threads will use ---Concurrency
# due to GIL -Global interpreter lock

# '''
# #Creation of threads:
# import threading

# #Function created(do's nothing)
# def display():
#     print("Hello")
# #Thread object(creation)
# t = threading.Thread(target=display)
# #start thread
# t.start()

# #multiple threads:
# import threading

# def task():
#     print("Thread running")

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)
# t3 = threading.Thread(target=task)

# t1.start()
# t2.start()
# t3.start()

# '''
# Main Thread
#     +   t1
#     +   t2
#     +   t3

#     all execuites independently

# '''
# #Threads with loops:

# def numbers():
#     for i in range(5):
#         print(i)
# t = threading.Thread(target=numbers)
# t.start()

# #Two Threads with different task
# def even():
#     for i in range(0,10,2):
#         print("Even:",i)
# def odd():
#     for i in range(1,10,2):
#         print("odd:",i)

# t1 = threading.Thread(target=even)
# t2 = threading.Thread(target=odd)

# t1.start()
# t2.start()

'''
os scheduler will decides:
which thread to runs first?
'''
import threading 
print(threading.current_thread())

#Nmaing of threads
import threading

def task():
    print(threading.current_thread().name)

t = threading.Thread(target=task,name="Student_Thread")
t.start()

#Passing parameters
def square(n):
    print(n*n)

t = threading.Thread(target=square,args=(5,))
t.start()

#to delay the threads
import time

print("start")
time.sleep(3)
print("end")

import threading
import time

def task():
    for i in range(5):
        print(i)
        time.sleep(1)
t = threading.Thread(target=task)
t.start()


# Retry mechanism
# while True:
#     try:
#         connect()
#     except:
#         time.sleep(5)


