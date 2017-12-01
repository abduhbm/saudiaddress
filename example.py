
# coding: utf-8

# In[2]:


from __future__ import print_function
from __future__ import unicode_literals
import os
import time
from saudiaddress.api import NationalAddress


# In[3]:

# initialize
DELAY_IN_SEC = 5

api_key = os.environ.get('NATIONAL_ADDRESS_API_KEY')

na = NationalAddress(key=api_key)


# In[4]:

# to get a national address from lat/long 
addresses = na.get_address(lat=26.318922, long=50.228043, language='E')
print("address:", addresses.records[0])


# In[5]:

time.sleep(DELAY_IN_SEC)
# to bulk search a list of (building_no, post_code, additional_no)
for address in na.bulk_search([(3468, 23955, 7487), (6418, 34412, 3618)], page=1).records:
    print(address)


# In[6]:

time.sleep(DELAY_IN_SEC)
# to verify an address
print("the address is", na.verify_address(6418, 34412, 3618))


# In[7]:

time.sleep(DELAY_IN_SEC)
# free text search for an address
addresses = na.free_text_search('2292  - king abdullah university of science and technology')
print("count:", addresses.count)
address = addresses.records[0]
print('lat={lat}, long={long}, city={city}, region={region}'.format(lat=address.Latitude, long=address.Longitude,
                                                                    city=address.City, region=address.RegionName))


# In[8]:

time.sleep(DELAY_IN_SEC)
# search nearest services
addresses = na.nearest_poi(lat=22.32, long=39.09, radius=2)
for address in addresses.records:
    print('title:%s' % address.Title)
    print('address:', address)


# In[9]:

time.sleep(DELAY_IN_SEC)
# search services based on fixed parameters
addresses = na.fixed_search(city_name='THUWAL', post_code=23955, additional_number=7487)
print(addresses.records[0])


# In[11]:

time.sleep(DELAY_IN_SEC)
# find availability of services by providing details in free text
addresses = na.poi_free_text_search('sabb atm', language='E')
print('total SABB ATMs found: %d' % addresses.count)
print(addresses.records)


# In[4]:

time.sleep(DELAY_IN_SEC)
# get a list of regions
regions = na.get_regions(language='A')
for region in regions[:5]:
    print(region)


# In[6]:

time.sleep(DELAY_IN_SEC)
# get a list of cities in a region
cities = na.get_cities(region_id=1)
for city in cities[:5]:
    print(city)


# In[14]:

time.sleep(DELAY_IN_SEC)
# get a list of districts in a city
districts = na.get_districts(city_id=3)
for district in districts[:5]:
    print(district)


# In[9]:

time.sleep(DELAY_IN_SEC)
# get a list of service categories
categories = na.get_categories()
for category in categories[:5]:
    print(category)


# In[13]:

time.sleep(DELAY_IN_SEC)
# to get a list of sub-service categories
sub_categories = na.get_subcategories(service_category_id=101)
for sub_category in sub_categories[:5]:
    print(sub_category)


# In[20]:

time.sleep(DELAY_IN_SEC)
# find all ATMs in district ad dirah in AR RIYADH city
services = na.poi_fixed_search('atm', district_name='ad dirah', city_name='AR RIYADH', page=1)
print("total:", services.count)
for service in services.records:
    print(service.Title, service)


# In[ ]:



