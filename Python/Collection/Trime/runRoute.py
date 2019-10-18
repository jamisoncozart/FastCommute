from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from pyautogui import press, typewrite
from time import sleep
import time
import re
import json

#Starts a new chrome page and runs a route based off of passed in parameters
def runRoute(routeName, routeLink, numRuns, offset):
    #start the chrome page
    #options = webdriver.ChromeOptions()
    #options.add_argument('--ignore-certificate-errors')
    #options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome()#chrome_options=options)
    driver.set_window_size(50,50)
    driver.minimize_window()
    driver.get(routeLink)

    #set the first element of the data output array to the current time and the link for the route
    data = [[time.strftime('%Y:%m:%d'), routeLink]]
    #Set the path to save the file later
    fileOutput = "C:/Devtop/Routes/" + routeName + "/" + time.strftime('%Y-%m-%d-%H-%M') + " "
    print(routeName + " beginning data collection for " + time.strftime('%A'))

    #Runs a loop every minute numRuns of times (1440 = 24 hours) or until 11:59 pm
    for a in range(0,numRuns):
        #break if it's the end of the day
        if (time.strftime('%H:%M') == "23:59"):
            break
        if (a % 60 == 0 and a != 0): #Prints to command prompt every hour to let me know it's still running
            print ("script is running " + time.strftime('%H:%M:%S'))

        #Refresh the chrome page and wait 5 sec to make sure it has loaded again
        driver.refresh()
        sleep(5)

        #Get all of the code for the page after it's loaded and find the travel time from it
        src = driver.page_source
        tTime = re.findall(r'.(id=\"section-directions-trip-0\")?>(([\d]+) h ([\d]+) min|([\d]+) min)', src)
        sleep(1)
        tTime = tTime[0][1]
        #print (tTime)

        #caclulate the number of minutes in the route from the travel time string pulled from the page code
        totalMin = 0
        if (" h " in tTime):
            totalMin = int(tTime[0]) * 60 + int(tTime[4:6])
        elif (len(tTime) is 6 or len(tTime) is 5):
            totalMin = int(tTime[0:2])
        else: #if something weird happens like a road is closed or a multi day route is picked no data is collected
            totalMin = 0

        #Add the time that was found (in minutes) to the data output array, and wait until the next minute
        data.append([time.strftime('%H:%M:%S'), totalMin])
        while (time.strftime('%S') != offset):
            sleep(1)

    #Oncce the loop has finished, close chrome and add the time and amount of minutes ran to the data ouput array
    driver.close()
    data.append([time.strftime('%Y:%m:%d'), str(len(data)-2)])

    #Add the number of times the loop ran (number of minutes the program collected data) to data ouput array
    #And save the file to the fileOutput created earlier
    fileOutput += str(len(data) - 2 )
    #print("Saving file to: " + fileOutput)
    with open(fileOutput, 'w') as f:
        json.dump(data, f)