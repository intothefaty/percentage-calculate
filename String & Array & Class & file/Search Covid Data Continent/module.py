# -*- coding: utf-8 -*-

def extract_data(input_file,data_file,output_file,continent):
    f = open(input_file)
    f2 = open(data_file)
    f3 = open(output_file,"a")

    

    for line in f.readlines():
        y=f2.readline()
        x=line.find("\t")
        if line[len(line)-1]=="\n":
            z=line.find("\n")
        else:
            z=len(line)
        
        if continent==line[x+1:z]:
            f3.write(line[:x]+" "+y)
    

    f3.close()
    f2.close()
    f.close()
    
def calculate_total(file_name):
    totalCase=0
    totalDeath=0
    totalTest=0
    
    f = open(file_name)
    for line in f.readlines():
        x=line.find(" ")
        y=x+line[x+1:].find(" ")+1
        z=line.rfind(" ")
        
        totalCase+=int(line[x+1:y])
        totalDeath+=int(line[y+1:z])
        totalTest+=int(line[z+1:len(line)])
    f.close()
    result = str(totalCase)+"\t"+str(totalDeath)+"\t"+str(totalTest)
    
    return result