# coding=utf-8
# 
from os import listdir
from os.path import isfile, isdir, join



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




if __name__ == '__main__':
	print(getFiles('.'))		# show local directory files
	print(getSubFolders('.'))	# show local sub directories