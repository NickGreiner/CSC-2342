# Nick Greiner
# CSC-2342-01
# 1/29/2020
# Python 3.7

import re
import itertools
import copy


def dictionaryFunc():
    print("Welcome to the dictionary.", "Enter exit to return to program.", "", sep="\n")

    dictionary = {'and': 'Both variables have to be true for and to be true', 'or': 'Only one variable has to be true for or to be true', 'implies': 'If proposition 1 is true, proposition 2 must be true for implies to be true. If proposition 1 is false, implies is automatically true.'}

    dictionarySearch = input("Enter term: ")

    dictionarySearch = dictionarySearch.lower()

    if dictionarySearch == "exit":
        menu()
    else:
        if dictionarySearch == "and" or dictionarySearch == "/\\":
            print(dictionary.get('and'), "\n")
            dictionaryFunc()
        elif dictionarySearch == "or" or dictionarySearch == "\\/":
            print(dictionary.get('or'), "\n")
            dictionaryFunc()
        elif dictionarySearch == "implies" or dictionarySearch == ">":
            print(dictionary.get('implies'), "\n")
            dictionaryFunc()
        else:
            print("Unknown value, returning to menu.")
            menu()


def splitStatement(statement):
    statementPart = statement[statement.find("(")+1:statement.find(")")]
    return statementPart


def menu():
    print("Welcome to the program. To start, enter a propositional statement.", "Valid connectives: /\ = and, \/ = or, "
                                                                                "> = implies. Negation is ~.",
          "Example input: p /\ q or (p \/ q) /\ ~r", "Enter dictionary to enter dictionary menu,", "or exit to terminate program.", "", sep="\n")
    fullStatement = input("Enter statement: ")
    fullStatement = fullStatement.lower()

    if fullStatement == "dictionary" or fullStatement == "dict":
        dictionaryFunc()

    elif fullStatement == "exit":
        return

    else:
        if not re.search("^[a-z \x2F \x3E \x5A-\x5E \x28 \x29 \x7E]*$", fullStatement):
            print("Error! Only letters a-z allowed!")
            while not re.search("^[a-z \x2F \x3E \x5A-\x5E \x28 \x29 \x7E]*$", fullStatement):
                fullStatement = input("Enter statement: ")

        variables = re.split(" /\\\ | \\\/ | > ", fullStatement)
        for i in range(0, len(variables)):
            variables[i] = re.sub('\\(', '', variables[i])
            variables[i] = re.sub('\\)', '', variables[i])

        variTable = [i for i in itertools.product(['T', 'F'], repeat=len(variables))]
        logicVariTable = copy.deepcopy(variTable)

        for i in range(0, len(variables)):
            if re.search('~', variables[i]):
                x = 0
                for row in logicVariTable:
                    logicVariTable[x] = list(logicVariTable[x])
                    if logicVariTable[x][i] == "T":
                        logicVariTable[x][i] = "F"
                    else:
                        logicVariTable[x][i] = "T"
                    x = x + 1
                variables[i] = re.sub('~', '', variables[i])

        partStatements = []
        if re.search('\\)', fullStatement):
            lastStatementPart = fullStatement
            while re.search('\\)', lastStatementPart):
                partStatements.append(splitStatement(lastStatementPart))
                lastStatementPart = partStatements[len(partStatements) - 1]


        if not partStatements == []:
            printStatements = ' | '.join(partStatements) + ' |'
        else:
            printStatements = ""

        if len(variables) == 1:
            print(' '.join(variables), "\n", "T", "\n", "F")
            return

        print(' '.join(variables), "|", printStatements, fullStatement)

        if partStatements == []:

            if re.search(" > ", fullStatement):
                connective = "implies"
            elif re.search(" /\\\ ", fullStatement):
                connective = "and"
            elif re.search(" \\\/ ", fullStatement):
                connective = "or"
            else:
                connective = ""

            x = 0
            if connective == "and":
                for row in variTable:
                    variString = ""
                    for i in range(0, len(variables)):
                        variString = variString + logicVariTable[x][i]
                    if (re.search("T", variString) and not re.search("F", variString)):
                        result = "T"
                    elif (re.search("F", variString) and not re.search("T", variString)):
                        result = "T"
                    else:
                        result = "F"
                    x = x + 1
                    print(' '.join([str(elem) for elem in row]), "|", result)

            elif connective == "or":
                for row in variTable:
                    if logicVariTable[x][0] == "T" or logicVariTable[x][1] == "T":
                        result = "T"
                    else:
                        result = "F"
                    x = x + 1
                    print(' '.join([str(elem) for elem in row]), "|", result)

            elif connective == "implies":
                for row in variTable:
                    if logicVariTable[x][0] == "T" and logicVariTable[x][1] == "F":
                        result = "F"
                    else:
                        result = "T"
                    x = x + 1
                    print(' '.join([str(elem) for elem in row]), "|", result)

        else:
            resultsTable = []
            remainStatement = fullStatement

            for i in range(0, len(partStatements)):

                if re.search(" > ", partStatements[0]):
                    connective = "implies"
                    remainStatement = re.sub('>', '', remainStatement)
                elif re.search(" /\\\ ", partStatements[0]):
                    connective = "and"
                    remainStatement = re.sub(' /\\\ ', '', remainStatement)
                elif re.search(" \\\/ ", partStatements[0]):
                    connective = "or"
                    remainStatement = re.sub(' \\\/ ', '', remainStatement)
                else:
                    connective = ""

                x = 0
                if connective == "and":
                    for row in variTable:
                        if (logicVariTable[x][0] == "T" and logicVariTable[x][1] == "T") or (logicVariTable[x][0] == "F" and logicVariTable[x][1] == "F"):
                            resultsTable.append('T')
                        else:
                            resultsTable.append('F')
                        x = x + 1

                elif connective == "or":
                    for row in variTable:
                        if logicVariTable[x][0] == "T" or logicVariTable[x][1] == "T":
                            resultsTable.append('T')
                        else:
                            resultsTable.append('F')
                        x = x + 1

                elif connective == "implies":
                    for row in variTable:
                        if logicVariTable[x][0] == "T" and logicVariTable[x][1] == "F":
                            resultsTable.append('F')
                        else:
                            resultsTable.append('T')
                        x = x + 1

            if re.search(" > ", remainStatement):
                connective = "implies"
            elif re.search(" /\\\ ", remainStatement):
                connective = "and"
            elif re.search(" \\\/ ", remainStatement):
                connective = "or"
            else:
                connective = ""

            x = 0
            if connective == "and":
                for row in variTable:
                    if (logicVariTable[x][2] == "T" and resultsTable[x] == "T") or (
                            logicVariTable[x][2] == "F" and resultsTable[x] == "F"):
                        result = "T"
                    else:
                        result = "F"
                    print(' '.join([str(elem) for elem in row]), "| ", resultsTable[x], " | ", result)
                    x = x + 1

            elif connective == "or":
                for row in variTable:
                    if logicVariTable[x][2] == "T" or resultsTable[x] == "T":
                        result = "T"
                    else:
                        result = "F"
                    print(' '.join([str(elem) for elem in row]), "| ", resultsTable[x], " | ", result)
                    x = x + 1

            elif connective == "implies":
                for row in variTable:
                    if logicVariTable[x][2] == "T" and resultsTable[x] == "F":
                        result = "F"
                    else:
                        result = "T"
                    print(' '.join([str(elem) for elem in row]), "| ", resultsTable[x], " | ", result)
                    x = x + 1


menu()
