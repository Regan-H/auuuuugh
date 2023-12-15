'''
Q1
e = list(input("insert something here\n"))
print(e[::2])

Q2
e = list(input("insert something here\n"))
wad = []
for i in range(len(e)+1):
    if i == 0:
        pass
    else:
        wad.append(e[-i])
print(wad)

Q3

e = []
while True:
    lol = (input('insert a list element\n'))
    if lol.isdigit() == True:
        lol = int(lol)
        e.append(lol)
    c = input("Would you like to continue [Y/N]\n")
    c.lower()
    if c == "n":
        break
    elif c == "y":
        pass
    else:
        print("no")
temp = 1
for i in e:
    if i > temp:
        temp = i
print(temp)

Q4
e = list(input("Insert something here\n"))
a = []
for i in e:
    a = e[0]
    e.remove(e[0])
    e.append(a)
    print(''.join(e))

Q5
oge = input("Insert something here\n").split()
e = oge.copy()
uc = int(input("Which word do you want to remove?"))
uc -=1
long = 0
for i in e:
    long += len(i)
word_l = len(e[uc])
e.remove(e[uc])
wasd = len(e)
print(f"{''.join(e)}, your orginal input {''.join(oge)} was {long} characters long. The word you wanted to remove was {word_l} characcters long")

Q6
ym = [
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August,'
'September',
'October',
'November',
'December',]
m, d, y = input("insert the date here").split("/")
m = int(m)
m -=1
d = int(d)
y = int(y)
mon = ym[m]
print(f"{mon} {d},{y}")

Q7
numb = list(input("insert a 10 digit number here"))
print(numb[::2])
'''