import urllib.request
import os
import time
import datetime

if not os.path.exists("output"):
	os.mkdir("output")

for i in range(5):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	print(str(i) + ": " + current_time_stamp)
	f = open("output/coinmarketcap" + current_time_stamp + ".html", "wb")
	response = urllib.request.urlopen('https://coinmarketcap.com/')
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(10)



