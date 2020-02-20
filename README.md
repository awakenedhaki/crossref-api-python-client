# crossref-api-python-client

A python wrapper for the Crossref REST API.

THIS LIBRARY IS CURRENTLY UNDERDEVELOPMENT.

## Introduction

This library provides a pure Python interface for the [Crossref REST API](https://github.com/CrossRef/rest-api-doc). [Crossref](https://www.crossref.org/) is an official Digital Object Identifier (DOI) Registration Agency of the International DOI Foundation. Crossref allows for easy retrieval of metadate from a variety of content types (academic papers, books, conference proceedings, etc).

## Installation

`crossref-api-python-client` can be installed via PyPi.

```zsh
$ pip install crossref-api-python-client
```

Or, you can clone this repository. If cloning the repository, you should may also wish to install [Poetry](https://github.com/python-poetry/poetry), a depedency management system.

```zsh
$ git clone https://github.com/awakenedhaki/crossref-api-python-client.git
```

Onces the repository and `poetry` are installed, run the following command within the repository.

```zsh
$ poetry install
```

## Usage

Each Crossref resource is represented as its own python object. As such, you can import any of the following endpoints:

- `Works`
- `Funders`
- `Members`
- `Prefixes`
- `Types`
- `Journals`

```python
>>> from crossrefapiclient import Works
>>> works = Works()
>>> works.get(doi = '10.1037/0003-066X.59.1.29')
{'message': {'DOI': '10.1037/0003-066x.59.1.29',
             'ISSN': ['1935-990X', '0003-066X'],
             'URL': 'http://dx.doi.org/10.1037/0003-066x.59.1.29',
             'alternative-id': ['2004-10043-004', '14736318'],
             ...}
 'message-type': 'work',
 'message-version': '1.0.0',
 'status': 'ok'}
```

## TODO

- Complete Crossref classes

    - `Works` still does not have all the methods that are specified in the Crossref doc.
    - Do we want all methods from the original docs?

- Complete README.md

- Post of PyPi