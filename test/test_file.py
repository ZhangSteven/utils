# coding=utf-8
# 

import unittest2
from os.path import join
from utils.utility import currentDir
from utils.file import getFiles



class TestFile(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFile, self).__init__(*args, **kwargs)


    def testGetFiles(self):
        files = getFiles(join(currentDir(), 'test', 'temp'))
        self.assertEqual(sorted(files), ['my document.docx', 'test1.txt'])



    def testGetFiles2(self):
        files = getFiles(join(currentDir(), 'test', 'temp'), True)
        filelist = [join(currentDir(), 'test', 'temp', 'my document.docx') \
                    , join(currentDir(), 'test', 'temp', 'test1.txt')]
        self.assertEqual(sorted(files), filelist)
