# FILTER TOP CRYPTOCURRENCIES FROM COINGECKO

## Installation
```
pip install requests
```

## Usage
```
import requests
cc = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    , headers = {"accept": "application/json"})
```
## Examples

Everything is defined in **coingecko API**: https://www.coingecko.com/api/documentations/v3

*Example of usage*:
```
cc = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false", 
    headers = {"accept": "application/json"})
print(cc.json())
print(cc.json()[n]['name'])
print(cc.json()[n]['current_price'])
print(cc.json()[n]['market_cap'])
```

*Filters out top N cryptocurrencies by market capitalization*:

Input:
5
Output:
1. "Cryptocurrency": "Bitcoin", "market cap": 793895115868, "current price": 42291
2. "Cryptocurrency": "Ethereum", "market cap": 340501314917, "current price": 2902.96
3. "Cryptocurrency": "Cardano", "market cap": 71390776955, "current price": 2.24
4. "Cryptocurrency": "Tether", "market cap": 69735010525, "current price": 1.0
5. "Cryptocurrency": "Binance Coin", "market cap": 54047611085, "current price": 350.6

## License
(https://choosealicense.com/licenses/mit/)
