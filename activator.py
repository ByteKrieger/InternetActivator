import time
from pythonping import ping
import pysimplegui as sg



def startping():
    ping('8.8.8.8', verbose=True, count=4 , interval=1)

    startping()
    time.sleep(5)

print("Ende")
time.sleep(5)