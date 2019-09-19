import xml.etree.ElementTree as ET
import json
import sys
import tabulate

with open('googleplayapps.xml') as f:
    xml = f.read()

with open('googleplayapps.json') as file1:
    json = json.load(file1)

def main():
    #program controller
    run = True
    while(run):
        fileType = chooseFileType()

        if (fileType == "consumer financial services"):
            print("consumer financial services")

        displayType = chooseDisplayType()

        fileMethod = combineFileAndDisplayType(fileType, displayType)

        run = chooseToContinue()

def chooseFileType():
    #selects a file type or uses consumer financial services
    print("----------------------------------------------------")
    print("Choose a file type to analyse.")
    print("Type '1' for CSV")
    print("Type '2' for XML")
    print("Type '3' for JSON")
    print("Type '4' to enter 'Consumer Financial Services Mode'")
    print("Type any other key to quit")
    print("----------------------------------------------------")

    try:
        option = int(input(">>> "))
    except Exception as e:
        sys.exit(0)

    if (option == 1):
        #CSV chosen
        return "csv"
    elif (option == 2):
        #XML chose
        return "xml"
    elif (option == 3):
        #JSON chosen
        return "json"
    elif (option == 4):
        calculateComplaints()
        return "consumer financial services"
    else:
        return

def chooseDisplayType():
    #chooses how you sort the data
    print("-----------------------------------------------------")
    print("Choose a way to display the data.")
    print("Type '1' to display a single record by its row number")
    print("Type '2' to display a whole column by its name")
    print("Type '3' sort and display dataset by input")
    print("-----------------------------------------------------")

    option = int(input(">>> "))

    if (option == 1):
        #Single Record chosen
        return "single record"
    elif (option == 2):
        #Whole Column chose
        return "whole column"
    elif (option == 3):
        #sort chosen
        return "sort"
    else:
        return

def combineFileAndDisplayType(file, display):
    #sorts gets filetyoe and displaytype and runs the proper function

    #methods for filetype CSV
    if (file == "csv"):
        if (display == "single record"):
            #csvSingleRecord()
            return "CSV and SINGLE RECORD"
        elif (display == "whole column"):
            #csvWholeColumn()
            return "CSV and WHOLE COLUMN"
        elif (display == "sort"):
            #csvSort()
            return "CSV and SORT"
    #methods for filetype XML
    elif (file == "xml"):
        if (display == "single record"):
            xmlSingleRecord()
        elif (display == "whole column"):
            xmlWholeColumn()
        elif (display == "sort"):
            xmlSort()
            #displayWholeXML()
            return "XML and SORT"
    #methods for filetype JSON
    elif (file == "json"):
        if (display == "single record"):
            #jsonSingleRecord()
            jsonSingleRow()
        elif (display == "whole column"):
            #jsonWholeColumn()
            jsonSingleCol()
        elif (display == "sort"):
            #jsonSort()
            jsonSortedBy()

def chooseToContinue():
    print("""-----------------------------------------------------
    Would you like to continue or exit?
    Type '1' to continue
    Type '2' to exit
    -----------------------------------------------------""")

    option = int(input(">>>"))

    if (option == 1):
        return True
    elif (option == 2):
        return False

def xmlSingleRecord():
    root = ET.fromstring(xml)

    print("Which row would you like to display?")
    print("I.E. number between 1 -", len(root))

    option = int(input(">>> ")) - 1

    for i in range(len(root)):
        if (option == i):
            print("%3s.  " % (i+1), end='')
            for j in range(len(root[0])):
                print(root[i][j].text, "   ", end='')
    print()

def xmlWholeColumn():
    rootlist = []

    root = ET.fromstring(xml)
    print(end='')
    print("Which column would you like to display?")

    print("I.E.", " ", end='')
    for i in range(len(root[0])):
        print(root[1][i].tag,", ", end='')
        rootlist.append(root[1][i].tag)
    print()

    option = str(input(">>> "))

    for i in range(len(root[0])):
        if (option == root[1][i].tag):
            categoryIndex = i

            print("%30s" % (root[1][i].tag))
            print()
            for j in range(len(root)):
                print("%30s" % (root[j][categoryIndex].text))

def xmlSort():

    tree = ET.fromstring(xml)

    rootlist = []

    print("Which category would you like to sort by?")

    print("I.E.", " ", end='')
    for i in range(len(tree[0])):
        print(tree[1][i].tag,", ", end='')
        rootlist.append(tree[1][i].tag)
    print()

    option = str(input(">>> "))

    temp = []

    #Converts elemetnTree into a LIST of LISTs
    for j in range(len(tree)):
        list = []
        for n in range(len(tree[0])):
            list.append(tree[j][n].tag)
            list.append(tree[j][n].text)
        temp.append(list)

    #Converts string of numbers into Int
    for k in range(len(tree)):
        list = []
        for m in range(len(tree[0])):
            if (hasNumbers(temp[k][m])):
                try:
                    newvalue = temp[k][m].replace(',', '')
                    temp[k][m] = float(newvalue)
                except Exception as e:
                    continue

    outputlist = []
    for m in range(len(temp)):
        i = iter(temp[m])
        newtemp = dict(zip(i, i))
        outputlist.append(newtemp)

    sortedlist = sorted(outputlist, key = lambda i: i[option])

    header = sortedlist[0].keys()
    rows =  [x.values() for x in sortedlist]
    print(tabulate.tabulate(rows, header, floatfmt=".1f"))

def jsonSingleRow():
    rowNum = int(input("Choose a row number>>> "))
    print(rowNum, json[rowNum - 1])

def jsonSingleCol():
    colName = jsonChooseColName()
    #dispaly the column in a nice way
    for element in range(len(json)):
        print(str(element) + " " + json[element][colName])

def jsonSortedBy():
    colName = jsonChooseColName()
    sortedList = sorted(json, key=lambda i: i[colName])
    #display the sortedList in a nice(ish) way
    for i in range(len(sortedList)):
        print(str(i) + " " + sortedList[i][colName])
        print(sortedList[i])

def jsonChooseColName():
    print("Options available:", "[OPTIONS]") #TODO [OPTIONS] should be the headers read from the json file
    colName = input("Choose a colomn name>>> ")
    return colName

#Checks to see if a map key value should be an int instead of str
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def calculateComplaints():
    print("calcualting complaints...")
    main()

main()
