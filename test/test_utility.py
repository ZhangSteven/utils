# coding=utf-8
# 

import unittest2
from os.path import join
from datetime import datetime
from utils.utility import currentDir, fromExcelOrdinal, allEquals
from xlrd import open_workbook



class TestUtility(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestUtility, self).__init__(*args, **kwargs)



    def testFromExcelOrdinal(self):
        # just file name
        inputFile = join(currentDir(), 'samples', 'date sample1.xlsx')
        ws = open_workbook(inputFile).sheet_by_index(0)
        self.assertEqual(datetime(1900,1,5), fromExcelOrdinal(ws.cell_value(1, 0)))
        self.assertEqual(datetime(2019,2,28), fromExcelOrdinal(ws.cell_value(2, 0)))
        self.assertEqual(datetime(2015,1,10, hour=18, minute=35) \
                        , fromExcelOrdinal(ws.cell_value(3, 0)))



    def testAllEquals(self):
        self.assertEqual(True, allEquals([]))
        self.assertEqual(True, allEquals(['a']))
        self.assertEqual(True, allEquals([[]]))
        self.assertEqual(False, allEquals(range(2)))
        self.assertEqual(True, allEquals(map(lambda x: 0, range(8))))
