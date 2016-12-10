import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

def get_html_page(query, page):
    request = 'https://www.monster.com/jobs/search/?q='
    request += query # Enter '-' for any spaces
    request += '&page='
    request += str(page)
    
    return requests.get(request)

def get_page_results(query, page):
    r = get_html_page(query, page)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('script', {'type' : 'application/ld+json'}) # Results come in script tag
    results.pop(0) # Remove search info from results
    return results

def get_n_results(query, n):
    results = []
    current_page = 1
    # Add results page by page
    while len(results) < n:
        results += get_page_results(query, current_page)
        current_page += 1
    # Remove extra results from end
    while len(results) > n:
        results.pop(-1)
    return results

def make_json(results):
    json_string = '{ "results" : [' # Open json
    # Write results
    for result in results:
        result_text = result.string # Get result string
        # Clean out extra spaces and new lines
        result_text = result_text.replace('\r\n', '')
        result_text = result_text.replace('  ', ' ')
        result_text = result_text.replace('  ', ' ')
        result_text = result_text.replace('  ', ' ')
        result_text = result_text.replace('  ', ' ')
        json_string += result_text # Append to json
        # Add ',' if not last element
        if result != results[-1]:
            json_string += ','
    json_string += ']}' # Close json
    # Prettify
    json_string = json.loads(json_string)
    json_string = json.dumps(json_string, sort_keys=True, indent=4)
    return json_string
    
results = get_n_results('Developer', 1000)
json_string = make_json(results)

file = open('results.json', 'w')
file.write(json_string)
file.close()