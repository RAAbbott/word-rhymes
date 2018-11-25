import requests


print("Enter a word to find rhymes!")
word = input()



query_rhy = f"?rel_rhy={word}"
query_nry = f"?rel_nry={word}"

response_rhy = requests.get(f'https://api.datamuse.com/words{query_rhy}')
response_nry = requests.get(f'https://api.datamuse.com/words{query_nry}')

data_rhy = response_rhy.json()
data_nry = response_nry.json()

if data_rhy == [] and data_nry == []:
    print("Check your spelling bro, that's not a word!")

print('')

for i in data_rhy:
    print(i['word'])

for i in data_nry:
    print(i['word'])