# coding=utf-8
# 

import csv, os
from datetime import datetime, timedelta
from functools import partial
from operator import getitem



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



def writeCsv(fileName, rows, **kwargs):
	"""
	[String] fileName (output file name, full path),
	[Iterable] rows (each row is a list of items),
	[Key-Value Pairs] kwargs: such as

		delimiter=',' (the default)
		quotechar='"'\
		quoting=csv.QUOTE_NONNUMERIC
	"""
	with open(fileName, 'w', newline='') as csvfile:
		file_writer = csv.writer(csvfile, **kwargs)
		for row in rows:
			file_writer.writerow(row)

		return fileName



def currentDir():
	"""
	Get the absolute path to the directory where this module is in.

	This piece of code comes from:

	http://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python
	"""
	return os.path.dirname(os.path.abspath(__file__))



def dictToValues(keys, d):
	"""
	[List] keys, [Dictionary] d => [Iterator] values

	retrieve the list of values corresponding to the keys from the dictionary.
	"""
	return map(partial(getitem, d), keys)



"""
	[Dictionary] d1, [Dictioanry] d2
		=> [Dictioanry] d (merged dictionary, with all the key value pairs
							from d1 and d2. If a key is both in d1 and d2,
							the d2 value will overwrite d1)
"""
mergeDict = lambda d1, d2: {**d1, **d2}



def allEquals(it):
	"""
	[Iterable] it => [Bool] whether all elements are equal

	Where "it" is iterable, for example a range object or a map object.

	Note iterable and iterator are different. iterable is a property, meaning
	if an object is iterable, we can use for or map on that object.

	While iterator is an interface, meaning we can apply next() when an object
	is an iterator.

	Not all iterable objects are iterator, say a range() object is not.

	The function returns True if there is zero or only one element in the
	iterable. Otherwise it uses the == operator to tell whether all of them
	are equal.

	The idea of this function comes from here:

	Check if all elements in a list are identical
	https://stackoverflow.com/a/3844832
	"""
	iterator = iter(it)
	try:
		first = next(iterator)
	except StopIteration:
		return True

	return all(first == el for el in iterator)