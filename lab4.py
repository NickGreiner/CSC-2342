# Nick Greiner
# CSC-2342-01
# 2/27/2020
# Python 3.7

print("Enter a sequence of integers separated by commas.")
seqInput = input("Input sequence: ")

sequence = seqInput.replace(" ", "").split(",")

for x in range(0, len(sequence)):
    sequence[x] = int(sequence[x])

d = sequence[1] - sequence[0]
r = sequence[2] / sequence[1]

if sequence[2] == sequence[0] + (3-1) * d:
    print("Your input ", sequence, " is a arithmetic sequence.", sep="")

elif sequence[2] == sequence[0] * pow(r, (3-1)):
    print("Your input ", sequence, " is a geometric sequence.", sep="")

else:
    print("Your input ", sequence, " is a unknown sequence.", sep="")
