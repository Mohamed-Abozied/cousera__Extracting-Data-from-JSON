import urllib.request
import json

url = input('Enter URL: ')

print('Retrieving', url)

json_file = urllib.request.urlopen(url).read()
print('Retrieved', len(json_file), 'characters')
info = json.loads(json_file)

total = 0
sum = 0

for item in info['comments']:
    sum += int(item["count"])
    total += 1

print('count', total)
print('Sum', sum)

# ***************** output ************
# Retrieving http://py4e-data.dr-chuck.net/comments_1569622.json
# Retrieved 2721 characters
# count 50
# Sum 2269