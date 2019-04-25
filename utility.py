# coding=utf-8
# 

import csv, os
from datetime import datetime, timedelta



def fromExcelOrdinal(ordinal, _epoch0=datetime(1899, 12, 31)):
	"""
	[Float] ordinal => [Datetime] date

	In Excel, an date is represented by a float number (ordinal), where the
	integral part represents the date and the decimal part represents the time
	of that day. This function converts that number to a python datetime object.

	Code sample comes from:

	https://stackoverflow.com/questions/29387137/how-to-convert-a-given-ordinal-number-from-excel-to-a-date
	"""
	if ordinal > 59:
		ordinal -= 1
	return (_epoch0 + timedelta(days=ordinal)).replace(microsecond=0)



def writeCsv(fileName, rows):
	with open(fileName, 'w', newline='') as csvfile:
		file_writer = csv.writer(csvfile)
		for row in rows:
			file_writer.writerow(row)



def currentDir():
	"""
	Get the absolute path to the directory where this module is in.

	This piece of code comes from:

	http://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python
	"""
	return os.path.dirname(os.path.abspath(__file__))
