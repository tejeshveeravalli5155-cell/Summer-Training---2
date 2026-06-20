'''
1.Race Condition
2.Synchronization
3.Lock
4.RLock
'''
'''
#why we need synchronization?
Synchronization:
This is the process of controlling access to shared resources so that only one thread modifies at a time

Lock:
Shared resourcers: any variable,file,database,object

Example:

count=0
if multiple threads modifies count simultaneously

#Race Condition:
occurs when multiple threads access and modify shared data simultaneously causing unpredictable outputs
'''
count = 0
count += 1
print(count)

#Write with threads
import threading
count = 0
def increment():
    global count
    count += 1
threads = []
for i in range(1000):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()
   
for t in threads:
    t.join()
print(count)

'''
critical section:
code section where shared resources are accessed is called critical section
count +=1--->critical section

To avoid race condition?
one thread should enter crirical section

solution: Lock

What is a lock?
it was a synchronization mechanism that  allow only one thread to execute a critical section at a time

Thread A acquires Lock
other threads will wait
Thread A releases Lock
next thread gets lock

import threading
lock =threading.lock()

#to apply lock
lock.acquire()

#to release
lock.release()

'''
import threading
count = 0
lock = threading.Lock()

def increment():
    global count
    for i in range(10000):
        with lock:
            #critical section
            count += 1
        
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(count)


import threading
class Bank:
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()
    def withdrawl(self,amount):
        with lock:
            if self.balance >= amount:
                self.balance -= amount
                print(amount,"withdrawn")
            else:
                print("Insufficient Balance!")

bank = Bank()
t1 = threading.Thread(target=bank.withdrawl,args=(700,))
t2 = threading.Thread(target=bank.withdrawl,args=(500,))

t1.start()
t2.start()

t1.join()
t2.join()
print(bank.balance)


'''
Deadlock:
Where the threads wait forever forb locks
Thread 1
Lock A
waiting for Lock B

Thread 2 
Lock B
waiting for Lock A

Thread 1 -->waiting Lock A
Thread 2 -->waiting Lock B
Deadlock

RLock:Recursive lock
A thread can acquire the same lock multiple times

Why RLock:
normal lock
acquire once
releases once

if same thread aquires again 
deadlock
'''
import threading
lock = threading.RLock()

def outer():
    lock.acquire()
    inner()
    lock.release()
def inner():
    lock.acquire()
    print("Inner")
    lock.release()
outer()