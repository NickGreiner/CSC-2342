# Nick Greiner
# CSC-2342-01
# 4/12/2020
# Python 3.7

import re

def convertToFraction(eventDec):
    event = int(eventDec * 1000)

    if event > 1000:
        small = 1000
    else:
        small = event
    for i in range(1, small + 1):
        if ((event % i == 0) and (1000 % i == 0)):
            gcd = i

    numerator = int(event / gcd)
    denominator = int(1000 / gcd)

    fraction = str(numerator) + "/" + str(denominator)

    return fraction


print("Start by entering two events, A and B, as either a decimal or percentage (i.e. 0.12 or 12%).")
aEvent = input("Input event A: ")
bEvent = input("Input event B: ")

if re.search('\\.', aEvent) and not re.search('%', aEvent):
    aDec = float(aEvent)
    aPercent = str(aDec * 100) + "%"

elif re.search('%', aEvent):
    aPercent = aEvent
    aDec = aEvent.replace('%', '')
    aDec = float(aDec) * .01

if re.search('\\.', bEvent) and not re.search('%', bEvent):
    bDec = float(bEvent)
    bPercent = str(bDec * 100) + "%"

elif re.search('%', bEvent):
    bPercent = bEvent
    bDec = bEvent.replace('%', '')
    bDec = float(bDec) * .01

aGivenB = (aDec * bDec) / bDec
aGivenBPercent = str(aGivenB * 100) + "%"

print("P(A) = " + str(aDec) + ", " + aPercent + ", or " + convertToFraction(aDec))
print("P(B) = " + str(bDec) + ", " + bPercent + ", or " + convertToFraction(bDec))
print("P(A|B) = " + str(aGivenB) + ", " + aGivenBPercent + ", or " + convertToFraction(aGivenB))
