import pythonping
import time
def startping():
    pythonping.ping('8.8.8.8', verbose=True, count=4 , interval=1)

try:
    while True:
        startping()
        time.sleep(60)
except KeyboardInterrupt:
    print("InternetActivator wird geschlossen...")
    time.sleep(5)

