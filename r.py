#r for relationship
#reference - see the, "R2" section on the following page:  https://www.w3schools.com/python/python_ml_train_test.asp
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

#example data variables, x, and y, are as follows (global variables, x, y as variable-names g_x and g_y):
g_x = numpy.random.normal(3, 1, 100)
g_y = numpy.random.normal(150, 40, 100) / x

def f_1(params=false):
  #params variable
  #params variable should be a list, such as, list_1 = [x, y]
  #see def help():, for instructions.
  #where x is data
  #where y is data
  #example of x and y is on the following page:  https://www.w3schools.com/python/python_ml_train_test.asp;  see the "R2" section of said page.
  if not bool(params):
    print("Error 0001; file name, \"r.py\"; function, def f_1(params=false):.")
    pass
  (x, y) = params
  train_x = x[:80]
  train_y = y[:80]
  test_x = x[80:]
  test_y = y[80:]
  mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
  r = r2_score(train_y, mymodel(train_x))
  print(r) 
  f_del()
  print("Finished!")
  return 0
def f_del():
  global g_x
  g_x = ""
  del g_x
  global g_y
  g_y = ""
  del g_y
  return 0
def help():
  example_1 = '''
import r
x = [user data as list variabe items, goes here]
y = [user data as list variabe items, goes here]
list_1 = list([])
list_1.append(x)
list_1.append(y)
r.f_1(list_1)
'''
  print(example_1)
