# -*- coding: utf-8 -*-

def fromSentence(inList,searchChr):
    if searchChr=='0':
        return "QUIT"
    result=""
    for wordList in inList:
        for word in wordList:
            if(word[0].upper()==searchChr.upper()):
                result+=word + " - "
    if result == "":
        return "There is no word starting with this letter"
    else:
        return "There is - " + result


inList = [
    ['This', 'is', 'lab', 'Script'],
    ['We', 'should', 'finish', 'it'],
    ['we', 'solve', 'some', 'questions']]

searchChr = 'x'
while(searchChr != '0'):
    print("\n'0' for quit")
    searchChr = input("Enter a character : ")
    
    print(fromSentence(inList,searchChr))