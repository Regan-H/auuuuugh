deedee = open("C:/Users/20RHoh.ACC/Desktop/example scripts/numbers.txt", "r")
tot= 0
for line in deedee:
    line.strip()
    if line == "\n":
        pass
    else:
        line = int(line)
        print(tot)
        tot += line
print(tot)
deedee.close()