import requests

base = "PLN"
url = ("https://api.apilayer.com/exchangerates_data/latest?base=" + base)
payload = {}
headers= {
  "apikey": "Nll2qGcmrqa5cfgphZJHfpEAOl6mQxGN"
}


response = requests.get(url, headers=headers, data = payload)

if response.ok == True:
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    date = data["date"]
    
    print("base: " + base)
    print("date: " + date)
    #print(rates)
    
    for key in rates:
        print(key + ": ", rates[key])