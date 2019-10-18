import time
import threading
import runRoute
import os

numRuns = 1440 #Number of iterations in the main loop.  1440 minutes in a day
links = []
threads = []

# waits until fresh minute to start the script
timeToStart = 60 - int(time.strftime('%S')) #finds out how many seconds until the next minute
print("Starting in " + str(timeToStart) + " seconds.")
while (time.strftime('%S') != "00"): #sleeps the program for 1 second until the next minute is reached
    time.sleep(1)

#Reads in routes.txt line for line, and splits each line into the name and link
with open ("C:/Devtop/Routes/Routes.txt") as f:
    for line in f:
        links.append(line.split())

#goes through each route that was added, starts it on a new thread by calling newRoute.newRoute(...)
#then wait 5 seconds before starting the next
for route in links:
    threads.append(threading.Thread(target=runRoute.runRoute, args=(route[0], route[1], numRuns, time.strftime('%S'))))
    threads[len(threads)-1].start()
    #runRoute.runRoute(route[0], route[1], numRuns)
    time.sleep(5)

#Waits for all of the threads to finish to continue (Will happen at 11:59 pm)
for thread in threads:
    thread.join()

#restarts the comp to start fresh for the next day, but gives the user 10 sec in case they want to stop it for debugging
print ("\n\nCollection complete\nSYSTEM WILL NOW SHUT DOWN")
time.sleep(10)
os.system("shutdown -t 0 -r -f")