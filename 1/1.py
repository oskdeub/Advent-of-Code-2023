print("Reading file")
with open ('input.txt') as input:
    lines = input.readlines()

for x in lines:
    print(x)  