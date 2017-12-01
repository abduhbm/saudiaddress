# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import requests
from .models import ResultSet, Address, Region, City, District, ServiceCategory, ServiceSubCategory

SA_NATIONAL_ADDRESS_URL = 'https://apina.address.gov.sa'
FORMAT = 'json'
ENCODE = 'utf8'


class NationalAddress(object):
    def __init__(self, url=None, key=None):
        if url:
            self.url = url
        else:
            self.url = SA_NATIONAL_ADDRESS_URL

        if key:
            self.key = key
        else:
            raise ValueError('no api_key was provided')

    def get_address(self, lat, long, language='E'):
        """Address reverse Geocode
        Args:
            lat: latitude in decimal unit
            long: longitude in decimal unit
            language: A for Arabic, E for English
        """
        headers = {'api_key': self.key}
        params = {'lat': lat, 'long': long, 'language': language, 'format': FORMAT, 'encode': ENCODE}
        r = requests.get(self.url + '/NationalAddress/v3.1/Address/address-geocode', params=params, headers=headers)
        result = r.json()
        addresses = []
        total = 0
        if result.get('success'):
            records = result.get('Addresses')
            total = result.get('totalSearchResults', 0)
            if records:
                for record in records:
                    addresses.append(Address.from_json(record))

        rs = ResultSet(addresses, int(total))
        return rs

    def bulk_search(self, addresses_tuple, language='E', page=1):
        """Search bulk addresses for complete details
        Args:
            addresses_tuple: a list of tuple in the form [(building_number, zip_code, additional_number)]
            language: A for Arabic, E for English
            page: if search count > 10, then this must be passed along to get the next set of results.
        """
        addresses_list = []
        for address in addresses_tuple:
            addresses_list.append('|'.join(str(attribute) for attribute in address))
        address_string = ';'.join(addresses_list)
        headers = {'api_key': self.key}
        params = {'addressstring': address_string, 'language': language, 'format': FORMAT, 'encode': ENCODE,
                  'page': page}
        r = requests.get(self.url + '/NationalAddress/v3.1/Address/address-bulk', params=params, headers=headers)
        result = r.json()
        addresses = []
        total = 0
        if result.get('success'):
            records = result.get('Addresses')
            total = result.get('totalSearchResults', 0)
            if records:
                for record in records:
                    addresses.append(Address.from_json(record))

        rs = ResultSet(addresses, int(total))
        return rs

    def fixed_search(self, language='E', page=1, city_id=None, district_id=None, building_number=None, post_code=None,
                     additional_number=None, city_name=None, district_name=None, street_name=None):
        """Find a complete address by providing some details about it"""
        headers = {'api_key': self.key}
        params = {'language': language, 'page': page, 'format': FORMAT, 'encode': ENCODE, 'cityId': city_id,
                  'districtId': district_id, 'buildingnumber': building_number, 'zipcode': post_code,
                  'additionalnumber': additional_number, 'cityname': city_name, 'districtname': district_name,
                  'streetname': street_name}
        r = requests.get(self.url + '/NationalAddress/v3.1/Address/address-fixed-params', params=params,
                         headers=headers)
        result = r.json()
        addresses = []
        total = 0
        if result.get('success'):
            records = result.get('Addresses')
            total = result.get('totalSearchResults', 0)
            if records:
                for record in records:
                    addresses.append(Address.from_json(record))

        rs = ResultSet(addresses, int(total))
        return rs

    def free_text_search(self, address_string, language='E', page=1):
        """Find a complete address by providing some details in free text"""
        headers = {'api_key': self.key}
        params = {'addressstring': address_string, 'language': language, 'format': FORMAT, 'encode': ENCODE,
                  'page': page}
        r = requests.get(self.url + '/NationalAddress/v3.1/Address/address-free-text', params=params, headers=headers)
        result = r.json()
        addresses = []
        total = 0
        if result.get('success'):
            records = result.get('Addresses')
            total = result.get('totalSearchResults', 0)
            if records:
                for record in records:
                    addresses.append(Address.from_json(record))

        rs = ResultSet(addresses, int(total))
        return rs

    def nearest_poi(self, lat, long, language='E', page=1, radius=0.5):
        """Search nearest service"""
        headers = {'api_key': self.key}
        params = {'lat': lat, 'long': long, 'language': language, 'format': FORMAT, 'encode': ENCODE,
                  'page': page, 'radius': radius}
        r = requests.get(self.url + '/NationalAddress/v3.1/Address/poi-nearest', params=params, headers=headers)
        result = r.json()
        addresses = []
        total = 0
        if result.get('success'):
            records = result.get('Addresses')
            total = result.get('totalSearchResults', 0)
            if records:
                for record in records:
                    addresses.append(Address.from_json(record))

        rs = ResultSet(addresses, int(total))
        return rs

    def poi_fixed_search(self, service_string, language='E', page=1, city_id=None, district_id=None,
                         building_number=None, post_code=None, additional_number=None, city_name=None,
                         district_name=None, street_name=None, service_category_id=None, service_subcategory_id=None,
                         region_id=None):
        """Find availability of a service by providing some details in fixed parameters"""
        headers = {'api_key': self.key}
        params = {'servicestring': service_string, 'language': language, 'format': FORMAT, 'encode': ENCODE,
                  'page': page, 'cityId': city_id, 'districtId': district_id, 'buildingnumber': building_number,
                  'zipcode': post_code, 'additionalnumber': additional_number, 'cityname': city_name,
                  'districtname': district_name, 'streetname': street_name, 'servicecategoryId': service_category_id,
                  'servicesubcategoryId': service_subcategory_id, 'regionid': region_id}
        r = requests.get(self.url + '/NationalAddress/v3.1/Address/poi-fixed-params', params=params, headers=headers)
        result = r.json()
        addresses = []
        total = 0
        if result.get('success'):
            records = result.get('Addresses')
            total = result.get('totalSearchResults', 0)
            if records:
                for record in records:
                    addresses.append(Address.from_json(record))

        rs = ResultSet(addresses, int(total))
        return rs

    def poi_free_text_search(self, service_string, language='E', page=1):
        """Find availability of a service by providing some details in free text"""
        headers = {'api_key': self.key}
        params = {'servicestring': service_string, 'language': language, 'format': FORMAT, 'encode': ENCODE,
                  'page': page}
        r = requests.get(self.url + '/NationalAddress/v3.1/Address/poi-free-text', params=params, headers=headers)
        result = r.json()
        addresses = []
        total = 0
        if result.get('success'):
            records = result.get('Addresses')
            total = result.get('totalSearchResults', 0)
            if records:
                for record in records:
                    addresses.append(Address.from_json(record))

        rs = ResultSet(addresses, int(total))
        return rs

    def verify_address(self, building_number, post_code, additional_number, language='E', page=1):
        """Verify an address"""
        headers = {'api_key': self.key}
        params = {'buildingnumber': building_number, 'zipcode': post_code, 'additionalnumber': additional_number,
                  'language': language, 'format': FORMAT, 'encode': ENCODE, 'page': page}
        r = requests.get(self.url + '/NationalAddress/v3.1/Address/address-verify', params=params, headers=headers)
        result = r.json()
        if result.get('success'):
            return result.get('addressfound')

    def get_regions(self, language='E'):
        """Get a lookup list of regions"""
        headers = {'api_key': self.key}
        params = {'language': language, 'format': FORMAT, 'encode': ENCODE}
        r = requests.get(self.url + '/NationalAddress/v3.1/lookup/regions', params=params, headers=headers)
        result = r.json()
        lookup = []
        if result.get('success'):
            records = result.get('Regions')
            if records:
                for record in records:
                    lookup.append(Region.from_json(record))

        return lookup

    def get_cities(self, region_id=-1, language='E'):
        """Get a lookup list of cities"""
        headers = {'api_key': self.key}
        params = {'language': language, 'format': FORMAT, 'regionid': region_id}
        r = requests.get(self.url + '/NationalAddress/v3.1/lookup/cities', params=params, headers=headers)
        result = r.json()
        lookup = []
        if result.get('success'):
            records = result.get('Cities')
            if records:
                for record in records:
                    lookup.append(City.from_json(record))

        return lookup

    def get_districts(self, city_id=-1, language='E'):
        """Get a lookup list of districts"""
        headers = {'api_key': self.key}
        params = {'language': language, 'format': FORMAT, 'cityid': city_id}
        r = requests.get(self.url + '/NationalAddress/v3.1/lookup/districts', params=params, headers=headers)
        result = r.json()
        lookup = []
        if result.get('success'):
            records = result.get('Districts')
            if records:
                for record in records:
                    lookup.append(District.from_json(record))

        return lookup

    def get_categories(self, language='E'):
        """Get a lookup list of service categories"""
        headers = {'api_key': self.key}
        params = {'language': language, 'format': FORMAT}
        r = requests.get(self.url + '/NationalAddress/v3.1/lookup/service-categories', params=params, headers=headers)
        result = r.json()
        lookup = []
        if result.get('success'):
            records = result.get('ServiceCategories')
            if records:
                for record in records:
                    lookup.append(ServiceCategory.from_json(record))

        return lookup

    def get_subcategories(self, service_category_id=-1, language='E'):
        """Get a lookup list of service sub-categories"""
        headers = {'api_key': self.key}
        params = {'language': language, 'format': FORMAT, 'servicecategoryid': service_category_id}
        r = requests.get(self.url + '/NationalAddress/v3.1/lookup/services-sub-categories', params=params,
                         headers=headers)
        result = r.json()
        lookup = []
        if result.get('success'):
            records = result.get('ServiceSubCategories')
            if records:
                for record in records:
                    lookup.append(ServiceSubCategory.from_json(record))

        return lookup