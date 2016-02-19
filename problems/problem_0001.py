class Problem_0001:
  
  def run(self):
    total = 0
    for i in range(1, 1000):
      if i % 5 == 0 or i % 3 == 0:
        total += i
        #print "Found: {0}".format(i)

    print "Problem 1 Answer: {0}".format(total)