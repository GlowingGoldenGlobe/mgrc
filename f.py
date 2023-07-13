#f.py
#f alias for "findOrBuildFile"
#copy at "~/Home/Help_Python/findOrBuildFile.py
#find or build new file
#create directory (folder)
#reference - https://www.tutorialspoint.com/python/os_mkdir.htm



"""About

    findOrBuildFile: find or build file

    Explanation
        (1) find - Find that text length is small enough to fit in an existing file, from which the text came or to which the text, otherwise, belongs
        (2) build - If the text length is too great (too large in quantity value), then build a new file(s), and split the text between multiple files

End "About"
"""



#To Do
#Procedure
"""

    1. (Part 1) Find text-qty, about the file to be edited. Example - len(text_data_str_of_file)
    2.1. (Part 2) If the text-qty is greater than 50,000, then the file may become too large; consequently, some text must be saved to another file, also (save the text to multiple files)
    2.2. To save to another file, also (i.e., also means - in addition to saving the text to the specified file, where the var arg sent to this module, to function f_1(params), received as var params (or var v_p, in this case), specifies the file to save to) - a new file must be created; consequently, since file names are in the format, <fileName_idHere.py>, find the id-value of the name of the current file (the, "idHere", part of the file name); then, add 1 to it (thus, building the new file name, with the format, <fileName_newIdHere.py>).
    
    
    
    Example 1
    
        import f as m_1
        with open("myFile.py", "r") as v_f:
          v_t = v_f.read()
          v_f.close() #*See Note 1, below.
          del v_f
        #<modify/edit v_t here>
        #then:
        m_1.f_1(v_t) #(1) build new file(s), if needed; (2) print v_t to file(s)
    
    
    
    Definitions
    <> : denotes aliases as references, between the character, less than, "<" and the character, greater than, ">". Example - <fileName.py>, means that a file name belongs at that position, fileName, but it doesn't mean that the file name is "fileName" + the extension ".py". Example 2 - <fN_id.py> could be filled in with something like, "urlData_112.py", or whatever file name would be suitable for the application one is working on.
    qty abbr English-United-States: quantity
    m_f abbr python3.10-code-syntax: module_1
    v_f abbr python3.10-code-syntax: variable_file_document_object
    v_t abbr python3.10-code-syntax: variable_text_from_file
    module python3.10-code-syntax: Is a file with ".py" extension, in its file name. A file with a ".py" extension, in its name, is used to run python syntax code in the command-line-interface.
    method python3.10-code-syntax: A method is a function.
    del abbr python3.10-code-syntax: delete variable name and value from the command-line-interface instance
    
    
    
    Notes
    *Note 1 - Text from file becomes available, only after the file is closed, using the .close() method.

"""


import os, sys
import re



def f_1(v_p = [None, "Build a new file.", ["dropbox", bool(False)]]):

   #About the function parameters
   #v_p[0] = my text
   #v_p[1] = indicate file name, else leave as, "Build a new file."
   #v_p[2] = indicate if saving to dropbox versus saving to my lapatop (my limited storage maximum requirements about my laptop, if saving to my laptop, leave the param as bool(False). If save to dropbox, then, indicate, bool(True).

  if not bool(v_p) or type(v_p) is not list:
    print("Error 0001; arg = [] is required; \"~/Home/Documents/Help_Python/findOrBuildFile.py\"; f_1();s line 9.")
    return None
    
  #Procedure: Part 1
  #Text length
  v_1 = len(v_p[0])
  
  #Procedure: Part 2
  #max text length per file; this qty is different if ["dropbox", True], about v_p[2][1] = <bool(True) or bool(False)>
  #(1) for laptop, use lesser value, v_2[0]; 
  #(2) for dropbox files, use greater value, v_2[1]
  v_2 = [int(50000), int(300000)] #verify dropbox file text qty maximum, regarding automatically-saving-data to dropbox about upload, before saving to dropbox
  #v_3 is the qty of splits to make, where each split is a part of the text to save, where each split part is a length small enough to fit into a file, or to be uploaded to dropbox, per the max-text-quantities requirements per each storage place (storage places: 1. laptop; 2. dropbox).
  v_3 = []
  #v_4 is a list([]) containing the text, where the text is split into usable lengths, a usable length per iterable in the list([]) var v_4, about the text which is to be saved to a file or files
  v_4 = []
  if not bool(v_p[2][1]): #then, v_2[0]
    if v_1 > 50000:
      v_3.insert(0, (v_1 / v_2[0]))
    else:
      v_3.insert(0, v_1)
  elif bool(v_p[2][1]): #then, v_2[1]
    if v_1 > 300000:
      v_3.insert(0, (v_1 / v_2[1]))
    else:
      v_3.insert(0, v_1)
  v_i = [int(0), int(0), int(0), str("")]
  if len(v_3) > 1:
    for v_i[0] in range(0, len(v_3[0])):
      v_i[1] = v_i[0]
      v_i[0] += 1
      v_i[2] = 1
      if v_i[0] > len(v_3[0]):
        v_i[2] = 0
      if not bool(v_p[2][1]): #then, v_2[0]
        v_i[3] = v_1[(v_2[0] * v_i[1]) : (((v_2[0] * v_i[1]) * 2) - v_i[2])]
      elif bool(v_p[2][1]): #then, v_2[1]
        v_i[3] = v_1[(v_2[1] * v_i[1]) : (((v_2[1] * v_i[1]) * 2) - v_i[2])]
      v_4.insert(0, v_i[3])
  elif len(v_3) == 1:
    v_4.insert(0, v_p[0])
    
  #Next, the text must be split at var endings, or function endings; in other words, the text cannot be split at positions inbetween var start positions versus var end positions, nor at position inbetween function start positions versus functions end positions.
  
  #Get the file name, about the file to which to write the text
  #Originating file, if any
  #This program (rather, this if conditional) makes that determination - If "Build a new file." is True, then there isn't an originating file; so, a new file must be built.
  if "Build a new file." in v_p[1]: 
    #1 of 2. No originiating file
    #Below, f_2() returns the following list: v_p[1] = [fileLocation/fileName.py, maxValueAboutIdsInFileNames]
    #Therefore, as follows:
        #v_p[1][0] = fileLocation/fileName.py
        #v_p[1][1] = maxValueAboutIdsInFileNames
    v_p[1] = f_2()
    print(v_p[1])
    
  #2 of 2. If there is an originating file, then:
  else:
    if "/" not in v_p[1]:
      #v_p[1] = [fileLocation/fileName.py, maxValueAboutIdsInFileNames]
      v_p[1] = ["AI_Data/" + v_p[1], f_2()[1]]
  
  with open(v_p[1][0], "w") as v_5:
  
    #Write to file IF LEN() == 1
    if len(v_4) == 1:
      v_5.write(v_4[0])
      v_5.close()
      del v_5
    
    #Write to file IF LEN() > 1
    #code... 07 08 2023
    elif len(v_4) > 1:
      v_i = [int(0), int(0), "AI_Data/data_", ".py"]
      for v_i[0] in range(0, len(v_4)):
        v_i[1] = v_i[0]
        v_i[0] += 1
                  
        if v_i[1] >= 1:
          v_p[1][0] = v_i[2] + str(v_p[1][1]) + v_i[3] #where, v_p[1][1] = maxValueAboutIdsInFileNames; refer to lines: 129; 130; 137; (line numbers are approx. because they may have been altered by the developer-writing-additional-code.
          v_5 = open(v_p[1][0], "w")
          
        v_5.write(v_4[v_i[1]])
        v_5.close()

  return None
  
  

#Build a new file name, about the latest id, about the aggregate of fileName_id file names; return the new file name
def f_2(v_p = None):

  #Get file names, in the ~/Home/dropbox_3_venv/AI_Data diriectory
  v_1 = [os.listdir("AI_Data"), int(0)]
  
  #Get all of the id values from the file_id.py file names. The id's are appended to v_2, as follows.
  v_2 = []
  for v_i in v_1[0]:
    if "_" not in v_i:
      continue
    v_1[1] = re.split("\.", re.split("\_", v_i).pop())[0] #The backslash character forces the re program to treat the character which follows it as a character, rather than permitting re to treat the character as a code usage instance of a character, where, for example, if there isn't a backslash, e.g., ".", this means a character variable, instead of the punctuation mark "." (a period character punctuation mark); where, "\." means ".", as the punctuation mark, and the backslash is used to create the normal meaning of the character, rather than the code usage variable meaning of the character. Example 2 - "\_" splits only at the underscore character, and DOES-NOT split at any <backslash charcater + underscore character>.
    v_2.insert(len(v_2), v_1[1])
    
  #code...
  v_3 = [str("AI_Data/") + str("data_") + str(max(v_2)) + str(".py"), max(v_2)]
  del v_2

  return v_3
  


"""Example 1
import os, sys
v_1 = ["AI_Data"]
os.mkdir(v_1[0]);
v_2 = ["This is some text."]
with open(v_1[0] + "/" + "data_1.py", "x") as v_3:
  v_3.write(v_2[0])
  v_3.close()
  del v_3
End "Example 1" """



"""Example 2

>>> import os, sys
>>> v_1 = ["/Home/dropbox_3_venv/AI_Data"]
>>> os.mkdir(v_1[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/Home/dropbox_3_venv/AI_Data'
>>> os.mkdir("/AI_Data")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
PermissionError: [Errno 13] Permission denied: '/AI_Data'
>>> 
KeyboardInterrupt
>>> os.mkdir("/AI_Data");
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
PermissionError: [Errno 13] Permission denied: '/AI_Data'
>>> os.mkdir("AI_Data");
>>> output=open("AI_Data/"+"data_1.py", "x")
>>> output.write("#data_1.py")
10
>>> output.close()
>>> del output
>>>

End "Example 2" """
