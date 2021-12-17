import json

acd = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', 'balance': 345.67}
    ]}

with open('acount.json','w') as ac:
    json.dump(acd,ac)

with open('acount.json','r') as ac:
    af=json.load(ac)
    print(af)
