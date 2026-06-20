'''
join():mainthread --> owner
        worker thread --> worker
'''
import threading
import time
def task():
    time.sleep(3)
    print("Thread Finished")

t = threading.Thread(target=task)
t.start()
t.join()
print("Main thread ends here")

#Multiple threads with join
def task(name):
    print(name,"started")
    time.sleep(2)
    print(name,"Finished")

t1 = threading.Thread(target=task,args=("A"))
t2 = threading.Thread(target=task,args=("B"))

t1.start()
t2.start()
t1.join()
t2.join()
print("All threads completed")

#Example on naming threads
def task():
    print(threading.current_thread().name,"Started")
    time.sleep(2)
    print(threading.current_thread().name,"Finished")

t1 = threading.Thread(target=task,name="download thread")
t2 = threading.Thread(target=task,name="Upload thread")
t1.start()
t2.start()