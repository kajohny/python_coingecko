FILTER TOP CRYPTOCURRENCIES FROM COINGECKO

Installation

pip install requests


Usage

import requests
cc = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false", headers = {"accept": "application/json"})

Examples

Everything is defined in coingecko API: https://www.coingecko.com/api/documentations/v3

Example of usage:
  cc = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false", 
    headers = {"accept": "application/json"})
  print(cc.json())
  print(cc.json()[n]['name'])
  print(cc.json()[n]['current_price'])
  print(cc.json()[n]['market_cap'])
