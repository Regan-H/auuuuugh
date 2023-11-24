want = input("Insert file that you want to count in")
weez = open(f"C:/Users/20RHoh.ACC/Desktop/example scripts/{want}", "r")
top = 0
bottom = 0
for line in weez:
    line = line.strip()
    if line == "":
        pass
    else:
        check = line.isdigit()
        line = int(line)
        if check == True:
            top+=line
            bottom+=1
        else:
            pass
mean = top/bottom
print(mean)