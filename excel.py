# coding=utf-8
# 
# Some utility functions to read Excel in Python.
#
# The xlrd package must be installed because the worksheet object is
# expected to be a xlrd worksheet object.
#
from functools import partial



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
