import requests  #pip install requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if "rates" in data and target_currency in data["rates"]:
        return data["rates"][target_currency]
    else:
        print("Error: Invalid currency code or API issue.")
        return None

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        return amount * rate
    else:
        return None

if __name__ == "__main__":
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))
    
    converted_amount = convert_currency(amount, base_currency, target_currency)
    
    if converted_amount:
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
