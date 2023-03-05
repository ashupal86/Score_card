

import os

choice=0

choice=int(input("Enter \n1: Add new \n2:Search or edit data \n:"))
if choice==1:
    import add_new
    
elif choice==2:
    import edit_exist
    

else:
    os.system("echo worng input")