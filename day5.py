import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
table = soup.find("tbody")
rows = table.find_all("tr")
countries = []
currency_codes = []
answer = ""

for row in rows:
  columns = row.find_all("td")
  if columns[2].string != None:
    countries.append(columns[0].string.capitalize())
    currency_codes.append(columns[2].string)

print("Hello! Please choose select a country by number :")

for index, country in enumerate(countries):
  print(f"# {index} {country}")

while(True):
  try:
    answer = int(input("#: "))
    if answer in range(len(countries)):
      break
    else:
      print("Choose a number from the list.")
  except:
    print("That wasn't a number.")

print(f"You chose {countries[answer]}")
print(f"The currency code is {currency_codes[answer]}")