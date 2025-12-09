import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

def get_rates():
   response = requests.get(URL)
   if response.status_code != 200:
      print("Помилка отримання даних з НБУ!")
      return None

   data = response.json()
   rates = {}

   for item in data:
      if item["cc"] in ["USD", "EUR", "PLN"]:
         rates[item["cc"]] = item["rate"]

   return rates

def main():
   rates = get_rates()
   if not rates:
      return

   print("\nАктуальний курси валют :")
   for code, rate in rates.items():
      print(f"{code}: {rate} грн")

   while True:
      currency = input("\nДля завершення роботи введіть 'exit' \nВведіть валюту (USD, EUR, PLN) : ").upper()
      if currency == "EXIT":
         print("Програму завершено.")
         break
      if currency not in rates:
         print(" Оберіть з перелічених валют: USD, EUR або PLN.")
         continue
      try:
         amount = float(input("Введіть необхідну суму: "))
         result = amount * rates[currency]
         print(f"{amount} {currency} = {result:.2f} грн")
      except ValueError:
         print("Введіть числове значення суми!")

main()
