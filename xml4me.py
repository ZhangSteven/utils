# coding=utf-8
# 
# When using xml.etree.ElementTree to parse XML files, we will encounter
# some common problems, here are functions to handle them.
# 

from utils.iter import head
import re



def stripNamespace(tag):
	"""
	[String] tag => [String] tag without XML name space

	When parsing the XML tree, an XML node's tag may looks like:

	{http://www.advent.com/SchemaRevLevel758/Geneva}Buy_New

	Where {http://xxx} is the name space of the XML file, "Buy_New" is the
	tag.

	The function removes the name space prefix and returns the tag after it.
	"""
	m = re.match('\{.*\}(.*)', tag)
	if m != None:
		return m.group(1)
	else:
		return tag



def findAllWithoutNamespace(parentNode, tag):
	"""
	[ET node] node, [String] tag => [Iterable] sub nodes with the tag

	Find elements with a tag which are direct children of the parentNode.

	It's similar to the findAll() function in elementTree mode, but the
	difference is that when we do comparison, we ignore the name space. This
	can be handy when the XML has one and only name space in it. 
	"""
	def rightNode(node):
		if stripNamespace(node.tag) == tag:
			return True
		else:
			return False


	return filter(rightNode, parentNode)



def findWithoutNamespace(parentNode, tag):
	"""
	[ET node] node, [String] tag => [ET node] sub node with the tag

	Similar to findAllWithoutNamespace(), but just return the first node
	that matches.
	"""
	return head(findAllWithoutNamespace(parentNode, tag))




if __name__ == '__main__':
	pass

	

