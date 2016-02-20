import sys
from helloworld.helloworld import HelloWorld
from problems.problem_0001 import Problem_0001
from problems.problem_0002 import Problem_0002
from problems.problem_0003 import Problem_0003


def main():
  HelloWorld().sayHello()
  Problem_0001().run()
  Problem_0002().run()
  Problem_0003().run()

if __name__ == "__main__":
   sys.exit( main() )