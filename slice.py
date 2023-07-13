#split at re.split() span() indexes (indices)
#The way to do that is to "slice" the str("") var.

#     Instructions

import re
"""Example of f_1() script, outside of a function var.
v_1 = ["This is some some text."]
v_2 = re.finditer("some ", v_1[0])
v_i = [int(0)]
v_i_2 = [""]
v_3 = []
for v_i_2[0] in v_2:
  v_3.insert(v_i[0], v_i_2[0].span())
  v_i[0] += 1
#v_3 is var type tuple; consequently, change tuple to list, as follows:
v_4 = []
v_i = [int(0)]
for v_i[0] in range(0, len(v_3)):
  v_4.insert(v_i[0], list(v_3[v_i[0]]))
  v_i[0] += 1
v_5 = [v_1[0][0:(v_4[0][0]-1)], v_1[0][(v_4[0][1]):len(v_1[0])]]
v_6 = [(v_5[0] + v_5[1])]
"""
def f_1(v_p=None):
  if not bool(v_p) or type(v_p) is not list:
    print("Error 0001 - This file is called, \"slice.py\"; f_1(). The args sent to this function must be a list([]) with a string at iterable=0, e.g., list([str(\"This is some text.\")]).")
    return None
  #Where args are as follows: (1) v_p[0] is the search criterion at which to find the span() values, and (2) v_p[1] is arg=str_text_data
  v_1 = re.finditer(v_p[0], v_p[1])
  v_i = [int(0), str("")]
  v_2 = []
  for v_i[1] in v_1:
    v_2.insert(v_i[0], v_i[1].span()) #.span() returns a tuple, inside of which are iterables. This line runs code which builds a list([]) var, with a tuple var inside. For example - v_2 = list([.span()]), as v_2 = [(1, 5)] (these values (1, 5) are only for example purposes and are not the actual values which will be returned by .span()). Also, if multiple .span() sets are found, it will look something like this, as follows: v_2 = [(1, 5), (13, 17), etc.]
    v_i[0] = (v_i[0] + 1)
  #v_2 is var type tuple; consequently, change tuple to list, as follows:
  v_3 = []
  v_i[0] = int(0)
  for v_i[0] in range(0, len(v_2)):
    v_3.insert(v_i[0], list(v_2[v_i[0]]))
    v_i[0] += 1
  #v_2 became v_3, but as - a list([]) containing list([]) var iterables, instead of a list([]) containing tuple var iterables.
  #Example - v_3 = [[1, 5], [13, 17], etc.], instead of v_2 = [(1, 5), (13, 17), etc.]
  #Now, v_4, below, is where the code builds two slices of the parameters string variable: (1) the section before the search criterion; (2) the section after the search criterion. Example v_4 = [section_before, section_after], see actual code details, below. This code omits the search criterion between two sections of the parameters string-text-data var; this affords the code the ability to replace or delete the search criterion from the string, where the search criterion is specified as the place to slice from the string, the place between two pos (positions, captured as return values from .span()). Example, if the two sections are combined into a string, without adding any criterion inbetween during the combination, then, it follows that the search criterion will have been deleted, since it is not in either of the two slices of the str var. Alternatively, some criterion may be added inbetween the sections, resulting in a modified str var.
  v_4 = [v_p[1][0:(v_3[0][0])], v_p[1][(v_3[0][1]):len(v_p[1])]] 
  v_5 = [(v_4[0] + v_4[1])]
  return [v_3, v_4, v_5]
v_1 = """Instructions, Part 1
  import slice
  v_1 = slice.f_1([mySearchCriterion, myDataStr])
  print(v_1[0]) #This is the set(s) of pos, where the search criterion was found in the data str var parameter.
  print(v_1[1]) #This is a list, containing the before and after sections about the sliced part of the, said, data str var sent to the function.
  print(v_1[2]) #This is a new data str var, the combination of the before and after sections, where the search criterion is omitted.
  
  Instructions, Part 2
  #Step 1. get all of the positions of some search criterion in a particular str var.
  v_1 = slice.f_1([mySearchCriterion, myDataStr])
  #Step 2. Specify what to replace it with, specify the position of the searchCriterion which you want to replace, as follows:
  v_2 = slice.f_2([repl, [pos1, pos2], str])
  print(v_2[0]) #[section_before, section_after]
  print(v_2[1]) #new str, as follows: (section_before + repl + section_after)
"""
def help(v_p=None):
  global v_1
  print(v_1)
  return None
def f_2(v_p=None):
  #parameters = [repl, [pos1, pos2], str]
  v_1 = [v_p[2][0:v_p[1][0]], v_p[2][v_p[1][1]:len(v_p[2])]]
  v_2 = v_1[0] + v_p[0] + v_1[1]
  return [v_1, v_2]

  
  
  
  
  
  
  






#Bottom of this Document
