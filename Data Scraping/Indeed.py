import json
import sys
from indeed import IndeedClient

client = IndeedClient(publisher=9074116252229934)

results = [ ]
i = 0
pagenumber = 0
for x in range(0, 40):
    pagenumber += 1
    params = {
        'q': "developer",
        'userip': "50.24.191.212",
        'useragent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
        'start': i,
        'limit': 25,
        'radius': 25
    }
    i += 25
    search_response = client.search(**params)
    search_response = json.loads(json.dumps(search_response))

    results += search_response[ 'results' ]

json_string = json.dumps({'results': results}, sort_keys=True, indent=4)

file = open('data.json', 'w')
file.write(json_string)
file.close()
