#download
#dropbox python sdk python package for dropbox (dropbox python sdk v2)
#download a file from dropbox via python (python3.10.6; python3.11.0; etc.)
#download a file
import c as C #compile from text to binary and vis-versa
import dropbox
from access_token import v_1
if "\n" in v_1[0]:
  #print(True)
  try:
    v_1[0] = v_1[0].replace("\n", "")
  except:
    print("replace method failed.")
else:
  #print(False)
  print("")
if "\n" in v_1[0]:
  print(True)
  try:
    v_1[0] = v_1[0].replace("\n", "")
  except:
    print("replace method failed.")
else:
  #print(False)
  print("")
try:
  dbx = dropbox.Dropbox(v_1[0])
  try:
    a = dbx.users_get_current_account()
    print(a)
    l = [dropbox, dbx]    
  except:
    print("Error 0002 - dropbox account token failed to open the dropbox.com account.")
except:
  print("Error 0001 - dbx variable cannot open dropbox.com account.")
def _f(fileName):

    global l
    (dropbox, dbx) = l

    if not fileName[0] == "/":
        f = str("/" + fileName)

    else:
        f = fileName
    
    metadata, r = dbx.files_download(f)
    #print("metadata, follows:")
    #print(r.content)
    b = r.content
    t = C.d(b)

    if "/" in f:
        f = f.split("/")
        f = f.pop()	

    file_new = open(f, "w")
    file_new.write(t)
    file_new.close()
    print("A file was downloaded. The file is called, " + fileName + ".")
    #print("f() Finished!")

    return t

#help
e = '''
    Instructions
    
        Note - Overwrite is True. Overwrite the existing file, if a file already exists by the name of the file which is being downloaded.

        import download as D
        fileName = "data.py"
        D.f(fileName)

        #How to download a list of files, option 1, as follows:
        myListOfFileNames = ["file1.txt", file2.py", "file3.csv"]
        for x in myListOfFileNames:
          D.f(x)
          
        #How to download a list of file, option 2, as follows:
        myList = ["file1.txt", file2.py", "file3.csv"]
        D.list_iterables(myList)
          
    #Done!
'''
print(e)
def f(x):
  #reference - ~/python_help_do_no_print_return.txt
  _f(x)
def list_iterables(fileList):#edited - changed from def l() to def list_iterables, on 11 17 2022.

  for fileName in fileList:
    f(fileName)
    
  print("f() Finished!")

  return None
def help():

  global e
  print(e)

  return None
    

