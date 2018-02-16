from pyicloud import PyiCloudService
from geopy.geocoders import Nominatim
import datetime, time, csv, sys, os

api = PyiCloudService('apple email goes here')
geolocator = Nominatim()

def convertTime(timeStamps):
	time_stamp = timeStamps / 1000
	time_now = time.time()
	time_delta = time_now - time_stamp 
	minutes, seconds = divmod(time_delta, 60) 
	hours, minutes = divmod(minutes, 60)
	time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime("%B %d %I:%M:%S")
	return time_stamp

def writeToCSV(information):
	fd = open("location.csv", "a")

	a = csv.writer(fd)
	data = ['Info', information['location'], information['time'], information['old'], information['battery']]
	a.writerow(data)
	fd.close()

for x in range(1,20):
	data = api.devices['H4b0AH4TKSa/G0YQ3cU2SZJqwIVkeOK/wOfn1jE7JMI0i5YWspnG4+HYVNSUzmWV'].location()
	status = api.devices['H4b0AH4TKSa/G0YQ3cU2SZJqwIVkeOK/wOfn1jE7JMI0i5YWspnG4+HYVNSUzmWV'].status()

	return_string = {}
	return_string["location"] = geolocator.geocode(str(data[u'latitude']) + ", " + str(data['longitude'])).address
	return_string["time"] =  convertTime(data[u'timeStamp'])
	return_string["old"] = str(data['isOld'])
	return_string["battery"] = str(float(status["batteryLevel"]) * 100).split('.')[0]

	writeToCSV(return_string)
	print "Updated."
	time.sleep(30)