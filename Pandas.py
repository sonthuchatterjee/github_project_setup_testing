import pandas as pd

grades_dict = {'A':4,'B':3,'C':2.5,'D':2}
grades = pd.Series(grades_dict)
#print(grades.values,grades.index,grades)
marks_dict = {'A':90,'B':80,'C':70,'D':60}
marks = pd.Series(marks_dict)

b = pd.DataFrame({'Grades':grades_dict,'Marks':marks})
print(b)
print(b.index['A':'C'])
#print(b.index,b['Grades'].values,b.values)
#c=b[b['Grades']> 2.5]
#print(c)

'''
d= pd.DataFrame([{'Marks':[1,2],'Grades':[3,4]}])
print(d,d.index,d.values)
print(d['Marks'].values[0])

e= pd.DataFrame([{'Marks':2,'Grades':3}])
print(e,e.index,e.values)
#print(d['Marks'].values[0])
'''
