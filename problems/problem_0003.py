#
#Largest prime factor
#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
#
class Problem_0003:
  
  def run(self):
    #NOTE: A prime facor is a positive integer that is greater than one and can only be divided evenly by 1 or itself
    #Apprach: 
    #  Use recursion to create prime factor tree, then grab the highest factor at the end
    #  
    
    numberToBeFactored = 600851475143
    defaultPrimeFactor = numberToBeFactored
    answer = self.calcHighestPrimeFactor(defaultPrimeFactor, numberToBeFactored)
    print "Problem 3 Answer: {0}".format(answer)
    
  def calcHighestPrimeFactor(self, currentPrimeFactor, numberToBeFactored):
    counter = 2 #2 is the lowest prime number
    nextNumberToBeFactored = numberToBeFactored
    
    while counter <= numberToBeFactored:
      if numberToBeFactored % counter == 0:
        nextNumberToBeFactored = numberToBeFactored / counter
        currentPrimeFactor = self.calcHighestPrimeFactor(counter, nextNumberToBeFactored)
        break
      counter += 1

    return currentPrimeFactor