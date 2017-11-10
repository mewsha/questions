"""test data"""
myArray = [[1,2,[3]],4] #deep list
myArray2 = [1,2,[3,4],5,[6]] #broad list
myArray3 = [1] #one item list
myArray4 = [] #empty list
myArray5 = [['a'], [1, 'bad']] #bad list
myArray6 = [{}, 5.6] #also bad list
testLists = [myArray, myArray2, myArray3, myArray4, myArray5, myArray6]

def combineArray(array, combined):
  """ Unnest a list into a single depth list
  and store into a passed in variable with
  error checking"""
  try:
    for x in array:
      if type(x) is int:
        combined.append(x)
      elif type(x) is list:
        if len(x) > 1:
          combineArray(x, combined)
        else:
          if type(x[0]) is int:
            combined.append(x[0])
      else:
        raise RuntimeError("Unable to unpack nonintegers")
  except (RuntimeError, Exception) as e:
    print "unable to combine- %s, %s" % (e, x)
    return 1
  return 0

if __name__ == "__main__":
  #unnest lists into a passed in variable, robust
  for alist in testLists:
    result = []
    combineArray(alist, result)
    print "list: %-25s answer:%-25s" % (alist, result)
    
