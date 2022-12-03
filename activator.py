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

# Muss noch irgendwie bearbeitet werden, damit es nicht so lange dauert bis es beendet wird.

