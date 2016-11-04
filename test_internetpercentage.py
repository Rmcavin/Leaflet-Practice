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

    ##test_get_data_missing_values - test to ensure it can handle a text file
    ##    with values missing or different formatting. One test for each values

    ##test_get_data_delineation - test to ensure it can handle text files that
    ##    aren't white space delineated, for example comma or tab delineations.

    ##test_get_data_inputissues - test to ensure it throws errors in case of
    ##     inproper inputs.

    def test_get_percentage(self):
        self.test_int_users = '25'
        self.test_population = '100'
        self.dictionary = {'China': ['25', '100']}
        getpercentage(self.dictionary)
        self.assertEqual('25.00', self.dictionary['China'][2])

    ##test_get_percentage_wrongvalues - test to ensure error messages occur
    ##  if dividing by zero or if negative numbers are present.

    ##test_get_percentage_nonumbers - test to ensure error messages occur
    ##    if there are letters in the value fields of the text file.

    ##test_find_gaps
    def test_find_gaps(self):
        self.dictionary = {'China':['25','100']}
        self.num_items = 2
        self.assertEqual([], findGaps(self.dictionary, self.num_items))

if __name__ == '__main__':
    unittest.main()
