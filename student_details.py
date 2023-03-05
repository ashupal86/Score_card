import os
import datetime

#date stamp year import
date=datetime.datetime.now()

#basic student details for section identifying and creating report card within their class and year
name=str(input("Enter Name of student: ")).capitalize()
dob=str(input("Enter Date of birth of student: "))
clas=str(input("Enter Class of student: "))
section=str(input("Enter Section of Student: ")).upper()

#path of directory and change to report card directory
path=os.getcwd()
secc="{}_{}".format(clas,section)
os.chdir(path+"/classes")

#exception handling for folder creation if exist or not
try:
    os.mkdir(secc)
except FileExistsError:
    pass


#Changing the path to students section
os.chdir(path+"/classes/"+secc)
file_name="{} {}".format(name,date.strftime("%Y"))

#writing basic student details to the file if file is exist or not
if os.path.isfile(file_name):
    os.remove(file_name)
file=open(file_name,'w+')
file.write("Student Name: {} \nStudent D.O.B: {} \nClass: {} \nSection: {}".format(name,dob,clas,section))
file.write("\n====================================================\n")
file.write("\tSUBJECT NAME \t\tMARKS OBTAINED \t\tGRADE\n")
file.close()



