#file overwrite - This script, upload.py, overwrites a file.
#See descriptions about mgrc modules at https://helpwithcode.w3spaces.com.
import c as m_1
import dropbox
from access_token import v_1 as m_2
gl = list([])
if "\n" in m_2[0]:
  #print(True)
  try:
    m_2[0] = m_2[0].replace("\n", "")
  except:
    print("replace method failed.")
else:
  #print(False)
  print("")
if "\n" in m_2[0]:
  print(True)
  try:
    m_2[0] = m_2[0].replace("\n", "")
  except:
    print("replace method failed.")
else:
  #print(False)
  print("")
try:
  dbx = dropbox.Dropbox(m_2[0])
  try:
    a = dbx.users_get_current_account()
    print(a)
    gl = [dropbox, dbx]    
  except:
    print("Error 0002 - dropbox account token failed to open the dropbox.com account.")
except:
  print("Error 0001 - dbx variable cannot open dropbox.com account.")
def f_1(fileName):
  (dropbox, dbx) = gl
  if "/" in fileName:
    a = fileName.split("/")
    c = a.pop()
    f = open(c, "r")
  elif "/" not in fileName:
    f = open(fileName, "r")
  t = f.read()
  f.close()
  f = ""
  if fileName[0] == "/":
    f = str(fileName)
  elif fileName[0] != "/":
    f = str("/") + str(fileName)
  b = m_1.e(t)
  dbx.files_upload(b, f)
  print("A file was uploaded.")
  return 0
def f_2(fileName):
  #print("overwrite="+"Y")
  (dropbox, dbx) = gl
  if "/" in fileName:
    a = fileName.split("/")
    c = a.pop()
    f = open(c, "r")
  elif "/" not in fileName:
    f = open(fileName, "r")
  f = open(fileName, "r")
  t = f.read()
  f.close()
  f = ""
  f = str("/") + str(fileName)
  b = m_1.e(t)
  dbx.files_upload(b, f, mode=dropbox.files.WriteMode.overwrite)
  print("A file was uploaded.")
  return 0
def file(fileName, overwrite="n"):
  if overwrite == "N" or overwrite == "n":
    f_1(fileName)
  elif overwrite == "Y" or overwrite == "y":
    f_2(fileName)
def list(aListOfFileNames, overwrite="n"):
  l = aListOfFileNames
  for i in l:
    if overwrite == "N" or overwrite == "n":
      f_1(i)
    elif overwrite == "Y" or overwrite == "y":
      f_2(i)
  print("list()  Done.")
def help():
  example_1 = '''#upload to dropbox.com, but fail to upload if file already exists
f = "myFile.txt"
upload.file(f)
...'''
  print("...")
  input()
  print(example_1)
  input()
  example_2 = '''#upload to dropbox.com; overwrite existing file
f = "myFile.txt"
upload.file(f, "Y")  #i.e., overwrite="Y"
...'''
  print(example_2)
  input()
  example_3 = '''#upload a list of files
f1 = "firstFile.txt"
f2 = "secondFile.py"
fileList = [f1, f2]
upload.list(fileList, overwrite="Y")'''
  print(example_3)
help()

