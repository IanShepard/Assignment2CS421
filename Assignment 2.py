import xml.etree.ElementTree as ET
import sys
import tabulate

with open('googleplayapps.xml') as f:
    xml = f.read()

def main():
    fileType = chooseFileType()

    if (fileType == "consumer financial services"):
        print("consumer financial services")

    displayType = chooseDisplayType()

    fileMethod = combineFileAndDisplayType(fileType, displayType)

def chooseFileType():
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
    elif (file == "xml"):
        if (display == "single record"):
            xmlSingleRecord()
        elif (display == "whole column"):
            xmlWholeColumn()
        elif (display == "sort"):
            xmlSort()
            #displayWholeXML()
            return "XML and SORT"
    elif (file == "json"):
        if (display == "single record"):
            #jsonSingleRecord()
            return "JSON and SINGLE RECORD"
        elif (display == "whole column"):
            #jsonWholeColumn()
            return "JSON and WHOLE COLUMN"
        elif (display == "sort"):
            #jsonSort()
             return "JSON and SORT"

def displayWholeXML():
    tree = ET.fromstring(xml)

    print("%30s %20s %5s %8s %8s %13s %6s %6s %9s %16s %11s %18s %15s" % (tree[1][0].tag, tree[1][1].tag, tree[1][2].tag, tree[1][3].tag, tree[1][4].tag, tree[1][5].tag, tree[1][6].tag, tree[1][7].tag, tree[1][8].tag, tree[1][9].tag, tree[1][10].tag, tree[1][11].tag, tree[1][12].tag), end='')
    print()
    print()

    for i in range(33):
        print("%30s %20s %5s %8s %8s %13s %6s %6s %12s %18s %11s %18s %15s" % (tree[i][0].text, tree[i][1].text, tree[i][2].text, tree[i][3].text, tree[i][4].text, tree[i][5].text, tree[i][6].text, tree[i][7].text, tree[i][8].text, tree[i][9].text, tree[i][10].text, tree[i][11].text, tree[i][12].text))

def xmlSingleRecord():
    root = ET.fromstring(xml)

    print("Which row would you like to display?")
    print("I.E. number between 1 - 33")

    option = int(input(">>> ")) - 1

    for i in range(33):
        if (option == i):
            print("%3s.  " % (i+1), end='')
            for j in range(13):
                print(root[i][j].text,"   ", end='')
    print()
    main()

def xmlWholeColumn():
    rootlist = []

    root = ET.fromstring(xml)
    print(end='')
    print("Which column would you like to display?")

    print("I.E.", " ", end='')
    for i in range(13):
        print(root[1][i].tag,", ", end='')
        rootlist.append(root[1][i].tag)
    print()

    option = str(input(">>> "))

    for i in range(13):
        if (option == root[1][i].tag):
            categoryIndex = i

            print("%30s" % (root[1][i].tag))
            print()
            for j in range(33):
                print("%30s" % (root[j][categoryIndex].text))
    main()

def xmlSort():

    tree = ET.fromstring(xml)

    rootlist = []

    print("Which category would you like to sort by?")

    print("I.E.", " ", end='')
    for i in range(13):
        print(tree[1][i].tag,", ", end='')
        rootlist.append(tree[1][i].tag)
    print()

    option = str(input(">>> "))

    temp = []

    for j in range(33):
        map = {tree[j][0].tag: tree[j][0].text, tree[j][1].tag : tree[j][1].text, tree[j][2].tag : tree[j][2].text, tree[j][3].tag : tree[j][3].text, tree[j][4].tag : tree[j][4].text, tree[j][5].tag : tree[j][5].text, tree[j][6].tag : tree[j][6].text, tree[j][7].tag : tree[j][7].text, tree[j][8].tag : tree[j][8].text, tree[j][9].tag : tree[j][9].text, tree[j][10].tag : tree[j][10].text, tree[j][11].tag : tree[j][11].text, tree[j][12].tag : tree[j][12].text}
        temp.append(map)

    sortedlist = sorted(temp, key = lambda i: i[option])
    header = sortedlist[0].keys()
    rows =  [x.values() for x in sortedlist]
    print(tabulate.tabulate(rows, header))

    main()

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

def calculateComplaints():
    print("calcualting complaints...")
    main()

main()
