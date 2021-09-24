import requests
import json

coin_market_cap = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false", 
    headers = {"accept": "application/json"})

print("Enter the number of top cryptocurrencies by market capitalization: ")
n = int(input())
i = 0
while i < n:
    print(str(i + 1) + '. "Cryptocurrency": ' + '"' + str(coin_market_cap.json()[i]['name']) + '"'', "market cap": ' + 
          str(coin_market_cap.json()[i]['market_cap']) + ', "current price": ' + str(coin_market_cap.json()[i]['current_price']))
    i += 1
