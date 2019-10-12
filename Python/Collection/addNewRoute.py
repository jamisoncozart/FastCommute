import os

print ("Enter the route name:")
routeName = str(input())

print ("Enter the route link:")
routeLink = str(input())

#write the new route to the text file
myfile = open ("Routes.txt", "a")
myfile.write(routeName + " " + routeLink + "\n")

#make a folder for the new route
if not os.path.exists(routeName):
    os.makedirs(routeName)

