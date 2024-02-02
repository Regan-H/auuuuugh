import listmaker
def HexToDec(x):
    ulil = []
    x = 0
    Total = 0
    Hexletters = {
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15
    }
    UserIn = input("Insert hexadecimal number here\n")
    UserIn = UserIn.upper()
    ulil = listmaker.create(UserIn, ulil)
    for i in ulil:
        if i.isalpha():
            Total += Hexletters[i]
            Total = str(Total)
            tempindex = ulil.index(i)
            ulil.remove(ulil[ulil.index(i)])
            ulil.insert(tempindex, Total)
            Total = 0
        else:
            continue
    ulil = listmaker.listint(ulil)
    for i in range(len(ulil)):
        x += ulil[-i-1]*(16**(i))
    return x
def DecToHex(x):
    UserIn = int(input("Insert decimal number here\n"))
    ulil = []
    Hexletters = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    while UserIn>0:
        rem = UserIn % 16
        ulil.append(rem)
        UserIn = UserIn//16
    for i in ulil:
        if i > 9:
            letter = Hexletters[i]
            tempindex = ulil.index(i)
            ulil.remove(ulil[ulil.index(i)])
            ulil.insert(tempindex, letter)
        else:
            continue
    ulil = listmaker.liststr(ulil)
    x = ulil
    return x
def BinToHex(x):
    UserIn = input("Insert binary number here\n")
    subtotal = 0
    x = []
    Ttotal = []
    ulil = []
    while UserIn != '':
        if len(UserIn) < 4:
            UserIn = '0' + UserIn
        else:
            UserIn, ulil = listmaker.Hexgrouper(UserIn, ulil)
    for i in ulil:
        Sublist = i
        for i in range(len(Sublist)):
            Sublist = listmaker.listint(Sublist)
            subtotal += Sublist[-i-1]*(2**(i))
        subtotal, Ttotal = listmaker.DecToHexRaw(subtotal, Ttotal)
        Ttotal = str(Ttotal)
        x.append(Ttotal)
    return x
def HexToBin(x):
    TempDec =  0
    x = []
    TempDec = HexToDec(TempDec)
    TempDec = int(TempDec)
    while TempDec>0:
        rem = TempDec % 2
        x.append(rem)
        TempDec = TempDec//2
    return x

