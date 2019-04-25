# coding=utf-8
# 
# Utility functions to use with iterators or list processing.
#
# More useful functions can be found in python3 itertools package.
# 

def head(it):
	"""
	[Iterable] it => [Object] first element in it, if empty return None
	
	This function is not pure, because it changes the input, i.e., consumes 
	the iterator.
	"""
	for x in it:
		return x

	return None



def numElements(it):
	"""
	[Iterable] it => [Integral] number of elements in an interable (it).
	
	This function is not pure, because it changes the input, i.e., consumes 
	the iterator.
	
	The idea comes from:
	https://stackoverflow.com/questions/3345785/getting-number-of-elements-in-an-iterator-in-python
	"""
	# return sum([1 for _ in it])
	return sum(map(lambda _: 1, it))



def compose(*funcs):
	"""
	[List] list of functions => [Function Object] a new function that is the
		compose of all the functions.

	compose(f, g, ...)(x) = f(g(...(x)))

	The code come from "Function Programming in Python", Chapter 4.

	There are some other libraries that contain a similar function.
	"""
	def inner(data, func=funcs):
		result = data
		for f in reversed(funcs):
			result = f(result)

		return result

	return inner




if __name__ == '__main__':
	pass

	

