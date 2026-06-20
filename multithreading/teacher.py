import threading
import time

def student(name):
    print(name,"started exam")
    time.sleep(3)
    print(name,"Submitted paper")

t1 = threading.Thread(target=student,args=("Anas",),name="Student-1")
t2 = threading.Thread(target=student,args=("Akhil",),name="Student-2")

t1.start()
t2.start()

t1.join()
t2.join()
print("Teacher collected all papers")