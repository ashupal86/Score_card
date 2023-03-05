import os
import student_details
import edit_data
import datetime

date=datetime.datetime.now()


#import student details for report card identification
try:
    name=student_details.name
    clas=student_details.clas
    dob=student_details.dob
    section=student_details.section
    print(name,clas,dob,section)
    name=edit_data.name
    clas=edit_data.clas
    
    section=edit_data.section

except Exception:
    pass



    

#chaning dir to report card exist
path=os.getcwd()
new_path=path+"/score card/classes/"+"{}_{}".format(clas,section)
try:
    os.chdir(new_path)
except FileNotFoundError:
    pass
#student file name
file_name="{} {}".format(name,date.strftime("%Y"))




t_marks=int(input("Enter total marks: "))
sci=int(input("Enter SCIENCE marks: "))
math=int(input("Enter MATHS marks: "))
eng=int(input("Enter ENGLISH marks: "))
hindi=int(input("Enter HINDI marks: "))
sst=int(input("Enter S.S.T marks: "))
comp=int(input("Enter COMPUTER marks: "))

sum1=sci+math+eng+hindi+sst+comp
per=(sum1/t_marks)*100
grade=""
g1=""
g2=""
g3=""
g4=""
g5=""
g6=""


#Science Grade
if (sci<=100 and sci >=90):
    g1="A"
elif sci<90 and sci>=70:
    g1="B"
elif sci<70 and sci >=50:
    g1="C"
elif sci<50 and sci>=40:
    g1="D"
elif sci <40:
    g1="Fail"


#Math Grade
if (math<=100 and math >=90):
    g2="A"
elif math<90 and math>=70:
    g2="B"
elif math<70 and math >=50:
    g2="C"
elif math<50 and math>=40:
    g2="D"
elif math <40:
    g2="Fail"

#English Grade
if (eng<=100 and eng >=90):
    g3="A"
elif eng<90 and eng>=70:
    g3="B"
elif eng<70 and eng >=50:
    g3="C"
elif eng<50 and eng>=40:
    g3="D"
elif eng <40:
    g3="Fail"

#HINDI Grade
if (hindi<=100 and hindi >=90):
    g4="A"
elif hindi<90 and hindi>=70:
    g4="B"
elif hindi<70 and hindi >=50:
    g4="C"
elif hindi<50 and hindi>=40:
    g4="D"
elif hindi <40:
    g4="Fail"

#SST Grade
if (sst<100 and sst >=90):
    g5="A"
elif sst<90 and sst>=70:
    g5="B"
elif sst<70 and sst >=50:
    g5="C"
elif sst<50 and sst>=40:
    g5="D"
elif sst <40:
    g5="Fail"

#COMPUTER Grade
if (comp<100 and comp >=90):
    g6="A"
elif comp<90 and comp>=70:
    g6="B"
elif comp<70 and comp >=50:
    g6="C"
elif comp<50 and comp>=40:
    g6="D"
elif comp <40:
    g6="Fail"

#All over Grade
if (per<100 and per >=90):
    grade="A"
elif per<90 and per>=70:
    grade="B"
elif per<70 and per >=50:
    grade="C"
elif per<50 and per>=40:
    grade="D"
elif per <40:
    grade="Fail"



#opening file to insert their marks of each sunject
file=open(file_name,'a+')
file.writelines("1.\tMaths \t\t\t\t\t {} \t\t\t{}\n".format(math,g2))
file.writelines("2.\tScience \t\t\t\t {} \t\t\t{}\n".format(sci,g1))
file.writelines("3.\tEnglish \t\t\t\t {} \t\t\t{}\n".format(eng,g3))
file.writelines("4.\tHindi \t\t\t\t\t {} \t\t\t{}\n".format(hindi,g4))
file.writelines("5.\tS.S.T \t\t\t\t\t {} \t\t\t{}\n".format(sst,g5))
file.writelines("6.\tComputer \t\t\t\t {} \t\t\t{}\n".format(comp,g6))
file.writelines("-----------------------------------------------------\n")
file.writelines("TOTAL MARKS: \t\t\t\t{} \t\t{}\n".format(sum1,grade))
file.writelines("======================================================\n")
file.writelines("All OVER PERCENTAGE: {}".format(per))
file.close()
#sci=g1
#math=g2
#eng=g3
#hindi=g4
#sst=g5
#comp=g6

