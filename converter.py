import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangeratesapi.io/latest?base={from_currency}&symbols={to_currency}"
    response = requests.get(url)
    exchange_rate = response.json()["rates"][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount
