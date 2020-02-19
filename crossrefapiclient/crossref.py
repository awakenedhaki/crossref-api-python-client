import requests


class CrossRef(object):
    URL = 'https://api.crossref.org/'

    def request(self, endpoint, doi):
        url = self._build_url(endpoint, doi)

    def _build_url(self, doi):
        return f'{URL}/{doi}'