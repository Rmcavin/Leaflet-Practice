##a test for internetpercentage.py
##Author: Rachel Cavin
##Date: 11/1/2016

import unittest
from internetpercentage import getdata, getpercentage, findGaps

class TestInternetPercentage(unittest.TestCase):

    def test_get_data(self):
        self.list1 = ['1      China      626600000']
        self.list2 = ['1      China       1373541278']
        self.dictionary = {}
        getdata(self.list1, self.dictionary)
        getdata(self.list2, self.dictionary)
        self.assertEqual(self.dictionary, {'China': ['626600000','1373541278']})

    def test_get_percentage(self):
        self.test_int_users = '25'
        self.test_population = '100'
        self.dictionary = {'China': ['25', '100']}
        getpercentage(self.dictionary)
        self.assertEqual('25.00', self.dictionary['China'][2])

if __name__ == '__main__':
    unittest.main()
