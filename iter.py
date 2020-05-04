# coding=utf-8
# 
# Utility functions to use with iterators or list processing.
#
# More useful functions can be found in python3 itertools package.
# 
from itertools import dropwhile, chain
from functools import reduce



def divide(key, it):
    """
    [Iterable] it, [Function] key => [Tuple] ([List] true list, [List] others)
    
    Divide an iterable into 2 sub lists based on a key function.
    """
    def accumulate(acc, el):
        if key(el):
            acc[0].append(el)
        else:
            acc[1].append(el)

        return acc


    return reduce(accumulate, it, ([], []))



def pop(it):
	"""
	Non-pure function (it consumes the iterator)

	[Iterable] it => [Object] first element in it, if empty return None.
	"""
	for x in it:
		return x

	return None


# To maintain backward compatibility. Previously the name was "head",
# but a better name for the function is "pop"
head = pop



def firstOf(condition, it):
	"""
	Non-pure function (it consumes the iterator)

	[Iterable] it, [Function] condition => [Object] first element in it that
		satisfies the condition, return None if no such elements or list is
		empty.
	"""
	notSatisfyCondition = lambda x: False if condition(x) else True
	return pop(dropwhile(notSatisfyCondition, it))



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
    This function is kept here for backward compatibility, but we should use
    toolz.functoolz.compose instead.

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



def itemGroup(separator, items):
    """
    A mask for function _itemGroup(), to handle the special situation where
    the input is []. In that case, _itemGroup() returns [[]], but we want
    [], therefore the filter.
    """
    return filter(lambda x: x != [], _itemGroup(separator, items))


def itemGroup2(separator, items):
    return filter(lambda x: x != [], _itemGroup2(separator, items))



def _itemGroup(separator, items):
    """
    A generator function, separate the list of items into a list of groups, divided
    by a separator item.

    [Function] separator, [Iterable] items => groups of items

    Where separator is a function which takes an item as input and tells whether
    an item is a separator item.

    For example,

    The list: [0, 1, 5, 6, 7, 5, 8, 9, 5, 2]
    separator item: 5
    outcome: [[0, 1], [5, 6, 7], [5, 8, 9], [5, 2]]

    """
    group = []

    for item in items:
        if separator(item):
            yield group
            group = [item]
        else:
            group.append(item)

    yield group



def _itemGroup2(separator, items):
    """
    A generator function, separate the list of items into a list of groups, divided
    by a separator item.

    [Function] separator, [Iterable] items => groups of items

    The difference between this version and the itemGroup() is that it skips
    those items at the beginning of the items list before the very first separator
    item.

    For example,

    The list: [0, 1, 5, 6, 7, 5, 8, 9, 5, 2]
    separator item: 5
    outcome: [[5, 6, 7], [5, 8, 9], [5, 2]]
    """
    notSeparator = lambda x: False if separator(x) else True    # negate separator
    group = []

    for item in dropwhile(notSeparator, items):
        if separator(item):
            if group != []:
                yield group
            group = [item]
        else:
            group.append(item)

    yield group



def divideToGroupTF(itTF):
    """
    [Iterator] itTF: an iterator of a series of True and False, like
                        [T, F, F, T, ...], it can be empty

        => [List] groups: a List of groups, where each group is also a List 
            of a leading T with subsequent Fs until the next T or end of itTF
            is reached.

    For example,

    []                  []
    [F, F]              []
    [F, T]              [[T]]
    [F, T, F]           [[T, F]]
    [T]                 [[T]]
    [T, F]              [[T, F]]
    [T, T]              [[T], [T]]
    [T, F, T]           [[T, F], [T]]
    [T, F, T, F, F]     [[T, F], [T, F, F]]
    """
    return reduce( lambda acc, el: \
                        acc + [[el]] if el else acc[:-1] + [acc[-1] + [el]]
                 , dropwhile(lambda el: not el, itTF)
                 , []
                 )



def divideToGroup(func, it):
    """
    A more generalized version.

    [Iterator] it: an iterator of elements
    [Function] func: a function that takes any element from the iterator and
                    evaluates to either True or False

        => [List] groups: a List of groups, where each group is also an List
            with a leading element that evaluates to True followed by items that
            evaluates to False, until the next element that evaluates to True
            or end of the iterator. 

    For example,

    []                  []
    [F, F]              []
    [F, T]              [[T]]
    [F, T, F]           [[T, F]]
    [T]                 [[T]]
    [T, F]              [[T, F]]
    [T, T]              [[T], [T]]
    [T, F, T]           [[T, F], [T]]
    [T, F, T, F, F]     [[T, F], [T, F, F]]
    """
    return \
    reduce( lambda acc, el: \
                        acc + [[el]] if func(el) else acc[:-1] + [acc[-1] + [el]]
          , dropwhile(lambda el: not func(el), it)
          , []
    )



if __name__ == '__main__':
    # even = lambda x: x%2 == 0
    # print(divide(even, range(5)))

    itTF = [False, True, False, True]
    output = divideToGroups(itTF)
    if output == []:
        print(output)
    else:
        for x in output:
            print(x)
