from bs4 import BeautifulSoup
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")



f = open("html_files/coinmarketcap20190210160211.html", "r")

# print(f.read())

soup = BeautifulSoup(f.read(), 'html.parser')

# print(soup)


currencies_table = soup.find("table", {"id": "currencies"})
currencies_tbody = currencies_table.find("tbody")
currency_rows = currencies_tbody.find_all("tr")



for r in currency_rows:
	currency_short_name = r.find("td", {"class": "currency-name"}).find("span",{"class":"currency-symbol"}).find("a").text
	currency_name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
	currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
	currency_price = r.find("a",{"class": "price"}).text
	currency_volume = r.find("a",{"class": "volume"}).text
	currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
	currency_change = r.find("td", {"class": "percent-change"})['data-sort']
	print(currency_short_name)
	print(currency_name)
	print(currency_market_cap)
	print(currency_price)
	print(currency_volume)
	print(currency_supply)
	print(currency_change)
	print("\n")


