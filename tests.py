import unittest

from crossrefapiclient import Works

class WorksTest(unittest.TestCase):

    def setUp(self):
        self.URL = 'https://api.crossref.org/v1/works/'
        self.DOI = '10.1037/0003-066X.59.1.29'
        self.works = Works()
        return super().setUp()
    
    def test_url(self):
        self.assertEquals(self.URL, self.works.url)

    def test_create_url(self):
        self.works.get(self.DOI)
        self.assertEquals(f'{self.URL}{self.DOI}/', self.works.url)


    @unittest.skip('Looking into comparing deeply nested dictionaries')
    def test_execute(self):
        pass
        
if __name__ == '__main__':
    unittest.main()