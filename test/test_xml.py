# coding=utf-8
# 

import unittest2
import xml.etree.ElementTree as ET
from utils.xml4me import stripNamespace \
                         , findAllWithoutNamespace \
                         , findWithoutNamespace
from utils.utility import currentDir
from os.path import join



class TestTrade(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTrade, self).__init__(*args, **kwargs)



    def getRoot(self, file):
        """
        Get root element of an XML tree
        """
        tree = ET.parse(file)
        root = tree.getroot()
        return root



    def testStripNamespace(self):
        file = join(currentDir(), 'samples', 'test1.xml')
        tag = self.getRoot(file).tag

        # {http://www.advent.com/SchemaRevLevel758/Geneva}GenevaLoader
        # print(tag)
        self.assertEqual(stripNamespace(tag), 'GenevaLoader')



    def testStripNamespace2(self):
        # This file has no xmlns element
        file = join(currentDir(), 'samples', 'test2.xml')
        tag = self.getRoot(file).tag

        # GenevaLoader
        # print(tag)
        self.assertEqual(stripNamespace(tag), 'GenevaLoader')



    def testFindAllWithoutNamespace(self):
        # Find all the "Buy_New" nodes
        file = join(currentDir(), 'samples', 'test1.xml')
        transactionsNode = self.getRoot(file)[0]
        nodes = findAllWithoutNamespace( transactionsNode \
                                       , 'Buy_New')
        self.assertEqual(sorted(map(portfolioId, nodes)) \
                        , ['19437', '20051', '30001', '40006-D'])



    def testFindWithoutNamespace(self):
        # Find the first "SellShort_New" sub element
        file = join(currentDir(), 'samples', 'test1.xml')
        transactionsNode = self.getRoot(file)[0]
        self.assertEqual(portfolioId(findWithoutNamespace(transactionsNode \
                                                         , 'SellShort_New')) \
                        , '40006-C')



    def testFindWithoutNamespace2(self):
        # If not found, it will return None
        file = join(currentDir(), 'samples', 'test1.xml')
        transactionsNode = self.getRoot(file)[0]
        self.assertEqual(findWithoutNamespace(transactionsNode, 'xxx'), None)




def portfolioId(node):
    """
    [ET node] node => [String] portfolio id

    A node that contains a <Portfolio> sub node looks like:

    <Buy_New>
        <Portfolio>30001</Portfolio>
        <KeyValue>000001</KeyValue>
        ...
    </Buy_New>
    """
    for subElement in node:
        if stripNamespace(subElement.tag) == 'Portfolio':
            return subElement.text

    return ''   # the default