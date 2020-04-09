import requests

from abc import ABCMeta
from uritemplate import URITemplate
from urllib.parse import urlencode, urljoin

from crossrefapiclient.utils import (
    validate,
    prefix_query,
    create_logger,
    _filter_builder
)

# CONSTANTS ===================================================================
# . Crossref available version
VERSION = 'v1'
# . URI template for CrossRef API
BASE = URITemplate('https://api.crossref.org/{version}/{resource}/')

# LOGGING =====================================================================
logger = create_logger(__name__)

# CLASSES =====================================================================

# TODO: header specification (adding mailto)
# TODO: looking into potential request errors


class MetaResource(ABCMeta):
    '''
    Metaclass for Crossref Resources.

    Sets the `resources` attribute with __new__ constructor from class name.
    '''
    def __new__(cls, name, bases, body):
        body['resource'] = name.lower()
        return super().__new__(cls, name, bases, body)


class Resource(metaclass=MetaResource):
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

    def __init__(self, debug = False):
        self.url = BASE.expand({
            'version': VERSION,
            'resource': self.resource
        })
        self.debug = debug
        if self.debug:
            logger.info(
                f'{self.__class__.__name__} URL has been set to {self.url}')

        self.params = {}

    def execute(self):
        '''
        Sends a GET request to CrossRef API.

        Returns
        -------
        A JSON object.
        '''
        params = urlencode(self.params)
        url = self.url + f'?{params}' if params else self.url

        if self.debug:
            logger.info(f'Request being sent to {url}')

        with requests.get(url) as r:
            logger.warning(f'Request status code: {r.status_code}')
            r.raise_for_status()
            return r.json()

    def get(self, identifier):
        self.url = urljoin(self.url, f'{identifier}/')
        if self.debug:
            logger.info(f'Identifier: {identifier}')
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

    def reset(self):
        self.url = BASE.expand({
            'version': VERSION,
            'resource': self.resource
        })


    def __repr__(self):
        attrs = ', '.join([f'{k}={v}' for k, v in vars(self).items()])
        return f'{self.__class__.__name__}({attrs})'


class CombinationResource(Resource):
    def works(self):
        self.url = urljoin(self.url, 'works/')
        logger.info(f'Combining with /works: {self.url}')
        return self


class Works(Resource):
    pass


class Funders(CombinationResource):
    pass


class Members(CombinationResource):
    pass


class Journals(CombinationResource):
    pass


class Licenses(CombinationResource):
    pass


class Types(CombinationResource):
    pass


class Prefixes(CombinationResource):
    pass
