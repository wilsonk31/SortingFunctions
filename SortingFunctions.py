#Wilson Keungkhamphong
#CS 222 01
#Final A
#Program that analizing 3 diffrent sorting methods. Using time in seconds for measurement.

import random
import time

def bubbleSort(aList):
    exchanges=True
    passnum=len(aList)-1
    while passnum > 0 and exchanges:
        exchanges=False
        for i in range(passnum):
            if aList[i] > aList[i + 1]:
                exchanges=True
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp

def selectionSort(aList):
    for fillslot in range(len(aList) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if aList[location] > aList[positionOfMax]:
                positionOfMax = location
        temp = aList[fillslot]
        aList[fillslot] = aList[positionOfMax]
        aList[positionOfMax] = temp


def insertionSort(aList):
    for index in range(1, len(aList)):
        currentValue = aList[index]
        position = index
        while position > 0 and aList[position - 1] > currentValue:
            aList[position] = aList[position - 1]
            position = position - 1
        aList[position] = currentValue

def createList(size): #Creates a list of random numbers
    lyst = []
    temp = []
    while len(lyst) < size: #for how many nums in lyst
        num = random.randint(1, 1000)
        lyst.append(num)
    return lyst

def printList(lyst):
    count = 0
    for num in lyst:
        print("%6d" % num, end == "")
        count += 1
        if count == 10:
            count = 0
            print()

def main():
    print("Creating List....")
    lyst = createList(100)
    lyst_A=list(lyst)
    lyst_B=list(lyst)


    lyst1k = createList(1000)
    lyst1k_A=list(lyst1k)
    lyst1k_B=list(lyst1k)



    lyst10k = createList(10000)
    lyst10k_A=list(lyst10k)
    lyst10k_B=list(lyst10k)

    #--------------------------100 Sorting---------------------------------->
    print("<--------------------------100 Sorting------------------------------------->")

    print("\n----------100 Bubble Sorting---------------->")
    StartTime=time.time()
    print("Time Started...")
    print("\n")
    print("\n 100 List Buble Sorting......>")
    bubbleSort(lyst)
    print("Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)

    print("\n----------100 Selection Sorting---------------->")
    StartTime=time.time()
    print("Time Started...")
    print("\n")
    print("\n 100 List Selection Sorting......>")
    selectionSort(lyst_A)
    print("Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)

    print("\n----------100 Insertion Sorting---------------->")
    StartTime=time.time()
    print("Time Started...")
    print("\n")
    print("\n 100 List Insertion Sorting......>")
    insertionSort(lyst_B)
    print("Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)



    #--------------------------1k Sorting------------------------------------->
    print("<--------------------------1k Sorting------------------------------------->")

    print("\n----------1k Bubble Sorting----------------->")
    StartTime=time.time()
    print("Time Started...")
    print("\n")
    print("\n 1k List Bubble Sorting.....>")
    bubbleSort(lyst1k)
    print("Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)


    print("\n----------1k Selection Sorting---------------->")
    StartTime=time.time()
    print("Time Started...")
    print("\n")
    print("\n 1k List Selection Sorting......>")
    selectionSort(lyst1k_A)
    print("Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)

    print("\n----------1k Insertion Sorting---------------->")
    StartTime=time.time()
    print("Time Started...")
    print("\n")
    print("\n 1k List Insertion Sorting......>")
    insertionSort(lyst1k_B)
    print("Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)

    #---------------------10k Sorting------------------------------------->
    print("<--------------------------10k Sorting------------------------------------->")

    print("\n----------10k Bubble Sorting---------------->")
    StartTime=time.time()
    print("Time Started...")
    print("\n")
    print("\n 10k List Bubble Sorting.....>")
    bubbleSort(lyst10k)
    print("Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)



    print("\n----------10k Selection Sorting---------------->")
    StartTime=time.time()
    print("Time Started...")
    print("\n")
    print("\n 10k List Selection Sorting......>")
    selectionSort(lyst10k_A)
    print("Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)

    print("\n----------10k Insertion Sorting---------------->")
    StartTime=time.time()
    print("Time Started...")
    print("\n")
    print("\n 10k List Insertion Sorting......>")
    insertionSort(lyst10k_B)
    print("Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)


    print("Done Running")

main()
