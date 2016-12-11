# Imports
import json
from pandas.io.json import json_normalize
import pandas as pd

# Read .json file to dataframe
data = pd.read_json('.\linkedin_results_1000.json', orient='column')

# Normalize/ flatten dataframe
data = json_normalize(data['results'])

# Create desired dataframe
data = pd.concat([data['decoratedJobPosting.companyName'], data['decoratedJobPosting.cityState'], data['decoratedJobPosting.jobPosting.title']], axis=1,)

# Rename dataframe columns
data.rename(columns={'decoratedJobPosting.companyName' : 'Name', 'decoratedJobPosting.cityState' : 'Location', 'decoratedJobPosting.jobPosting.title' : 'Job Title'}, inplace=True)

# Import dataframe to .csv
data.to_csv('linkedin.csv', encoding='utf-8')

# Print dataframe
print data
