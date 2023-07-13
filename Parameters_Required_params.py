#Parameters_Required_params.py
#How to make required inputs, to a function, when only one parameter var list is specified, about the function parameters, as follows:


"""
def f_1(v_p = ["value 1", "value 2", ["description", "value 1 of description"]]):

  #Step 1. 
  #Assign required variables, here, as follows:
  v_1 = "value 1"
  v_2 = "value 2"
  v_3 = ["description", "value 1 of description"]]

  #Step 2.
  #Next, Get the length

  #Step 3.
  #Then, Assign the required variables, according to the list built in step 1 (above)
  
  return None
"""
  
  
#Simplified  
#That can be re-written, and the solution is a combination of functions f_1 and f_2, as follows:

def f_1(v_p = None):
  
  #Assigned required variables, here, as follows:
  v_1 = "value 1"
  v_2 = "value 2"
  v_3 = ["description", "value 1 of description"]]
  
  #Get params len()
  #Reason - To find how many required variables must be assigned to the parameters variable, v_p, as follows:
  if len(v_p) < 2:
  
    if len(v_p) == 0:
      print("Error 0001; line 30; file, \"thisFileName.py\". At least one arg must be provided when calling this function.")
      return [False, "mgrc. Error 0001."]
    
    elif len(v_p) == 1:
      v_p.insert(len(v_p), v_2)
    
    elif len(v_p) == 2:
      v_p.insert(len(v_p), v_3)
  
  return None
  
#That can be simplified, as follows:
def f_2(v_p = None):

  #Get required params
  v_1 = f_1(v_p)

  return none  
  
  
  
  
  
  





#Bottom of this Document
