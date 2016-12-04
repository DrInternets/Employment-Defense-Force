import json
import sys
from indeed import IndeedClient

client = IndeedClient(publisher = 9074116252229934)

i = 0
pagenumber = 0
for x in range (0,40):
    pagenumber += 1
    params = {
    'q' : "developer",
    "l" : "austin",
    'userip' : "50.24.191.212",
    'useragent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
    'start' : i,
    'limit' : 25
    'radius' : 25
    }
    i += 25
    search_response = client.search(**params)
    with open('data.json', 'a') as f:
        json.dump(search_response, f)
    print "Getting page number", pagenumber

print "All pages successfully saved"
sys.exit()
