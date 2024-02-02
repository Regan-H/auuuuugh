def create(x, y):
    for i in x:
        y.append(i)
    return y
def listint(x):
    for i in x:
        x = list(map(int, x))
    return x
def liststr(x):
    for i in x:
        x = list(map(str, x))
    return x
def Hexgrouper(x, y):
    temptotal = ''
    temptotal += x[:4]
    x = x[4:]
    y.append(temptotal)
    return x, y
def DecToHexRaw(x, y):
    ulil = []
    Hexletters = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    while x>0:
        rem = x % 16
        ulil.append(rem)
        x = x//16
    for i in ulil:
        if i > 9:
            letter = Hexletters[i]
            tempindex = ulil.index(i)
            ulil.remove(ulil[ulil.index(i)])
            ulil.insert(tempindex, letter)
        else:
            continue
    ulil = liststr(ulil)
    y = ulil
    return x, y