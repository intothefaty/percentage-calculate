# -*- coding: utf-8 -*-

def seperate(lst):
    lsti = []
    lstf = []
    lsts = []
    for item in lst:
        try:
            lsti.append(int(item))
        except:
            try:
                lstf.append(float(item))
            except:
                lsts.append(item)
                
    return [lsts,lsti,lstf]

lst = []
f = open("data_da902dffed16a625ca6648cc52ac12cb.txt")
for line in f.readlines():
    lst.append(line[:len(line)-1])
f.close()

lstsif = seperate(lst)

strList = lstsif[0]
intList = lstsif[1]
floatList = lstsif[2]

print("Integers:",intList)
print("Floats:",floatList)
print("Strings:",strList)
