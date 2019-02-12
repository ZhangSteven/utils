# coding=utf-8
# 
from os import listdir
from os.path import isfile, isdir, join
import ntpath



def getFiles(directory):
	"""
	[String] directory => [List] file names under that directory

	sub folders are not included
	"""
	return [f for f in listdir(directory) if isfile(join(directory, f))]



def getSubFolders(directory):
	"""
	[String] directory => [List] sub folder names under that directory

	files are not included
	"""
	return [f for f in listdir(directory) if isdir(join(directory, f))]



def stripPath(file):
	"""
	[String] file name (with or without full path) => [String] file name 
		without path

	The code snippet comes from:

	https://stackoverflow.com/a/8384788/3331297
	"""
    head, tail = ntpath.split(path)
    return tail



if __name__ == '__main__':
	print(getFiles('.'))		# show local directory files
	print(getSubFolders('.'))	# show local sub directories