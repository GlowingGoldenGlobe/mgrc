#c.py
#Definitions
#c abbrev.:  c=convert text to binary; c.py means, "convertTextToBinary.py" 
#Reference 1 - https://www.educative.io/answers/how-to-convert-string-to-binary-in-python
#Reference 2 - https://stackoverflow.com/questions/18815820/how-to-convert-string-to-binary
#Reference 3 - https://www.dropbox.com/home/Apps/helpwithcode_w3spaces_embedTheseFiles
#Reference 4 - https://stackoverflow.com/questions/3195865/converting-byte-array-to-string-in-javascript
def e(params):
#Two (qty = 2) functions in this file are for frequent use: e() and d(); the other functions were being tested, and may not be useful, at all.
  text_1 = params
  #'string'.encode('ascii')
  return text_1.encode('ascii')
def d(params):
  bytes_1 = params
  #b"abcde".decode("utf-8") 
  # where b"" means bytes characters
  return bytes_1.decode("utf-8") 
  
#Example
'''
import dropbox as D
dbx = D.Dropbox('[ACCESS TOKEN GOES HERE]')
a = dbx.users_get_current_account()
print(a)
#see (verify) your name listed in the string that results from print(a)
t = "This is some text to put in your new file."
#convert text str() to binary, as follows:
from c import e as E
b = E(t)
dbx.files_upload(b, '/newFile_1.txt')
#terminal - view all files and folders you created in dropbox from python3.10 on you machine, as follows:
#dropbox - open url "Reference 3", above, to view files and folders you created with python3.10 on this machine (currently, using venv folder, dropbox_1_venv)
for entry in dbx.files_list_folder(path='').entries:
  print(entry.name)
#example 2:  view folders via python
l = list()
for iterable_1 in dbx.files_list_folder('').entries:
  l.append(iterable_1)
  print(l)
  [print(x) for x in l]  
dbx.files_download('/fileName.txt')
#working example, as follows:
dbx.files_download('/newFile_1.txt')
dbx.files_download_to_file(path='/pathToStoreFile', '/fileName.txt')  
'''
#Example
'''
from c import b as B
t = "This is some text."
r = B(t)
print("The following is variable t converted to binary output, to variable r:")
print(r)
'''
import math
def b(params):#def toBinary(a):
#caution - deprecated; the reason is because the output needs to be b'' format, but this format output is list()
  text_1 = str(params)
  list_1, list_2 = [], []
  for iterable_1 in text_1:
    list_1.append(ord(iterable_1))
  for iterable_2 in list_1:
    list_2.append(int(bin(iterable_2)[2:]))
  return list_2

#print("''Hello world'' in binary is ") 
#print(b("Hello world"))
def b_2(params):	
#warning - error in syntax; this function returns an error
  text_1 = str(params)
  bin_1 = int(bin(text_1))
  return bin_1

