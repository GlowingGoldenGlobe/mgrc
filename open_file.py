#open_file.py
def f_1():
  f = open("data_1.py", "r")
  t = f.read()
  print(type(t))
  f.close()
  del f
  return t
def f_2():
  f = open("data_2.py", "r")
  t = f.read()
  print(type(t))
  f.close()
  del f
  return t
