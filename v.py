#verify dropbox account user name
def d(dbx):
  a = dbx.users_get_current_account()
  print(a)
  pass
  return "0"
e='''import v
v.d(dbx)'''
print(e)