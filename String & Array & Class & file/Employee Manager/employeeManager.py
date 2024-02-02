# -*- coding: utf-8 -*-

import instructor

def read_file(filename):
    employees = {}
    
    f = open(filename,"r")
    rowCount = len(list(f))
    f.close()
    
    f = open(filename,"r")
    for i in range(rowCount):
        x = f.readline()
        x=x[:len(x)-1]
        
        list1 = x.split(";")
        
        employees.update({list1[0]:list1[1:]})
    return employees

def searchId(employees,search_id):
    count = 0
    for x in employees:
        if(x==search_id):
            count+=1
            employee = instructor.Instructor(x,employees[x][0],employees[x][1],int(employees[x][2]))
            print("")
            print("Name : " + employee.get_name())
            print("Status : " + employee.get_status())
            print("Salary : " + str(employee.calculate_salary()))
    return count
        
def searchStatus(employees,status):
    count = 0
    for x in employees:
        if(employees[x][1]==status):
            count+=1
            employee = instructor.Instructor(x,employees[x][0],employees[x][1],int(employees[x][2]))
            print("")
            print("Id : " + x)
            print("Name : " + employee.get_name())
            #print("Status : " + employee.get_status())
            print("Salary : " + str(employee.calculate_salary()))
    return count
            

employees = read_file("instructor.txt")

while (True):
    choose = input("\nsearch with id (i), search with status (s), quit (q): ")
    if(choose.lower()=="i"):
        search_id = str(input("Enter Id : "))
        cond = searchId(employees,search_id)
        if cond == 0:
            print("There is no employee with an id")
    elif(choose.lower()=="s"):
        status = input("Enter Status (F)(P) : ")
        cond  = searchStatus(employees,status.upper())
        if cond == 0:
            print("There is no employee with this status")
    elif(choose.lower()=="q"):
        break
    else:
        print("You made an incorrect entry..")

    
    


