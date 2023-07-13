#VMN.py (VarModuleName.py)
def f_1(v_p = None):
  #new module var
  v_1 = __import__(v_p[0]) 
  #module_directory
  v_2 = dir(v_1) 
  #module_variables
  v_3 = f_2(v_2)
  #module_functions
  v_4 = f_3(v_2)
  v_5 = [v_3, v_4]
  return v_5
def f_2(v_p = None):
  v_1 = []
  v_i = [str(""), str("")]
  for v_i[0] in v_p:
    if "v_" in v_i[0]:
      v_1.insert(len(v_1), v_i[0])
  return v_1
def f_3(v_p = None):
  v_1 = []
  v_i = [str(""), str("")]
  for v_i[0] in v_p:
    if "def f_" in v_i[0]:
      v_1.insert(len(v_1), v_i[0])
  return v_1
v_1 = [
"""
     Important Note
This module is workable only if: 
(1) all of the var names in the module-which-is-being-analyzed are called, "v_" + some_integer (Examples: v_1, v_2, etc.); and
(2) all of the function names in the module-which-is-being-analyzed are called, "f_" + some integer (Examples: f_1(), f_2(), etc.)
""",
"""
     Instructions Part 1
#module file name - since it's an import moduleName syntax command, do not include the file ext, ".py"; instead, omit ".py" from the arg var.
v_1 = ["myModuleFileName"]
#new module var
v_2 = __import__(v_1[0])
#Examples - usage:
v_2.v_1
v_2.f_1() 
""",
"""
     Instructions Part 2
import VMN #VarModuleName, what to do when your module name is a value about a var
v_1 = ["myModuleFileName"]
v_2 = VMN.f_1(v_1)
#module var names
print(v_2[0])
#module def names
print(v_2[1])
#print everything returned by VMN.f_1(), as follows:
for x in v_2:
  print(x)
#or
[print(x) for x in v_2]
#also
#the qty of iterable lists inside of list var v_2, as follows:
print(len(v_2))
#the qty of var names (the first iterable list), as follows:
print(len(v_2[0]))
#the qty of def (function) names (the second iterable list), as follows:
print(len(v_2[1]))
"""
]
def help():
  global v_1
  print(v_1[0])
  input()
  print(v_1[1])
  input()
  print(v_1[2])
  return None
