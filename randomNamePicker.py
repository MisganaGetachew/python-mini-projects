#random name picker
import random


while True:
    names = input("insert names seprated by coma: ")
    editedNames =  names.split(",")
    length = len(editedNames)
    number = random.randint(0, length-1)
    print(editedNames[number]+ " is going to pay the bill"+ "😀")