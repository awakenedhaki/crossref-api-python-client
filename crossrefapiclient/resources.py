import json
import requests

from abc import abstractmethod, ABCMeta
from uritemplate import URITemplate
from urllib.parse import urlencode, urljoin

from crossrefapiclient.utils import validate, prefix_query

# CONSTANTS ===================================================================
# . CrossRef available version
VERSION = 'v1'
# . URI template for CrossRef API
BASE = URITemplate('https://api.crossref.org/{version}/{resource}/')

# CLASSES =====================================================================

class MetaResource(ABCMeta):
    '''
    Metaclass for CrossRef Resources.

    Sets the `resources` attribute with __new__ constructor from class name.
    '''
    def __new__(cls, name, bases, body):
        body['resource'] = name.lower()
        return super().__new__(cls, name, bases, body)


class Resource(metaclass=ABCMeta):
    '''
    Abstract class for a CrossRef Resource.

    Currently available resources in the CrossRef API are:
        - /works
        - /funders
        - /members
        - /types
        - /licenses
        - /journals
    '''
    def __init__(self):
        self.url = BASE.expand({
            'version': VERSION,
            'resource': self.resource
            })
        self.params = {}

    @abstractmethod
    def get(self, identifier):
        return

    @abstractmethod
    def query(self, **kwargs):
        pass

    @abstractmethod
    def filter(self, **kwargs):
        pass

    @abstractmethod
    def sort(self, **kwargs):
        pass

    def execute(self):
        '''
        Sends a GET request to CrossRef API.

        Returns
        -------
        A JSON object.
        '''
        params = urlencode(self.params)
        url = self.url + f'?{params}'
        with requests.get(url) as r:
            return r.json()


class Works(Resource, metaclass=MetaResource):
    '''
    Python object for /works CrossRef endpoint.
    '''

    def get(self, doi):
        self.url = urljoin(self.url, doi)
        return self

    @validate()
    @prefix_query
    def query(self, **kwargs):
        self.params.update(**kwargs)
        return self

    @validate('{resource}')
    def filter(self, **kwargs):
        self.params.update({
            'filter': _filter_builder(**kwargs)
        })
        return self

    @validate()
    def sort(self, sorter, order='asc'):
        self.params.update({
            'sort': sorter,
            'order': order
        })


def _filter_builder(**kwargs):
    '''
    Formats filters into a string of comma separated parameters.
    '''
    field = [f'{filter_name}:{value}' for filter_name, value in kwargs.items()]
    return ','.join(field)