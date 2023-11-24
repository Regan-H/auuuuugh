womp = open("C:/Users/20RHoh.ACC/Desktop/example scripts/Shelley.txt", "r")
start, end = input("Insert the start and end range you want printed\n").split()
start = int(start)
end = int(end)
temp = []
for line in womp:
    temp.append(line)
for i in range(start-1, end):
    print(temp[i].strip())
womp.close()