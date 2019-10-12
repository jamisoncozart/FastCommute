from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from pyautogui import press, typewrite
from time import sleep
import time
import re
import json

def runRoute(routeName, routeLink, numRuns, offset):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(50,50)
    driver.minimize_window()
    driver.get(routeLink)
    data = [[time.strftime('%Y:%m:%d'), routeLink]]
    fileOutput = "C:/Devtop/Routes/" + routeName + "/" + time.strftime('%Y-%m-%d-%H-%M') + " "# + str(numIt)
    print(routeName + " beginning data collection for " + time.strftime('%A'))

    #put a bigger 1-24h loop around this one that takes time.time() at beginning and reloops every 24*60*60 seconds
    for a in range(0,numRuns):
        if (time.strftime('%H:%M') == "23:59"):
            break
        if (a % 180 == 0 and a != 0): #Prints to command prompt every 30 minutes to let me know it's still running
            print ("script is running " + time.strftime('%H:%M:%S'))

        driver.refresh()
        sleep(5)

        src = driver.page_source
        tTime = re.findall(r'.(id=\"section-directions-trip-0\")?>(([\d]+) h ([\d]+) min|([\d]+) min)', src)
        sleep(1)
        tTime = tTime[0][1]
        #print (tTime)

        totalMin = 0
        if (" h " in tTime):
            totalMin = int(tTime[0]) * 60 + int(tTime[4:6])
        elif (len(tTime) is 6 or len(tTime) is 5):
            totalMin = int(tTime[0:2])
        else: #if something weird happens like a road is closed or a multi day route is picked no data is collected
            totalMin = 0

        data.append([time.strftime('%H:%M:%S'), totalMin])
        #print (str(totalMin) + " minutes.")
        #print(time.strftime('%S'))
        while (time.strftime('%S') != offset):
            sleep(1)

    driver.close()
    data.append([time.strftime('%Y:%m:%d'), str(len(data)-2)])

    fileOutput += str(len(data) - 2 )
    #print("Saving file to: " + fileOutput)
    with open(fileOutput, 'w') as f:
        json.dump(data, f)