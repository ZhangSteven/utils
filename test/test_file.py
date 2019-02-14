# coding=utf-8
# 

import unittest2
from os.path import join
from utils.utility import currentDir
from utils.file import getFiles, getSubFolders, stripPath



class TestFile(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFile, self).__init__(*args, **kwargs)



    def testGetFiles(self):
        # just file name
        files = getFiles(join(currentDir(), 'test', 'temp'))
        self.assertEqual(sorted(files), ['my document.docx', 'test1.txt'])



    def testGetFiles2(self):
        # file name with full path
        files = getFiles(join(currentDir(), 'test', 'temp'), True)
        filelist = [join(currentDir(), 'test', 'temp', 'my document.docx') \
                    , join(currentDir(), 'test', 'temp', 'test1.txt')]
        self.assertEqual(sorted(files), filelist)



    def testStripPath(self):
        self.assertEqual(sorted(getSubFolders(join(currentDir(), 'test', 'temp'))) \
                        , ['folder 1', 'folder 2'])



    def testStripPath(self):
        paths = [ 'C:\\Intel\\Logs.txt' \
                , 'C:\\temp\\Reconciliation\\' \
                , '/usr/etc/hello.py' \
                , '/usr/config/']
        self.assertEqual(list(map(stripPath, paths))
                        , ['Logs.txt', '', 'hello.py', ''])