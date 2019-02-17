# coding=utf-8
# 

import unittest2
from utils.iter import head, numElements



class TestIter(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIter, self).__init__(*args, **kwargs)

    def testHead(self):
        r = range(10)
        self.assertEqual(0, head(r))
        self.assertEqual(0, head(r))    # a range object NOT consumed like
                                        # normail iterable

        r2 = map(lambda x: 2*x, r)
        self.assertEqual(0, head(r2))
        self.assertEqual(2, head(r2))   # the iterator (map object) consumed



    def testNumElements(self):
        self.assertEqual(0, numElements([]))

        r = range(10)
        self.assertEqual(10, numElements(r))
        self.assertEqual(10, numElements(r))    # range object, like a list,
                                                # not consumed

        r2 = map(lambda x: 2*x, r)
        self.assertEqual(10, numElements(r2))
        self.assertEqual(0, numElements(r2))    # the iterator (map object) 
                                                # consumed