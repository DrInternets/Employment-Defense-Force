# LinkedIn Jobs Board Scraper
# Creator: Aaron Kingery

import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

QUERY = 'Developer'
LOCATION = 'tx' # location should be lowercase two letter state abbreviation (e.g. tx)
N_RESULTS = 1000
DATA_FILE_NAME = 'linkedin_results_1000.json'

def get_html_page(start):
    request = 'https://www.linkedin.com/jobs/search?keywords='
    query = QUERY.replace(' ', '%20') # Correct spaces
    request += query
    request += '&locationId=STATES.us.'
    request += LOCATION
    request += '&orig=JSERP&start='
    request += str(start)
    request += '&count=25&trk=jobs_jserp_pagination_'
    request += str((start // 25) + 1) # Calculate page number
    
    return requests.get(request)

def get_html_page_results(start):
    results = []
    # Request page until it doesn't redirect
    while len(results) < 1:
        html = get_html_page(start)
        soup = BeautifulSoup(html.text, 'html.parser')
        results = soup.find_all('code', {'id' : 'decoratedJobPostingsModule'})
    
    result_json_string = results[0].string # all results come in one json object
    json_data = json.loads(result_json_string) # get json data
    
    return json_data['elements'] # get search results

def get_results():
    results = []
    current_start = 0
    while len(results) < N_RESULTS:
        results += get_html_page_results(current_start)
        current_start = len(results)
    return results
    
final_results = get_results()
final_json_string = json.dumps({'results' : final_results}, sort_keys=True, indent=4) 

file = open(DATA_FILE_NAME, 'w')
file.write(final_json_string)
file.close()