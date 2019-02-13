# coding=utf-8
# 
# Some of the functions to use with iterators or list processing.
# 

def head(it):
	"""
	[Iterable] it => [Object] first element in it, if empty return None
	
	This function is not a pure function, because it consumes the iterator.
	"""
	for x in it:
		return x

	return None



def numElements(it):
	"""
	[Iterable] it => [Integral] number of elements in an interable (it).
	
	This function is not a pure function, because it consumes the iterator.

	The idea comes from:
	https://stackoverflow.com/questions/3345785/getting-number-of-elements-in-an-iterator-in-python
	"""
	return sum([1 for _ in it])



if __name__ == '__main__':
	pass

	

