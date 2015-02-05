#! /usr/bin/python

class JessStrings(object):

	def __init__(self):
		pass
	
	
	def oneUnit(self, func, before, after):
		if (func(before) == after):
			return True
		return (before, func(before), False)
	
	
	def unitTesting(self):
		before = "palmtree"
		after = "eertmlap"
		palindromeWord1 = "racecar"
		palindromeWord2 = "aViDa dIvA"
		
		print "Unit test on stringReversal1"
		print self.oneUnit(self.stringReversal1, before, after)
		
		print "Unit test on stringReversal2"
		print self.oneUnit(self.stringReversal2, before, after)
		
		print "Unit test on stringReversal3"
		print self.oneUnit(self.stringReversal3, before, after)
		
		print "Unit test on stringReversal4"
		print self.oneUnit(self.stringReversal4, before, after)
				
		print "Unit test on palindromeFinder1 (Positive)"
		print self.palindromeFinder(palindromeWord1)
		
		print "Unit test2 on palindromeFinder1 (Positive)"
		print self.palindromeFinder(palindromeWord2)
		
		print "Unit test on palindromeFinder1 (Negative)"
		print self.palindromeFinder(before)
		
		print "Unit test on palindromeFinder1 (Negative)"
		print self.palindromeFinder(after)
		
		
	def stringReversal1(self, word):
		"""Practical implementation using python built-ins"""
		return word[::-1]
		
		
	def stringReversal2(self, word):
		"""Using built in reversed"""
		newword = ""
		for c in reversed(word):
			newword = newword + c 
		return newword
		
		
	def stringReversal3(self, word):
		"""String reversal, split and join list to hold the letters"""
		alist = [x for x in word]
		alist2 = alist.reverse()
		return "".join(alist)
		
			
	def stringReversal4(self, word):
		"""
		String reversal using a reversed insert sort of method. 
		"""
		alist = []
		for i in range(len(word)):
			alist.insert(0, word[i])
		return "".join(alist)


	def palindromeFinder(self,word):
		lowerword = word.lower()
		lowerword = lowerword.replace(" ", "")
		reverseword = lowerword[::-1]
		if(reverseword == lowerword):
			return True
		else:
			return False		
		
		
if (__name__ == '__main__'):
	jess = JessStrings()
	jess.unitTesting()
