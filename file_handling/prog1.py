#file handling
#read only mode
'''
try:
    readFile = open("abc.txt", "r+")
    print(readFile.read())
    readFile.close()
except FileExistsError:
    print("No such file exists")
'''
## read file line by line
'''
try:
    readFile = open("abc.txt","r")
    readingLine = readFile.readline()
    while readingLine != '':
        print(readingLine,end= '')
        readingLine = readFile.readline()  # update readingLine

    readFile.close()
except FileExistsError:
    print("No such file exists")
'''

## read file line by line and add abc at end of line
'''
try:
    readFile = open("abc.txt","r")
    readingLine = readFile.readline()
    while readingLine != '':
        print(readingLine,end= 'abc')
        readingLine = readFile.readline()
except FileExistsError:
    print("No such file exists")

'''

 #w - writes over the original file a - add the new text at the EOF of OG text
'''
try:
    newText = "\nHow are you ? Nice to meet you !  !"
    openFile = open('abc.txt', "a")
    openFile.writelines(newText)
    print("Done Writing")
    openFile.close()

     #Read the updated file
    with open("abc.txt", "r") as file:
        print("\nUpdated File Content:")
        for line in file:
            print(line, end="")
except FileExistsError:
    print("No such file")

    '''
'''
# create a new file exclusively
try:
    with open("xyz.txt", "x") as file:
        file.write("This file was created exclusively\n")
except FileExistsError:
    print("Error: xyz.txt already exists")
'''

# OS module

import os
fnm = "xyz.txt"
try:
    if os.path.exists(fnm):
        os.remove(fnm)
        print('File - ', fnm, 'has been deleted !!')
except FileNotFoundError as e:
    print(f"Error: {e}. File not found.")
