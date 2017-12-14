saudiaddress: A simple Python wrapper for the Saudi National Address APIs
=========================================================================

Saudi National Address API website: `https://api.address.gov.sa <https://api.address.gov.sa>`_

Basic Usage of saudiaddress
---------------------------

.. code-block:: pycon

    >>> from saudiaddress.api import NationalAddress
    >>> api_key = os.environ.get('NATIONAL_ADDRESS_API_KEY')
    >>> na = NationalAddress(key=api_key)


Reverse geocoding of coordinates to a national address

.. code-block:: pycon

    >>> addresses = na.get_address(lat=26.318922, long=50.228043, language='E')
    >>> print("address:", addresses.records[0])
    address: 6418 al kurnaysh road - al kurnaish AL KHUBAR 34412 - 3618

Bulk search a list of (building number, post code, additional number)

.. code-block:: pycon

    >>> for address in na.bulk_search([(3468, 23955, 7487), (6418, 34412, 3618)], page=1).records:
    >>>     print(address)
    3468  - king abdullah university of science and technology THUWAL 23955 - 7487
    6418 al kurnaysh road - al kurnaish AL KHUBAR 34412 - 3618

Verify a national address

.. code-block:: pycon

    >>> print("the address is", na.verify_address(6418, 34412, 3618))
    the address is True

Free text search for a national address

.. code-block:: pycon

    >>> addresses = na.free_text_search('2292  - king abdullah university of science and technology')
    >>> print("count:", addresses.count)
    >>> address = addresses.records[0]
    >>> print('lat={lat}, long={long}, city={city}, region={region}'.format(lat=address.Latitude, long=address.Longitude, city=address.City, region=address.RegionName))
    count: 1
    lat=22.324697064547, long=39.0942996143403, city=THUWAL, region=Makkah

Search nearest services

.. code-block:: pycon

    >>> addresses = na.nearest_poi(lat=22.32, long=39.09, radius=2)
    >>> for address in addresses.records:
    >>>     print('title:%s' % address.Title)
    >>>     print('address:', address)
    title:Samba atm
    address: 3468  - king abdullah university of science and technology THUWAL 23955 - 7487
    title:sabb bank
    address: 7126  - king abdullah university of science and technology THUWAL 23955 - 3451

Search services based on fixed parameters

.. code-block:: pycon

    >>> addresses = na.fixed_search(city_name='THUWAL', post_code=23955, additional_number=7487)
    >>> print(addresses.records[0])
    3468  - king abdullah university of science and technology THUWAL 23955 - 7487

Find availability of services by providing details in free text

.. code-block:: pycon

    >>> addresses = na.poi_free_text_search('sabb atm', language='E')
    >>> print('total SABB ATMs found: %d' % addresses.count)
    >>> print(addresses.records)
    total SABB ATMs found: 695
    6897 king fahd road - al ulaya AR RIYADH 12211 - 3388
    7277 king fahd road - al ulaya AR RIYADH 12212 - 3333
    7411 king fahd road - al ulaya AR RIYADH 12212 - 3229
    2946 al amir muhammad ibn abdul aziz branch rd - al ulaya AR RIYADH 12213 - 7929
    2332 no 92 - al ulaya AR RIYADH 12214 - 9330

Get a list of regions

.. code-block:: pycon


    >>> regions = na.get_regions(language='A')
    >>> for region in regions[:5]:
    >>>     print(region)
    Region (ID=12, Name= الباحة)
    Region (ID=13, Name= الجوف)
    Region (ID=9, Name= الحدود الشمالية)
    Region (ID=1, Name= الرياض)
    Region (ID=4, Name= القصيم)

Get a list of cities within a region

.. code-block:: pycon

    >>> cities = na.get_cities(region_id=1)
    >>> for city in cities[:5]:
    >>>     print(city)
    City (ID=3, Name=AR RIYADH)
    City (ID=828, Name=AD DIR'IYAH)
    City (ID=669, Name=AD DUWADIMI)
    City (ID=1061, Name=AL KHARJ)
    City (ID=24, Name=AL MAJMA'AH)

Get a list of districts in a city

.. code-block:: pycon

    >>> districts = na.get_districts(city_id=3)
    >>> for district in districts[:5]:
    >>>     print(district)
    District (ID=10100003130, Name=ad dar al baida)
    District (ID=10100003039, Name=ad difa)
    District (ID=10100003007, Name=ad dirah)
    District (ID=10100003116, Name=ad dubiyah)
    District (ID=10100003076, Name=ad duraihimiyah)

Get a list of service categories

.. code-block:: pycon

    >>> categories = na.get_categories()
    >>> for category in categories[:5]:
    >>>     print(category)
    Category (ID=101, Name=Auto Services)
    Category (ID=122, Name=CivilDefense)
    Category (ID=102, Name=Commercial)
    Category (ID=103, Name=Cultural Sites)
    Category (ID=104, Name=Diplomatic)

Get a list of sub-service categories

.. code-block:: pycon

    >>> sub_categories = na.get_subcategories(service_category_id=101)
    >>> for sub_category in sub_categories[:5]:
    >>>     print(sub_category)
    Sub-Category (ID=10101, Name=Auto Agency)
    Sub-Category (ID=10102, Name=Auto Service Station)
    Sub-Category (ID=10103, Name=Auto Showroom)
    Sub-Category (ID=10104, Name=Auto Spare Parts)
    Sub-Category (ID=10105, Name=Auto Workshop)

Fina all ATMs in district 'ad dirah' in Riyadh city

.. code-block:: pycon


    >>> services = na.poi_fixed_search('atm', district_name='ad dirah', city_name='AR RIYADH', page=1)
    >>> print("total:", services.count)
    >>> for service in services.records:
    >>>     print(service.Title, service)
    total: 19
    al rajhi atm 7221  - ad dirah AR RIYADH 12633 - 3262
    albilad atm 7272 al batha - ad dirah AR RIYADH 12633 - 3394
    albilad atm 2778 al imam muhammad ibn saud ibn muqrin - ad dirah AR RIYADH 12634 - 6823
    albilad atm 2760 tariq ibn ziyad - ad dirah AR RIYADH 12634 - 6287
    alinma atm 2577 al imam muhammad ibn saud ibn muqrin - ad dirah AR RIYADH 12634 - 6681
    alinma atm 2591 al imam turki ibn abdullah ibn muhammad - ad dirah AR RIYADH 12634 - 6883
    alinma atm 6774 ash shaikh muhammad ibn abdul wahab - ad dirah AR RIYADH 12634 - 2938
    anb atm 6645  - ad dirah AR RIYADH 12634 - 2856
    atm _ national commercial bank 6487 al muqaybirah - ad dirah AR RIYADH 12634 - 2821
    riyadh atm 7172 al batha - ad dirah AR RIYADH 12633 - 3386


Installation
------------

    $ pip install saudiaddress


