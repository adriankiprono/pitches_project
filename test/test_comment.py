import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    test class that test the behaviour of the Review class
    '''
    def setUp(self):
        '''
        Set up method that runs before every test case
        '''
        self.new_review =Review(1234,'Python Must Be Crazy','https://image.tmdb.org/t/p/w500/','good movie but very long')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))