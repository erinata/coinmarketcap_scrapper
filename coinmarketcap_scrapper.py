import urllib.request

response = urllib.request.urlopen('https://coinmarketcap.com/')

html = response.read()

print(html)

