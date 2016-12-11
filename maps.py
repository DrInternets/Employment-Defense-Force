%matplotlib inline

from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import json

with open('linkedin_results_1000.json') as data_file:    
    linkedin_json = json.load(data_file)
    
linkedin_results = linkedin_json['results']

geolocator = Nominatim()
linkedin_lons = []
linkedin_lats = []
for i in range(0, 200):
    location = geolocator.geocode(linkedin_results[i]['decoratedJobPosting']['cityState'])
    linkedin_lons.append(location.longitude)
    linkedin_lats.append(location.latitude)

fig = plt.figure()

themap = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49, projection='lcc',lat_1=32,lat_2=45,lon_0=-95)
themap.drawcoastlines()
themap.drawcountries()
themap.drawstates()
themap.fillcontinents(color = 'gainsboro')
themap.drawmapboundary(fill_color='steelblue')

linkedin_x, linkedin_y = themap(linkedin_lons, linkedin_lats)
      
themap.plot(linkedin_x, linkedin_y, 
            'o',
            color='Blue',
            markersize=4
            )

plt.show()
