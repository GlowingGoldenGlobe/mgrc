#s.py
#server upgrade file
#get or save server data file (data_1.js) text
#;//#0-1-x-b-5-7-2-r-!-$-&# - This key variable character-set-sequence is arbitrary, but it must remain consistant, unaltered versus its copy of itself in the data_1.js file.
import json
t1 = '''function data_1_file() {
  var d = '''
t2 = ';//#0-1-x-b-5-7-2-r-!-$-&#'
t3 = '''
  return d;
}'''
l = list()
#File Name, HERE:
fileName = "data_1.js"
#data_1.js about info
f = open(fileName, "r")
t = f.read()
f.close()
del f
h_1 = t.split("function data_1_file() {")
header = h_1[0]
l = [t1, t2, t3, header]
def save(params1, params2=fileName, params3=l):
  (t1, t2, t3, header) = params3
  fileName = params2
  x = str(params1)
  if "\\" in x:
    a = x.split("\\")
    del x
    x = "#r_c!1#".join(a)
  j = json.dumps(x)
  #j2 = json.dumps(j)
  #o = header + t1 + j2 + t2 + t3
  o = header + t1 + j + t2 + t3
  if "\\" in o:
    a = o.split("\\")
    del o
    o = "#r_c!2#".join(a)
  f = open(fileName, "w")
  f.write(o)
  f.close()
  l = len(o)
  print("Finished.")
  return l
def get(params=fileName):
  f = open(fileName, "r")
  t = f.read()
  f.close()
  #modify text
  #print(t)
  if "#r_c!2#" in t:
    a = t.split("#r_c!2#")
    del t
    t = "\\".join(a)
  m = list([])
  if "var d = '\"" in t:
    m = t.split("var d = '\"")
    #print("True 1")
  elif "var d = \"" in t:
    m = t.split("var d = \"")
  elif "var d = \'" in t:
    m = t.split("var d = \'")
  else:
    try:
      m = t.split("var d = ")
    except:
      print("s.get() failed!. Error 0001.")
  m2 = m[1]
  #print(m2)
  #print("m2 is True")
  if "\"';//#0-1-x-b-5-7-2-r-!-$-&#" in m2:
    m3 = m2.split("\"';//#0-1-x-b-5-7-2-r-!-$-&#")
  elif "\";//#0-1-x-b-5-7-2-r-!-$-&#" in m2:
    m3 = m2.split("\";//#0-1-x-b-5-7-2-r-!-$-&#")
  try:
    m3 = m2.split("';//#0-1-x-b-5-7-2-r-!-$-&#")
  except:
    #print(False)
    ''''''
  try:
    m3 = m2.split(";//#0-1-x-b-5-7-2-r-!-$-&#")
  except:
    print(False)
    pass
  string_data = m3[0]
  #print("m3 is True")
  #input()
  #print(string_data)
  d = list([])
  try:
    d = json.loads(string_data)
    d_string = str(d)
    if "#r_c!1#" in d_string:
      a = d_string.split("#r_c!1#")
      del d
      d = "\\".join(a)
    #print("json.loads successful")
    #input()
    #print(t)
  except:
    print("exception occurred - json.loads must have failed.")
    #print(type(t))
    #input()
    #print(t)
    #d_str = t.split()[0]
    #d = json.loads(d_str)
    pass
  iterate(d)
  return d
def append(params):
  d = get()
  d.append(params)
  save(d)
def help(x="0"):
  example_1 = '''
#Example

#import
#import server py file, s.py, as follows:
import s'''
  example_1_2 = '''
#get
#s.get() ;  get data from data_1.js, as follows:
d = s.get()
#The data json string is auto loaded by s.get(), 
#and your result data is variable d; 
#preference - I save and get my data as a variable type list([]).
#How to display your data, to view your data; where variable l = list([]), - the command is as follows:
s.iterate(l)'''
  example_1_3 = '''
#modify
#modify data_text, it becomes myData variable, as follows:
myData = "Data here..."

#s.save(arg)
#save myData, overwrite old data, in file, data_1.js, as follows:
#note - myData will be auto dumped to json string variable type, then saved, by function s.save(myData)
s.save(myData)
...'''
  example_2 = '''#note - you might save header information as iterable list item l[0]
#print all items in the data list, as follows:
[print(x) for x in l] #or, display them, as follows:
s.iterate(l)#then, once displayed iterables, print per iterable number, as follows:
print(l[2])#etc.'''
  if x=="display" or x=="iterate" or x=="list" or x=="get" or x=="get data":
    print(example_1_2) 
  elif x=="save":
    print(example_1_3)
  elif "modify" in x or "edit" in x:
    print(example_1_3)
  elif "header" in x or "title" in x:
    print(example_2)
  else:
    print(example_1)
    input()
    print(example_1_2)
    input()
    print(example_1_3)
    input()  
    print(example_2)
  pass
  pass
help()
def iterate(params1, params2=fileName):
  if bool(isinstance(params1, list)):
    l = params1.copy()
  elif not bool(isinstance(params1, list)):
    print("Error 0002b0002b - s.py file, def iterate():  The function parameter, params1, is supposed to be a var type list(), but is not a list.")
  print("file name:  " + fileName)
  print("list length:  " + str(len(l)))
  print('''______________________________''')
  print("iterable number | list item")
  i = 0
  while i < len(l):
    try:
      item = json.loads(l[i])
    except:
      item = l[i]
    if not bool(isinstance(item, str)):
      item = json.dumps(item)
    print(str(i) + " " + item)
    print("")
    i = (i + 1)
    del item
  print('''______________________________''')
  print('''Example
item = d[3]
s.iterate(item)''')
    
    
    
    
    
    
    
    
    
    
#Bottom of this Document
