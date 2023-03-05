import os
import datetime 
date=datetime.datetime.now()




name=""
Class=""
dob=""
sec=""

while name=="":
    name=str(input("Enter student name: ")).upper()

while dob=="":
    dob=str(input("Enter dob: "))

while Class=="":
    Class=str(input("Enter Class: "))



while sec=="":
    sec=str(input("Enter Section: ")).upper()

path=os.getcwd()
new=(path+"/report card databasse")
os.chdir(new)

file_name="{} {}".format(name,date.strftime('%Y'))

try:
    os.mkdir("{} {}".format(Class,sec))
    os.chdir(new+"/{} {}".format(Class,sec))
except FileExistsError:
    os.chdir(new+"/{} {}".format(Class,sec))
    pass

try:
    
    if os.path.isfile("{}.txt".format(file_name)):
        raise FileExistsError
    else:
        file=open("{}.txt".format(file_name),'a+')
        file.writelines("Student Name: {}\nD.O.B: {}\nClass: {}\nSection: {}".format(name,dob,Class,sec))
        file.writelines("\n==============================================")
        os.system("echo File Created  {}.txt".format(file_name))
        file.close()
except FileExistsError:
    file=open("{}.txt".format(file_name),'r+')
    os.system("cat '{}.txt'".format(file_name))
    file.close()
    pass


