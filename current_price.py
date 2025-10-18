import requests

data=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
price=data.json()
print(f"Bitcoin: ${price['bitcoin']['usd']:,.2f}")