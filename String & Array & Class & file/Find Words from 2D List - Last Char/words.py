# -*- coding: utf-8 -*-

def formSentence(inList,endStr):
    result = []
    for listt in inList:
        for item in listt:
            if item[len(item)-len(endStr):len(item)].upper() == endStr.upper():
                result.append(item)
    return result
    

inList = [
    ['This', 'is', 'lab', 'Script'],
    ['HIS', 'THESIS', 'Will', 'FINISH'],
    ['we', 'have', 'big', 'crisis']
    ]
print("Two Dimensional List:")
print(inList)
endStr = input("What is the ending string: ")
print("Words that end with",endStr,":")
print(formSentence(inList, endStr))



