# -*- coding: utf-8 -*-

def read_file(fname):
    sList = []
    f = open(fname)
    for line in f.readlines():
        ggwp = line[:len(line)-1].split(",")
        Id = ggwp[0]
        name = ggwp[1]
        surname = ggwp[2]
        x = int(ggwp[3])
        y = int(ggwp[4])
        z = int(ggwp[5])
        sList.append([Id,name,surname,x,y,z])
    return sList