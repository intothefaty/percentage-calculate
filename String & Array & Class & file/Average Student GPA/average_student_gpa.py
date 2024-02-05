# -*- coding: utf-8 -*-

import read_file

class Student:
    _Id = None
    _name = None
    _surname = None
    _overall = None
    
    def __init__(self, Id, name, surname):
        self._Id = Id
        self._name = name
        self._surname = surname    
    
    def getId(self):
        return self._Id
    
    def getName(self):
        return self._name
    
    def getSurname(self):
        return self._surname
    
    def getOverall(self):
        return self._overall
    
    def calculate_overall(self,x,y,z):
        overall = (x*25+y*35+z*40)/100
        self._overall = overall
    
    def __lt__(self,other):
        return self._overall<other.getOverall()
    
    def __str__(self):
        return F'Id: {self._Id}\nName: {self._surname} {self._name}\nOverall Grade: {self._overall}'
    
    def __repr__(self):
        return F'Id: {self._Id}\nName: {self._surname} {self._name}\nOverall Grade: {self._overall}'
    
sList = read_file.read_file("student_1.txt")
Id = input("Enter student id: ")

for student in sList:
    if student[0]==Id:
        s = Student(Id, student[1], student[2])
        s.calculate_overall(student[-3], student[-2], student[-1])

try:
    print(s.__repr__())
    print("\n")
except:
    print("There is no such a student\n\n")


#sort
def takeLast(item):
    return item[-1]

for i in range(len(sList)):
    sx = Student("", "", "")
    sx.calculate_overall(sList[i][3], sList[i][4], sList[i][5])
    sList[i].pop()
    sList[i].pop()
    sList[i].pop()
    sList[i].append(sx.getOverall())  

sortedList = []
sList.sort(key=takeLast)

for student in sList:
    sortedList.append("Id:"+student[0]+" Name:"+student[2]+" "+student[1][0].upper()+". Overall Grade:"+str(student[3]))

print("Sorted List according to the Overall:")
print(sortedList)    
        




