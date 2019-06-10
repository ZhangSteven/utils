# coding=utf-8
# 

import unittest2
from utils.iter import pop, numElements, firstOf, itemGroup, itemGroup2



class TestIter(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIter, self).__init__(*args, **kwargs)

    def testPop(self):
        r = range(10)
        self.assertEqual(0, pop(r))
        self.assertEqual(0, pop(r))    # a range object NOT consumed like
                                        # normail iterable

        r2 = map(lambda x: 2*x, r)
        self.assertEqual(0, pop(r2))
        self.assertEqual(2, pop(r2))   # the iterator (map object) consumed



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



    def testFirstOf(self):
        condition = lambda x: x > 4

        L = []
        self.assertEqual(None, firstOf(condition, L))

        L = [1, 3, 5, 2, 6, 3]
        self.assertEqual(5, firstOf(condition, L))

        L = [1, 2, 3]   # non of the items satifies
        self.assertEqual(None, firstOf(condition, L))



    def testItemGroup(self):
        separator = lambda x: x ==5
        self.assertEqual(list(itemGroup(separator, [])), [])
        self.assertEqual(list(itemGroup(separator, [0, 1])), [[0, 1]])
        self.assertEqual(list(itemGroup(separator, [0, 1, 5])), [[0, 1], [5]])
        self.assertEqual(list(itemGroup(separator, [5, 2])), [[5, 2]])
        self.assertEqual(list(itemGroup(separator, [0, 1, 5, 6, 7]))
                        , [[0, 1], [5, 6, 7]])
        self.assertEqual(list(itemGroup(separator, [0, 1, 5, 6, 7, 5, 5, 2]))
                        , [[0, 1], [5, 6, 7], [5], [5, 2]])



    def testItemGroup2(self):
        separator = lambda x: x ==5
        self.assertEqual(list(itemGroup2(separator, [])), [])
        self.assertEqual(list(itemGroup2(separator, [0, 1])), [])
        self.assertEqual(list(itemGroup2(separator, [0, 1, 5])), [[5]])
        self.assertEqual(list(itemGroup2(separator, [5, 2])), [[5, 2]])
        self.assertEqual(list(itemGroup2(separator, [0, 1, 5, 6, 7]))
                        , [[5, 6, 7]])
        self.assertEqual(list(itemGroup2(separator, [0, 1, 5, 6, 7, 5, 5, 2]))
                        , [[5, 6, 7], [5], [5, 2]])