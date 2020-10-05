import requests, json, pandas

print("Welcome to the Ice And Fire Api - Houses to TSV")

try:
    response = requests.get('https://anapioficeandfire.com/api/houses')
except:
    print('ERROR 500! Server is down')
    exit()


housesData = json.loads(response.text)

houseName = []
houseRegion = []
houseCoatOfArms = []
houseWords = []

for dict in housesData:
    houseName.append((dict['name']))
    houseRegion.append((dict['region']))
    houseCoatOfArms.append((dict['coatOfArms']))
    houseWords.append((dict['words']))

df = pandas.DataFrame({
     'Name': houseName,
     'Region': houseRegion,
     'Coat Of Arms': houseCoatOfArms,
     'Words': houseWords
     })

print("Conversion under progress...")
try:
    df.to_csv('Ice&Fire_Houses.tsv', sep='\t', index=False)
    print("Your TSV file is ready! Search for Ice&Fire_Houses.tsv")
except:
    print("Conversion has gone wrong!")
    exit()
