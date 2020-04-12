# Nick Greiner
# CSC-2342-01
# 2/07/2020
# Python 3.7

# At time of comment (10:51 PM, 2/12/2020) program runs correctly using default .txt files but runs
# incorrectly with blank filetype, i.e. "FileA".

# If this is not fixed by final submission, please add .txt files to directory and run without
# parameters to at least test the rest of the program.

import sys
import os.path

setA = set()
setB = set()
setC = set()

if len(sys.argv) == 1:
    if os.path.exists("FileA.txt") and os.path.exists("FileB.txt") and os.path.exists("FileC.txt"):
        setA.update(open("FileA.txt").read().split(", "))
        setB.update(open("FileB.txt").read().split(", "))
        setC.update(open("FileC.txt").read().split(", "))
    else:
        sys.exit("No input files found, try adding them as CLI parameters.")

else:
    setA.update(open(sys.argv[1]).read().split(", "))
    setB.update(open(sys.argv[2]).read().split(", "))
    setC.update(open(sys.argv[3]).read().split(", "))

allNames = set()
for i in setA:
    if i not in allNames:
        allNames.add(i)
for i in setB:
    if i not in allNames:
        allNames.add(i)
for i in setC:
    if i not in allNames:
        allNames.add(i)

print("All names:", ', '.join(allNames))
print("Enter two sets and the operation to run, i.e. 'A union B'")

command = input("Input: ")

set1 = set()
set2 = set()

if "union" in command:
    sets = command.split(" union ")
    if sets[0] == "A":
        set1 = setA
    if sets[0] == "B":
        set1 = setB
    if sets[0] == "C":
        set1 = setC
    if sets[1] == "A":
        set2 = setA
    if sets[1] == "B":
        set2 = setB
    if sets[1] == "C":
        set2 = setC
    print("Cardinality of ", sets[0], " = ", len(set1), ", cardinality of ", sets[1], " = ", len(set2), sep="")
    print("Union:", ', '.join(set1.union(set2)))

if "intersect" in command:
    sets = command.split(" intersect ")
    if sets[0] == "A":
        set1 = setA
    if sets[0] == "B":
        set1 = setB
    if sets[0] == "C":
        set1 = setC
    if sets[1] == "A":
        set2 = setA
    if sets[1] == "B":
        set2 = setB
    if sets[1] == "C":
        set2 = setC
    print("Cardinality of ", sets[0], " = ", len(set1), ", cardinality of ", sets[1], " = ", len(set2), sep="")
    print("Intersection:", ', '.join(set1.intersection(set2)))

if "product" in command:
    sets = command.split(" product ")
    list1 = []
    list2 = []
    if sets[0] == "A":
        list1 = list(setA)
    if sets[0] == "B":
        list1 = list(setB)
    if sets[0] == "C":
        list1 = list(setC)
    if sets[1] == "A":
        list2 = list(setA)
    if sets[1] == "B":
        list2 = list(setB)
    if sets[1] == "C":
        list2 = list(setC)
    print("Cardinality of ", sets[0], " = ", len(list1), ", cardinality of ", sets[1], " = ", len(list2), sep="")
    print("Product: ", end="")

    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            print("{", list1[i], ", ", list2[j], "}, ", sep="", end="")
