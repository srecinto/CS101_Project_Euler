import sys
from helloworld.helloworld import HelloWorld
from problems.problem_0001 import Problem_0001


def main():
  HelloWorld().sayHello()
  Problem_0001().run()

if __name__ == "__main__":
   sys.exit( main() )