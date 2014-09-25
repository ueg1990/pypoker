import unittest
from pypoker import Result

class ResultTestCase(unittest.TestCase):
    '''
    Tests for the Result class
    '''
    def setUp(self):
        self.result = Result(100, 'Test Message')

    def test_result_rank_message(self):
    	self.assertEqual([self.result.rank, self.result.message], [100, 'Test Message'])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
