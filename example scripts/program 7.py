wubwub = open("C:/Users/20RHoh.ACC/Desktop/example scripts/shelley.txt", "r")
counter = 0
for line in wubwub:
    for letter in line:
        if line == "\n" or "":
            pass
        else:
            counter +=1
print(counter)