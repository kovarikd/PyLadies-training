import requests, json

with open('23_5_2019_Slovniky/sample.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

stranka = requests.get('https://api.github.com/user', headers=headers)
stranka.raise_for_status()
data = json.loads(stranka.text)
print(json.dumps(data, ensure_ascii=True, indent=2))

print(data['avatar_url'])
