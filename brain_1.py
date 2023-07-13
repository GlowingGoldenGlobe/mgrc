#brain_1
#get data
#eyes observe data
#holds that data here, via this file, variables and functions

#test data meanings
#compare to objectives
#synthesize (compute analysis; search for) relevant data
#discover next task, or wait

var_1 = list([])#contents
var_2 = list([])#search terms
var_3 = list([])#recent objectives
import open_file
import re
def f_1():
  f_2()
  f_3()
  return None
def f_2():
  #Step 1 - data_1.py on the infinite clock of my conscious (since my conscious is the conscious, God); recorded, as a scheduled event
  #Step 2 - get contents; options
  contents = open_file.f_2()
  global var_1
  var_1 = contents
  return None
def f_3():
  #code...
  #test data meanins
  #Step 3 - from var_1 (contents) - get data, to synthesize
  global var_1
  list_1 = re.split(", ", var_1)#var_1 = contents
  length_1 = len(list_1)  
  if length_1 <= 3:
    data_inception = open_file.f_1()
  else:
    f_4()
  return None
def f_4():
  #read and synthesize contents data; find a relevant data file(s)
  import data_2
  list_1 = data_2.file_descriptions
  search_term = ""
  list_2 = f_5()
  length_list_2 = len(list_2)
  i = 0
  test_1 = False
  while i in range(length_list_2):
    for iterable_1 in list_1:
      search_term = list_2[i]
      #print(search_term)
      if search_term.upper() in iterable_1[1].upper():
        print(True)
        print(iterable_1)
        test_1 = True
        #code...
      else:
        print(False)
        #code...
    i = (i + 1)
  if not bool(test_1):
    print("No matches were found.")
  return None
def f_5():
  #Find search terms to search for, for function f_4(), above.
  #store search terms in global var_2
  global var_2
  search_term = ""
  #code...
  var_2.append(search_term)
  if not bool(var_2):
    return var_2
  elif bool(var_2):
    f_6()
    return var_3
def f_6():
  #Recent objectives - store as var_3 list([])
  global var_3
  recent_synthesis = ""
  #code...
  recent_synthesis = "API Brain"
  var_3.append(recent_synthesis)#recent_objectives_description
  return None
  
  
  





