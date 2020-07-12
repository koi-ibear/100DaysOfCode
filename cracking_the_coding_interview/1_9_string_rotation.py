"""
1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of" erbottlewat").
"""
def isRotation(s1, s2):
	"""
	function that checks if s1 is a rotation of s2
	"""
	l1 = len(s1)
	l2 = len(s2)
	if l1==l2:
		if isSubstring(s1, s2*2):
			return True
	return False


## test case
isRotation('cdab', 'abcd')
isRotation('bbab', 'abcd')
"""
💡
1. string buffer in Python
str1+str2+...: O(n*n)
''.join([str1, str2, ...]): O(n)
str*k: O(n)
"""	

# ==============helper function================
def isSubstring(s1, s2):
	"""
	function that checks if s1 is a substring of s2
	"""
	if s2.count(s1) > 0:
		return True
	return False

def isSubstring(s1, s2):
	if s2.find(s1) > -1:
		return True
	return False


def isSubstring(s1, s2):
	l1, l2 = len(s1), len(s2)
	if l1 > l2:
		return False
	i = 0
	for j in range(l2):
		if i == l1:
			return True
		if i > 0 and s1[i] != s2[j]:
			i = 0
		if s1[i] == s2[j]:
			i += 1
			if i > l1:
				break
	if i < l1:
		return False
	return True

# test case
isSubstring('abc', 'bcbca')
isSubstring('a', 'abc')
isSubstring('abc', 'bcab')
isSubstring('abc', 'ababc')

