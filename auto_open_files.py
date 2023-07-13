import subprocess as S
#gedit is Ubuntu's text editor; "gedit" is a command in the terminal which opens Ubuntu's text editor
#gedit FILENAME.txt
list_1 = list(["about.py", "modules.py", "build_file.py", "modify_file.py", "open_file.py", "brain_1.py", "brain_2.py","file_names.py", "data_1.py", "data_2.py", "wip_brain_exclamation.py"])
def f_1():
  global list_1
  for item_1 in list_1:
    S.Popen(["gedit", item_1])
  return None
f_1()
