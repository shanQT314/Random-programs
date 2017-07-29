
import urllib2
import urllib
import sys
import json
import os
from pprint import pprint
import datetime
import csv

'''
Todo: 
- Create the CSV file if its not there
- Produce errors if the values entered don't match
'''



#messages to print out 
ErrorInAPI = "Error when making API call that I couldn't handle"


#Authentication codes to get this to work 
OAuthTwoClientID = "lolololol"
ClientOrConsumerSecret = "ok"

#Declares variables so that we can add them later
AccessToken = ""
RefreshToken = ""



def writeToCSV(startSleep, endSleep):
	'''
	Takes datetime objects for both when sleep started, and when 
	it ended, and then appends it to a CSV file in the directory
	of the python file 
	'''

	#Converts the text arguments into dateTime objects
	startObject = datetime.datetime.strptime(startSleep, "%Y-%m-%dT%H:%M:%S.000")
	endObject = datetime.datetime.strptime(endSleep, "%Y-%m-%dT%H:%M:%S.000")

	#Strips the dateTime object's date values only, and converts them to strings
	startDate = datetime.datetime.strftime(startObject, '%d/%m/%Y')
	endDate = datetime.datetime.strftime(endObject, '%d/%m/%Y')

	#Strips the dateTime obejct's time values only, and changes them to strings
	startTime = datetime.datetime.strftime(startObject, '%I:%M %p')
	endTime = datetime.datetime.strftime(endObject, '%I:%M %p')


	#Opens a csv files in the directory and the values to it

	with open(r'dates.csv', 'a') as fd:
		a = csv.writer(fd);
		data = ['Sleep', startDate, startTime, endDate,endTime];
		a.writerow(data);


def GetTokens():
  '''
  Gets the authorization tokens from a tokens.txt file
  in the same directory as the actual file
  returns the access and refresh tokens
  '''

  #Open the file
  file = open('tokens.txt','r')

  #Read first two lines - first is the access token, second is the refresh token
  AccToken = file.readline()
  RefToken = file.readline()

  #Close the file
  file.close()

  #See if the strings have newline characters on the end.  If so, strip them
  if (AccToken.find("\n") > 0):
    AccToken = AccToken[:-1]
  if (RefToken.find("\n") > 0):
    RefToken = RefToken[:-1]

  #Return values
  return AccToken, RefToken

def MakeAPICall(InURL,AccToken,RefToken):
  #Start the request
  req = urllib2.Request(InURL)

  #Add the access token in the header
  req.add_header('Authorization', 'Bearer ' + AccToken)

  #Fire off the request
  try:
    #Do the request
    response = urllib2.urlopen(req)
    #Read the response
    FullResponse = response.read()

    #Return values
    return True, FullResponse

  except urllib2.URLError as e:
    print "Got this HTTP error: " + str(e.code)
    HTTPErrorMessage = e.read()
    print "This was in the HTTP error message: " + HTTPErrorMessage
    #See what the error was
    if (e.code == 401) and (HTTPErrorMessage.find("Access token invalid or expired") > 0):
      print "Need a new token buddy"
    #Return that this didn't work, allowing the calling function to handle it
    return False, ErrorInAPI


def FindWakeTime(start, inBed):
	'''
	Takes the values of sleep start time, and minutes in bed
	as text values, converts them into datetime objects, 
	adds the minutes value to the starttime value
	and then converts that value into a string
	and returns it
	'''

	dateobject = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S.000")
	end = dateobject + datetime.timedelta(minutes = int(inBed))
	endTime = datetime.datetime.strftime(end, "%Y-%m-%dT%H:%M:%S.000")
	return endTime

def checkIfFileExists(fileName):
	'''
	Uses the os.path to find out if fileName exists 
	'''
	try: 
		check = os.stat(fileName)
	except os.error:
		return False
	return True


tokenCheck = checkIfFileExists('tokens.txt')

if not tokenCheck:
	sys.exit('No file for tokens exists')



#Asks the user for input on what dates to get sleeping data for
print "Enter Beginning date YYYY-MM-DD"
firstDateInput = raw_input()

print "Enter Final date YYYY-MM-DD"
lastDateInput = raw_input()

#Converts the text values into dateTime objects
firstDate = datetime.datetime.strptime(firstDateInput, '%Y-%m-%d')
lastDate = datetime.datetime.strptime(lastDateInput, '%Y-%m-%d')

#finds the number of days needed to increment later on 
datesToGet = (lastDate - firstDate).days



#Get the tokens
AccessToken, RefreshToken = GetTokens()


while firstDate < lastDate:

	currentDate = datetime.datetime.strftime(firstDate, '%Y-%m-%d')
	FitbitURL = "https://api.fitbit.com/1/user/-/sleep/date/%s.json" % (currentDate)

	print "Getting values for " + currentDate + " and fitbit url is " + FitbitURL


	APICallOK, APIResponse = MakeAPICall(FitbitURL, AccessToken, RefreshToken)

	if APICallOK:
		j = json.loads(APIResponse)

		x = j['summary']['totalSleepRecords']

		if (x != 0):
			starttime =  j['sleep'][0]['startTime']
			timeinbed =  j['sleep'][0]['timeInBed']

			end = FindWakeTime(starttime, timeinbed)

			print "You went to sleep at " + starttime + " and woke up at " + end
			writeToCSV(starttime, end)

		else:
			print "No data for that day, moving on"
		
		print '\n\n'

		firstDate = firstDate + datetime.timedelta(days = 1)
	else:
  		print ErrorInAPI	

  