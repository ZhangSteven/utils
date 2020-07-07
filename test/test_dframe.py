# coding=utf-8
# 

import unittest2
from utils.dframe import dictListToDataFrame



class TestDFrame(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDFrame, self).__init__(*args, **kwargs)



    def testDictListToDataFrame(self):
        # just file name
        df = dictListToDataFrame([ {'x': 88, 'y': 99}
                                 , {'x': 101, 'y': 120}
                                 , {'x': 111, 'y': 132}
                                 ])

        self.assertEqual(3, len(df))
        self.assertEqual(99, df.iloc[0]['y'])
        self.assertEqual(101, df.iloc[1]['x'])
        self.assertEqual(132, df.iloc[2]['y'])