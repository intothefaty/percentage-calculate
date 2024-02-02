# -*- coding: utf-8 -*-

sentence = input("Enter the sentence : ")

sentences = sentence.split()

sentences.sort()
print("\nRESULT")
for i,sentence in enumerate(sentences):
    print(str(i+1) + ". " + sentence)
