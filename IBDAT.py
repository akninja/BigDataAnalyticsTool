# THIS HAS BEEN ALTERED SO THE CODE IS IMMMUTABLE
# Author: Alex Knoepfler
#
# A generic big-data analytics tool that displays unique occurences of
# classes in a specified common.  It also calculates the ratios for
# each class.
import numpy as np
import statistics as statistics

#Places a selected column in a linear array for processing
#Returns the unique instances of classes and the number of classes
#Passes unique, out, lists to statistics function.

def extractCol(filepath, n):

    out =[] #Hold ALL classes
    with open(filepath,'r') as datafile:
        for line in datafile:
                out.append(line.split(',')[n])
                format ='\n'.join(out)
                makeDataSet(format,n)

def booleanToCol(out):
        normal = "normal.\n"
        newCol = open("C:/Users/ajkno/Desktop/New42.txt", 'w+')
        for i in out:
            if i == normal:
                    newCol.write("0, \n")
            else:
                    newCol.write("1, \n")

def makeDataSet(format, n):
    newData = open("column.txt", 'w')

    header = "col"
    header += str(n)
    header = header +"\n"

    newData.write(header)
    newData.write(format)
def uniqueClasses(filepath, n):

    with open(filepath, "r") as infile:
        out =[] #Hold ALL classes
        unique = [] #Holds the unique occurences of each class


        for line in infile:
            line = line.strip()
            out.append(line.split(',')[n])

        unique.extend(np.unique(out))

        #numeric(unique)#Uncomment if and only if column is numeric
        print (unique, "\n\nNumber of Classes: ", len(unique))

        stats(out, unique)
        #booleanToCol(out)
#Input parameters are out, unique lists
#Calculates ratios for each class.
def numeric(unique):
    unique.sort(key=int) #Lists numbers in ascending order.
    print("\nMin: ",min(unique, key=int),"\nMax: ",max(unique, key=int),"\nMedian: ",statistics.median(unique))

def stats(out, unique):
    count = 0
    j = 0

    for j in range (0,len(unique)):
        for i in out:
            if i == unique[j]:
                    count = count + 1
        print(unique[j], ": {0:.6f}".format(count/ len(out)))
        count = 0 #Re-initializes the count

#Main, specifies file path, selects columns via user input.
#Note that I have made the filepath fixed.
#Uncomment lines 38/39 to take a user input for filepath
def main():
    #filepath = "C:\Data\kddcup.data.txt" #input("Enter file path: ")
    f2 = "C:/Data/kddcup.data.txt"
    newFourTwo = "C:/Users/ajkno/Desktop/New42.txt"
    for n in range (41, 42):
        print("\nColumn", n , "Classes\n\n")
        uniqueClasses(f2, n)
        #extractCol(filepath,n)
        #for m in range(41,42):
        #print("\n\nColumn 41 statistics with normal, satan,neptune, etc. as data\n\n")
        #uniqueClasses(filepath, m)
main()
