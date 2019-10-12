import time
import threading
import runRoute
import os

numRuns = 1440 #Number of iterations in the main loop.  1440 minutes in a day



# waits until fresh minute to start the script
timeToStart = 60 - int(time.strftime('%S'))
print("Starting in " + str(timeToStart) + " seconds.")
while (time.strftime('%S') != "00"):
    time.sleep(1)

links = []
with open ("C:/Devtop/Routes/Routes.txt") as f:
    for line in f:
        links.append(line.split())

for route in links:
    th = threading.Thread(target=runRoute.runRoute, args=(route[0], route[1], numRuns, time.strftime('%S')))
    th.start()
    #runRoute.runRoute(route[0], route[1], numRuns)
    time.sleep(5)

th.join()
th.join()

os.system("shutdown -t 0 -r -f")