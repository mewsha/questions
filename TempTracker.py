class TempTracker(object):
  """Tracks a set of temperatures and provides utility funtions"""
  
  def __init__(self):
    """ Init an empty temperature tracker"""
    self._tempHistory = []
    
  def insert(self, newTemp):
    """ Insert new valid temperatures """
    try:
      if type(newTemp) is int:
        self._tempHistory.append(newTemp)
        return (newTemp, None)
      else:
        return (1, "unable to insert %s- must be int." % newTemp)
    except Exception as e:
      return (1, e)
    
  def get_max(self):
    """ Get the highest temperature recorded"""
    try:
      if len(self._tempHistory) > 0:
        maxTemp = self._tempHistory[0]
        for x in self._tempHistory:
          if x > maxTemp:
            maxTemp = x
        return (maxTemp, None)
      else:
        return (1, "Temperature history is empty.")
    except (IndexError, Exception) as e:
      return (1, e)
  
  def get_min(self):
    """ Get the lowest temperature recorded"""
    try:
      if len(self._tempHistory) > 0:
        minTemp = self._tempHistory[0]
        for x in self._tempHistory:
          if x < minTemp:
            minTemp = x
        return (minTemp, None)
      else:
        return (1, "Temperature history is empty.")
    except (IndexError, Exception) as e:
      return (1, e)
      
        
  def get_mean(self):
    """ Get the mean temperature recorded"""
    try:
      if len(self._tempHistory) > 0:
        meanTemp = 0
        countTemps = float(len(self._tempHistory))
        for num in self._tempHistory:
            meanTemp += num
        meanTemp = meanTemp/countTemps
        return (meanTemp, None)
      else:
        return (1, "Temperature history is empty.")
    except Exception as e:
      return (1,e)

  def get_history(self):
    """Print history"""
    print self._tempHistory
    

if __name__ == "__main__":
  tempTrack = TempTracker()
  tempTrack.insert("notatemp")
  for x in range(-10,10,2):
    print tempTrack.insert(x)
  max = tempTrack.get_max()
  print "Max is:", max[0]
  min = tempTrack.get_min()
  print "Min is:", min[0]
  mean = tempTrack.get_mean()
  print "Mean is:", mean[0]
