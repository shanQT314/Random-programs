import requests
import json
import urllib
import re 

queryParameter = "Rhegmatorhina"

response = requests.get('https://www.xeno-canto.org/api/2/recordings', params=(('query', 'Rhegmatorhina'),('pg','1')))
parsed = json.loads(response.text)

recordings = parsed["recordings"]
for recording in recordings: 
    redirect = requests.get("https:" + recording["url"]) 
    newResults = re.findall(r"data-xc-filepath=\'(\S+)\'", redirect.text)
    mp3file = urllib.request.urlretrieve("https:" + newResults[0], queryParameter + "_" + recording["sp"] + "_" +  recording["type"] +"_" + recording["cnt"] + "__XC" + recording["id"] + ".mp3")
