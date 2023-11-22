blba = open("C:/Users/20RHoh.ACC/Desktop/example scripts/shelley.txt", "r")
count = 0
emcount = 0
for line in blba:
    if line == "\n":
        emcount +=1
    else:
        count +=1
print(count, emcount)
blba.close()