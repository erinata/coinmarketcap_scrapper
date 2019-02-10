import urllib.request
import os

response = urllib.request.urlopen('https://coinmarketcap.com/')

html = response.read()

# print(html)

if not os.path.exists("output"):
	os.mkdir("output")

f = open("output/coinmarketcap.html", "wb")
f.write(html)

