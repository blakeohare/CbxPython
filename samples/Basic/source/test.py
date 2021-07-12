import helper

class Foo:
  
  iAmClassField = 42
  
  def __init__(self):
    self.meow = 43
    print("This is __init__")
	
  def sayHello(self):
    print("I am foo")

class Bar(Foo):
  def __init__(self):
    Foo.__init__(self)
    self.meow += 1

def doubleMe(x):
  return x * 2

def main(x):
  print('DOUBLE: ' + str(doubleMe(14)))
  for i in range(10):
    print(str(i + 1) + " Mississippi")
  n = 1
  while n <= 4:
    print(str(n) + " Arkansas")
    n += 1
  helper.doHelp()
  helper.doHelp2()

  if x > 10:
    pass

  for temp in 'abcdefg':
    x = 42
    y = 60
    if y > 30:
      x = x + 1

  myDict = {
    "a": 42,
    "b": [1, 2, 3],
  }

  print(myDict['a'] + ' | ' + myDict['b'])
  
  foo = Foo()
  bar = Foo()
  print(foo.meow)
  print('1A ' + str(foo.iAmClassField))
  print('1B ' + str(bar.iAmClassField))
  foo.iAmClassField = 50
  print('2A ' + str(foo.iAmClassField))
  print('2B ' + str(bar.iAmClassField))
  Foo.iAmClassField = 60
  print('3A ' + str(foo.iAmClassField))
  print('3B ' + str(bar.iAmClassField))
  
  print('-' * 40)
  bar = Bar()
  print(bar.meow)
  print(bar.iAmClassField)

main(4)
