djmusicman = open("C:/Users/20RHoh.ACC/Desktop/example scripts/shelley.txt", "r")
full = []
counter = 0
for line in djmusicman:
    if line == "\n" or "":
            pass
    else:
        full.append(line)
full.reverse()
print("\n".join(full))