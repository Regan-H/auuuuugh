'''
file = open('C:/Users/20RHoh.ACC/Desktop/coding stuff/courses.csv', 'r')
count = 0
for line in file:
    line = line[:-1]
    fields =line.split(',')
    if fields[0] == 'CS':
        print(fields[0],fields[1])
        count += 1
file.close()

wasd = open('C:/Users/20RHoh.ACC/Desktop/coding stuff/remainder.txt', 'r')
for line in wasd:
    if line == "\n":
        pass
    else:
        print(line)
'''
twitter = open('C:/Users/20RHoh.ACC/Desktop/coding stuff/results.txt', 'r')
ulc = 0
dcuc = 0
tcdc = 0
for line in twitter:
    line = line[:-1]
    fields = line.split(',')
    if fields[1] == 'UL':
        ulc +=1
    elif fields[1] == 'DCU':
        dcuc += 1
    elif fields[1] == 'TCD':
        tcdc += 1
print (ulc, dcuc, tcdc)
teitter.close()