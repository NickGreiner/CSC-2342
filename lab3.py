# Nick Greiner
# CSC-2342-01
# 2/14/2020
# Python 3.7

import re
import sys


def menu():
    sets = set()
    set1 = set()
    set2 = set()
    output = list()
    setsList = list()

    print("Enter a set or two sets with each element separated by ',' and each set separated by '/'.")

    setInput = input("")
    setInput = re.sub(' ', '', setInput)

    if re.search("/", setInput):
        sets.update(setInput.split("/"))
        setsList = list(sets)
        set1.update(setsList[0].split(","))
        set2.update(setsList[1].split(","))

    else:
        set1.update(setInput.split(","))

    print("Enter function selection:", "(a) One-to-One", "(b) Onto", sep="\n")

    select = input("")
    select = select.lower()

    if select == "a":
        if not len(set1) < len(set2):
            print("Set cardinality invalid for function. Try with new set.")
            menu()

        set1.add(" ")
        for i in range(0, len(set2)):
            setPair = str(set1.pop()) + " → " + str(set2.pop())
            output.insert(len(output), setPair)
        print("f : ", ", ".join(output), sep="")
    elif select == "b":
        if not len(set2) < len(set1):
            print("Set cardinality invalid for function. Try with new set.")
            menu()

        element = set2.pop()
        set2.add(element + '#')
        set2.add(element + '##')
        for x in range(0, len(set2)):
            setPair = str(set1.pop()) + " → " + str(set2.pop())
            output.insert(len(output), setPair)
            output[x] = re.sub('#', '', output[x])
        print("f : ", ", ".join(output), sep="")
    else:
        print("Invalid function selection.")

    rerun = input("Run again? Y/N: ")
    rerun = rerun.upper()

    if rerun == "Y":
        menu()

    else:
        sys.exit()


menu()
