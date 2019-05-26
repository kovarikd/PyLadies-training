import requests

# stazeni stranky
stranka = requests.get('https://github.com')

# overeni, ze dotaz probehl v poradku
stranka.raise_for_status()

# vypsani obsahu
print(stranka.text.encode('utf-8'))