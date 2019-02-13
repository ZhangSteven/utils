# coding=utf-8
# 
from os import listdir
from os.path import isfile, isdir, join
import ntpath



def getFiles(directory, withDir=None):
	"""
	[String] directory, [Bool] withDir => [List] file names under that 
		directory. Sub folders are not included.

	if the function is called without the second parameter 'withDir', then 
	file names are without directory, otherwise full path file names are 
	returned.
	"""
	if withDir == None:
		return [f for f in listdir(directory) if isfile(join(directory, f))]
	else:
		return [join(directory, f) for f in listdir(directory) if isfile(join(directory, f))]



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
	head, tail = ntpath.split(file)
	return tail



if __name__ == '__main__':
	print(getFiles('.'))		# show local directory files
	print(getSubFolders('.'))	# show local sub directories