# encoding=utf-8

import urllib2
import json
import time
import datetime

outfile = open('City.csv','w')
link =  'https://aviation-edge.com/v2/public/cityDatabase?key=1017f2-25efad'
req = urllib2.Request(link, headers={'User-Agent': "Magic BROESER"})
try:
 response = urllib2.urlopen(req)
 html = response.read()
 j = json.loads(html)
except urllib2.HTTPError, e:
 print('HTTPError ='+ str(e.code))
except urllib2.URLError, e:
 print('URLError ='+ str(e.reason))
for i in j:
    v = i['cityId']
    v1 = ''
    v2 = i['codeIataCity']
    print v2
    v3 = i['codeIso2Country']
    v4 = ''
    v5 = i['latitudeCity']  
    v6 = i['longitudeCity'] 
    v7 = i['timezone']  
    v8 = i['GMT']  
    v9 = i['geonameId']     
    outfile.write(str(v) + ',' + str(v1) + ',' + str(v2) + ',' + str(v3) + ',' + str(v4) + ',' + str(v5) + ',' + str(v6) + ',' + str(v7) + ',' + str(v8) + ',' + str(v9) + '\n')    