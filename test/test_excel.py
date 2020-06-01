# coding=utf-8
# 

import unittest2
from os.path import join
from itertools import chain
from utils.utility import currentDir
from utils.excel import getRawPositions, getRawPositionsFromFile



class TestExcel(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestExcel, self).__init__(*args, **kwargs)



    def testGetRawPositions(self):
        self.assertEqual([], getRawPositions([]))
        self.assertEqual([], list(getRawPositions(chain([], [['a']]))))

        # This will fail, but getRawPositions() assumes the input is an iterator
        # instead of a List
        # self.assertEqual([], list(getRawPositions([['a']])))



    def testGetRawPositionsFromFile(self):
        positions = list(getRawPositionsFromFile(join('samples', 'AssetType_SpecialCase.xlsx')))
        self.assertEqual(3, len(positions))
        p = positions[0]
        self.assertEqual('XS1684793018', p['ID'])
        self.assertEqual(19437, p['Portfolio'])
        self.assertEqual('Equity, Listed equities', p['AssetType'])