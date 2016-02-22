#
# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
# 
class Problem_0004:
  
  def run(self):
    
    #Test isPalindrome method
    #print "101: {0}".format(self.isPalindrome(101))
    #print "1001: {0}".format(self.isPalindrome(1001))
    #print "1: {0}".format(self.isPalindrome(1))
    #print "1003: {0}".format(self.isPalindrome(1003))
    #print "103: {0}".format(self.isPalindrome(103))
    #print "982081: {0}".format(self.isPalindrome(982081))
    
    #Brute forcing it...  Can't figure out the equation to calc this
    leftNumber = 999
    rightNumber = 999
    numberThreshold = 900 #just try 10 for now
    rightNumberThreshold = 900 
    isPalindrome = False
    answer = 0
    while leftNumber > numberThreshold:
      rightNumber = 999
      while rightNumber > numberThreshold:
        answer = leftNumber * rightNumber
        isPalindrome = self.isPalindrome(answer)
        if isPalindrome :
          break
        rightNumber -= 1
        
      if isPalindrome :
        break
      leftNumber -= 1
      
    print "Problem 4 Answer: {0}x{1}={2} product is a Palindrome: {3}".format(leftNumber, rightNumber, answer, isPalindrome)
    
  #
  # Checks if number is a palendrome
  #
  def isPalindrome(self, numberToCheck):
    result = True
    numberToCheckString = str(numberToCheck)
    fullStringLength = len(numberToCheckString)
    halfStringLength = fullStringLength / 2
    currentCharIndex = 0
    
    while currentCharIndex < halfStringLength:
      oppositeCharIndex = (fullStringLength - currentCharIndex - 1)
      
      if numberToCheckString[currentCharIndex] != numberToCheckString[oppositeCharIndex]:
        result = False
        break
      
      currentCharIndex += 1
      
    return result