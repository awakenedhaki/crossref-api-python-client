from crossrefapiclient import Works
from pprint import pprint

if __name__ == '__main__':

    # Conceptualization of works endpoint
    works = Works()
    works.get(doi='10.1037/0003-066X.59.1.29')
    # works.filter(filterName = 'filterValue').sample(100)
    # works.query(author = "authorName").row(2)
    pprint(works.execute())

    # # Conceptualization of funders endpoint
    # funders = CrossRef('funders')
    # funders.get(funderId = '{funderId}').works()
    # funders.get(funderId = '{funderId}').works(doi = '{doi}')