# coding=utf-8
# 
# Some utility functions to read Excel in Python.
#
# The toolz and xlrd package must be installed.
#
from toolz.functoolz import compose
from xlrd import open_workbook
from functools import partial
from itertools import takewhile
from utils.iter import pop



def cellValue(ws, row, column):
	"""
	[Worksheet] ws, [Int] row, [Int] column => [String or Float] value

	ws: an xlrd worksheet object
	row, column: the row and column number, starting from 0.

	Returns a value from that row, the value is either a string or a floating
	number.
	"""
	return ws.cell_value(row, column)



def worksheetToLines(ws, startRow=0, numColumns=None):
	"""
	[Worksheet] ws, [Int] startRow, [Int] numColumns => [Iterable] a list of lines
	Where,

	ws: worksheet
	startRow: the starting line to read from
	numColumns: number of columns to read each line

	A generator function, convert the worksheet to a series of lines, where each
	line is a list of values from that row.
	"""
	row = startRow
	while (row < ws.nrows):
		yield rowToList(ws, row, numColumns)
		row = row + 1



def rowToList(ws, row, numColumns=None):
	"""
	[Worksheet] ws, [Int] row, [Int] numColumns => [List] values from the row
	Where,

	ws: worksheet
	row: the row to read from
	numColumns: number of columns to read each line
	"""
	if numColumns == None:
		numColumns = ws.ncols

	return list(map(partial(cellValue, ws, row), range(numColumns)))



def fileToLines(file):
	"""
	[String] file => [Iterable] lines

	Read an Excel file, convert its first sheet into lines, each line is
	a list of the columns in the row.
	"""
	return worksheetToLines(open_workbook(file).sheet_by_index(0))



def getRawPositions(lines):
	"""
	[Iterator] lines => [Iterator] positions

	The the first line as the headers, then convert the remaining lines to 
	dictionaries, with the headers as the keys. It stops reading further lines
	once the first cell of a line is empty (white space).

	NOTE: lines must be an iterator and not a List. Otherwise the 'pop' function's
	side effect wont' work and the first position will be wrong.

	1) If lines is an empty iterator, then return []
	2) If lines contains only the header line, then return []
	3) All white spaces are striped off, either in headers or line values.

	"""
	stripString = lambda x: x.strip() if isinstance(x, str) else x

	getHeaders = compose(
		list
	  , partial(map, stripString)
	  , partial(takewhile, lambda x: x != '')
	)


	toPosition = lambda headers, line: compose(
		dict
	  , lambda line: zip(headers, line)
	  , partial(map, stripString)
	)(line)


	isEmpty = lambda c: isinstance(c, str) and c.strip() == ''

	processHeadnLines = lambda headerLine, lines: \
		map( partial(toPosition, getHeaders(headerLine))
		   , takewhile(lambda line: len(line) > 0 and not isEmpty(line[0]), lines))


	return \
	compose(
		lambda headerLine: [] if headerLine == None else processHeadnLines(headerLine, lines)
	  , pop
	)(lines)
# End of getRawPositions()



"""
	[String] file => [Iterator] positions

	Assume file is an Excel file, this function reads its first worksheet and
	convert the lines from that worksheet to positions.
"""
getRawPositionsFromFile = compose(
	getRawPositions  
  , fileToLines
)