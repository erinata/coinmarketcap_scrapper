from bs4 import BeautifulSoup
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")



f = open("html_files/coinmarketcap20190210160211.html", "r")

# print(f.read())

soup = BeautifulSoup(f.read(), 'html.parser')

print(soup)


