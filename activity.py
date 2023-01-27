#pip install XlsxWriter
import xlsxwriter

#creating a list dictionaries to store the content of the excel sheet 

data = [
    {
        'Name':"Amy",
        'Grade':2,
        'School':'St.Mary High School'
    },
    {
        'Name':"Amy",
        'Grade':2,
        'School':'St.Mary High School'
    },
    {
        'Name':"Amy",
        'Grade':2,
        'School':'St.Mary High School'
    },
    {
        'Name':"Anu",
        'Grade':2,
        'School':'St.Mary High School'
    },
    {
        'Name':"Aleesha",
        'Grade':2,
        'School':'St.Mary High School'
    },
    {
        'Name':"Ava",
        'Grade':2,
        'School':'St.Mary High School'
    },
    {
        'Name':"Arya",
        'Grade':2,
        'School':'St.Mary High School'
    }
]

#create an object 
student_data = xlsxwriter.Workbook("task1_1.xlsx")
worksheet = student_data.add_worksheet("firstsheet")

# SYNTAX ---> .write(row, column, name)
worksheet.write(0,0,"#")
worksheet.write(0,1,"Name")
worksheet.write(0,2,"Grade")
worksheet.write(0,3,"School")

for index, value in enumerate(data):
    worksheet.write(index+1,0,str(index))
    worksheet.write(index+1,1,value["Name"])
    worksheet.write(index+1,2,value["Grade"])
    worksheet.write(index+1,3,value["School"])

student_data.close()