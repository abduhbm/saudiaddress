# -*- coding: utf-8 -*-
from future.utils import python_2_unicode_compatible


@python_2_unicode_compatible
class Model(object):
    """
    base class from which all Nation Address models will initiate
    """

    def __init__(self, **kwargs):
        self.param_defaults = {}

    @classmethod
    def from_json(cls, data, **kwargs):
        """
        Create a new instance from a JSON dict
        """
        data_copy = data.copy()
        if kwargs:
            for key, value in kwargs.items():
                data_copy[key] = value

        c = cls(**data_copy)
        c._json = data
        return c


class Address(Model):
    """
    A class representation of the Address component
    """

    def __init__(self, **kwargs):
        self.param_defaults = {
            'Title': None,
            'Address1': None,
            'Address2': None,
            'ObjLatLng': None,
            'BuildingNumber': None,
            'Street': None,
            'District': None,
            'City': None,
            'PostCode': None,
            'AdditionalNumber': None,
            'UnitNumber': None,
            'RegionName': None,
            'IsPrimaryAddress': None,
            'Latitude': None,
            'Longitude': None,
        }
        for param, default in self.param_defaults.items():
            value = kwargs.get(param, default)
            value = value if value else ''
            setattr(self, param, value)

    def __repr__(self):
        return u"{building} {street} - {dist} {city} {post_code} - {add_no}".format(building=self.BuildingNumber,
                                                                                    street=self.Street,
                                                                                    dist=self.District, city=self.City,
                                                                                    post_code=self.PostCode,
                                                                                    add_no=self.AdditionalNumber)


class Region(Model):
    """
    A class representation of the Region component
    """

    def __init__(self, **kwargs):
        self.param_defaults = {
            'Id': None,
            'Name': None,
        }
        for param, default in self.param_defaults.items():
            value = kwargs.get(param, default)
            value = value if value else ''
            setattr(self, param, value)

    def __repr__(self):
        return u"Region (ID={id}, Name={name})".format(id=self.Id, name=self.Name)


class City(Model):
    """
    A class representation of the City component
    """

    def __init__(self, **kwargs):
        self.param_defaults = {
            'Id': None,
            'Name': None,
        }
        for param, default in self.param_defaults.items():
            value = kwargs.get(param, default)
            value = value if value else ''
            setattr(self, param, value)

    def __repr__(self):
        return u"City (ID={id}, Name={name})".format(id=self.Id, name=self.Name)


class District(Model):
    """
    A class representation of the District component
    """

    def __init__(self, **kwargs):
        self.param_defaults = {
            'Id': None,
            'Name': None,
        }
        for param, default in self.param_defaults.items():
            value = kwargs.get(param, default)
            value = value if value else ''
            setattr(self, param, value)

    def __repr__(self):
        return u"District (ID={id}, Name={name})".format(id=self.Id, name=self.Name)


class ServiceCategory(Model):
    """
    A class representation of the Service Category and sub-Category component
    """

    def __init__(self, **kwargs):
        self.param_defaults = {
            'Id': None,
            'Name': None,
        }
        for param, default in self.param_defaults.items():
            value = kwargs.get(param, default)
            value = value if value else ''
            setattr(self, param, value)

    def __repr__(self):
        return u"Category (ID={id}, Name={name})".format(id=self.Id, name=self.Name)


class ServiceSubCategory(Model):
    """
    A class representation of the Service Category and sub-Category component
    """

    def __init__(self, **kwargs):
        self.param_defaults = {
            'Id': None,
            'Name': None,
        }
        for param, default in self.param_defaults.items():
            value = kwargs.get(param, default)
            value = value if value else ''
            setattr(self, param, value)

    def __repr__(self):
        return u"Sub-Category (ID={id}, Name={name})".format(id=self.Id, name=self.Name)


class ResultSet(object):
    """
    A holder class for base model instances
    """

    def __init__(self, records, count):
        self.records = records
        self.count = count
