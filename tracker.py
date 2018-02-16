# Needs the pyicloud package, which you can get with pip install pyicloud. 
# afterwards, use the iCloud --username:"your icloud email" and type in your 
# password and have it be saved to your computer's "keyring", so that way 
# you don't have to hard code your password in like all the other poor souls
# also don't forget to import geopy, which converts coordinates to actual
# locations on a map 


from pyicloud import PyiCloudService
from geopy.geocoders import Nominatim
import datetime, time, csv, sys, os

api = PyiCloudService('apple email goes here')
geolocator = Nominatim()

def convertTime(timeStamps):
	'''
	Takes in the time stamp in the form apple supplies it from iCloud and returns 
	one that you and I can understand. 
	'''
	time_stamp = timeStamps / 1000
	time_now = time.time()
	time_delta = time_now - time_stamp 
	minutes, seconds = divmod(time_delta, 60) 
	hours, minutes = divmod(minutes, 60)
	time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime("%B %d %I:%M:%S")
	return time_stamp

def writeToCSV(information):
	'''
	This one takes in the dictionary of information 
	and writes it out to a file called (guess?) location.csv
	yeah whatever 
	'''
	
	fd = open("location.csv", "a")

	a = csv.writer(fd)
	data = ['Info', information['location'], information['time'], information['old'], information['battery']]
	a.writerow(data)
	fd.close()

for x in range(1,1440):
	'''
	This thing runs for an entire 24 hours, or more commonly knows as an entire 1440 minutes 
	Don't forget to use your actual device's ID
	google it. 
	'''
	data = api.devices['deviceID goes here'].location()
	status = api.devices['deviceID goes here'].status()

	return_string = {}
	return_string["location"] = geolocator.geocode(str(data[u'latitude']) + ", " + str(data['longitude'])).address
	return_string["time"] =  convertTime(data[u'timeStamp'])
	return_string["old"] = str(data['isOld'])
	return_string["battery"] = str(float(status["batteryLevel"]) * 100).split('.')[0]

	writeToCSV(return_string)
	print "Updated."
	time.sleep(60)
