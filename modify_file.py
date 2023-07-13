#step 2
#modify_file.py
#write to file, where the file is already created
#reference - procedures list, file, "in progress_to do_06 14 2023.txt"
import re
#for re.split(pattern_to_find, string_to_split); returns a list variable object, list_1 = list(["a", 2, list([]), ...])
#also, for re.sub(pattern_to_find, value_with_which_to_replace_pattern, string_to_search)
def f1(params=None, params2=None):
  #params = file_name ; the name of the file to which data will likely be saved
  #params2 = data_text ; the text to saved to the file; the text in observation; not the file text, unless the file text, as same
  #part 1 - test if adequate params are given to this function
  if bool(params):
    l = len(params)
    if l > 1:
      (file_name, data_text) = params
    elif bool(params2):
      file_name = params
      data_text = params2
    elif not bool(params2) and not l > 1:
      print("Two variable arguments are required for this function: (1) file_name; (2) data_text. Use either: a list, or two separate variables, to pass the arguments to this function.")
      return None
  else:
    return None
  #part 2 - identify category about params variable
  f = open("data_1.py", "r")
  #code... i left of here 06 14 2023
  #part 3 - test file size; test if: (1) adequate space is available; (2) no more space is available on this file for storage    
  del l
  #file
  f = open(file_name, "r")
  t = f.read()
  print(type(t))
  f.close()
  del f
  #l = len(data_text)
  l = len(t)
  f_limit = True #file_size_limit_storage_available = bool(True)
  q = 5000 #file_limit_qty = 5000; characters qty length
  if l > q:
    f_limit = False
    #must create new file
    from file_names import data as FD
    a = FD.enumeration
    a_str = str(a)
    file_name = "data_" + a_str + ".py"
    f = open("file_names.py", "r")
    t_2 = f.read()
    t_split = re.split("enumeration = [", t_2)
    t_part_1 = t_split[0]
    t_split_3 = t_split[1]
    t_split_4 = re.split("]", t_split_3)
    t_enumeration = t_split_4[0]
    t_part_2 = t_split_4[1]
    t_part_middle = "enumeration = [" + t_enumeration + ", " + a_str + "]"
    t_new = t_part_1 + t_part_middle + t_part_2
  f = open(file_name, "w")
  result = ""
  f.write(result)
  return None
def f_compile_1(params=None):
  if bool(params):
    l = len(params)
  #those symbols likely to cause a problem with html syntax, json, or whatever
  #compile them to workable, store-able, code syntax aliases
  for x in list_1:
    arg = x
    f_test_1(arg)
  if not
def f_test_1(param):
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  a_upper = alphabet.copy()
  a_upper.upper()
  list_1 = list([])
  list_1 = alphabet + a_upper + numbers
  if param in list_1:
    return True
  else:
    return False
  
  
  
  
  
  
  
  
