class Problem_0002:
  
  def run(self):    
    result = 0
    currentNumber = 1
    nextNumber = 2
    sumOfEvenTerms = 0;
    
    #print "seq: {0}".format(currentNumber)
    
    while nextNumber < 4000000:
      #print "seq: {0}".format(nextNumber)
      #Check for even value term on the sequence to add
      if nextNumber % 2 == 0:
        sumOfEvenTerms += nextNumber
      
      #Standard temp value swap
      result = (currentNumber + nextNumber)
      currentNumber = nextNumber
      nextNumber = result
      
    print "Problem 2 Answer: {0}".format(sumOfEvenTerms);
    