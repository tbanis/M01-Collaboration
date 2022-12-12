import multiprocessing
import os
import time
import random

def curTime():
    print(time.ctime())

def randTime():
    print(random.random())

if __name__ == "__main__":
    p = multiprocessing.Process(target=curTime)
    p2 = multiprocessing.Process(target=randTime)
    p.start()
    p2.start()
    time.sleep(5)
    p.terminate()
    p2.terminate()