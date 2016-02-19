#
# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
class Problem_0001:
  
  def run(self):
    total = 0
    for i in range(1, 1000):
      if i % 5 == 0 or i % 3 == 0:
        total += i
        #print "Found: {0}".format(i)

    print "Problem 1 Answer: {0}".format(total)