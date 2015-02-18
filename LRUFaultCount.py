#! /usr/bin/python

"""
Count the number of faults when accessing a 
paging system of 4 frames (represented by a list)
"""
class FaultCount:

	pageSystem = None
	numFrames = 0
	
	def __init__(self, frames):
		self.pageSystem = []
		#initialize a blank paging system with 4 empty frames
		empty = self.createPage(None, 0)
		for i in range(frames):
			self.pageSystem.append(empty)
		self.numFrames = frames
		pass
		
		
	def createPage(self, value, accessTime):
		page = {'value':value, 'accessed':accessTime}
		return page
		
	def countFaults(self, accessList):
		faultCount = 0
		#iterate through each page in access list
		numPass = len(accessList)
		for n in range(numPass):
			pageValue = accessList[n]
			found = False
			i = 0
			lruAccessed = self.pageSystem[0]['accessed']
			lruIndex = 0
			#search paging system frames for page & LRU
			while(found == False and i < self.numFrames):
				frame = self.pageSystem[i]
				frameValue = frame['value']
				if(frameValue == pageValue):
					found = True
				else:
					#find LRU by access time (pass num)
					frameAccessed = frame['accessed']
					if(frameAccessed < lruAccessed):
						lruAccessed = frameAccessed
						lruIndex = i
				i = i + 1 
			#if found  
			if(found == True):
				#update access time (pass num)
				frame['accessed'] = n
			#if not
			else:
				#create page for new value
				page = self.createPage(pageValue, n+1)
				#replace lru with page
				self.pageSystem[lruIndex] = page
				#increment fault count
				faultCount = faultCount + 1
		return faultCount
	
	
if(__name__=="__main__"):
	myfault = FaultCount(4)
	print myfault.countFaults([3,4,2,1,4,7,2,5,3,6,1,3])
	yourfault = FaultCount(3)
	print yourfault.countFaults([2,3,4,2,1,3,7,5,4,3])
