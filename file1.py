import os
inp = int(input("enter your choice : "))
if inp==1:
  os.system("notepad")
elif inp == 2:
  os.system("calc")
elif inp==3:
  os.system("google chrome")
elif inp==4:
  os.system("mspaint")
else:
  print("wrong choice")
