#! /usr/bin/python

class WordScore(object):
	
	def oneUnit(self, func, word, score):
		myscore = func(word)
		if (myscore == score):
			return True
		return False
	
	def unitTesting(self):
		print "Testing 'Jaba The Tubby'"
		print self.oneUnit(self.scoreWord, "Jaba The Tubby", 22)
		
		print "Testing 'use THE force'"
		print self.oneUnit(self.scoreWord, "use THE force", 16)
		
		
	def scoreWord(self, word):
		"""returns: the score for a word"""
		result = 0
		#lowercase the word
		myword = word.lower()
		#iterate each letter
		for c in myword:
			#score letters
			points = self.scoreLetter(c)
			#add up results
			result = result + points
		#return results
		return result
		
	def scoreLetter(self, letter):
		"""returns: the score for a letter"""
		#set score to 0
		score = 0		
		#is it a f
		if(letter == 'f'):
			#score is 3
			score = 3
		#is it a j
		if(letter == 'j'):
			#score is 6
			score = 6
		#is it a x
		if(letter == 'x'):
			#score is 12
			score = 12
		#is it a aieo
		if(letter == 'a' or letter == 'i' or letter == 'e'
		   or letter == 'o'):
			#score is 2
			score = 2
		#is it a t
		if(letter == 't'):
			#score is 5
			score = 5
		#return the score
		return score
	
if(__name__=="__main__"):
	mywordscore = WordScore()
	mywordscore.unitTesting()
