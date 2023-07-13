#rhd.py
import re
def  f_1(v_p=None):
  #v_p: variable parameters
  #params: file_name; the file which the AI is supposed to read.
  if not bool(v_p):
    return "Error 0001. File, \"rhd.py\""
  with open(v_p[0], "r") as f:
    t = f.read()
    f.close()
    del f
  f_2(t)
  return None
def f_2(params=None):
  x = "All of this can be deleted. Definition - anything below this word, might be useful, keep the data below the word \"Definition\"<delete the text inbetween the special characters.>Don't delete this sentence, outside of the special characters.<Delete this, too.>"
  x_l = x.lower()
  s_1 = str("Definition").lower()
  y = re.split(s_1, x)[1]
  z_1 = re.split("<", y)
  text_2 = ""
  for item_1 in z_1:
    text_2 += re.split(">", item_1)[1]

  
