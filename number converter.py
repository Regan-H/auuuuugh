ui = input("insert a number here")
ulil = []
hfgdf = []
ertfgujhik = []
b = 1
choice = input("What would you like to do? Add binary, or convert between them")
choice.lower()
dec = ["2", "3", "4", "5", "6", "7", "8", "9"]
total = 0
kind = ''
for i in ui:
    if i in dec:
        kind = "decimal"
else:
    if kind == 'decimal':
        pass
    else:
        kind = "binary"
        for i in ui:
            ulil.append(i)
        ulil = list(map(int, ulil))
if kind == choice:
    print(f"it's already a {choice}")
else:
    if choice == "decimal":
        for i in range(len(ulil)):
            total += ulil[-i-1]*(2**(i))
        print(total)
    elif choice == 'binary':
        ui = int(ui)
        while ui>0:
            rem = ui % 2
            ulil.append(rem)
            ui = ui//2
        print(ulil[::-1])
    elif choice == 'add':
        ko = input("Insert 2nd binary here")
        for e in ko:
            hfgdf.append(e)
        hfgdf = list(map(int, hfgdf))
        hjkl = max(len(hfgdf), len(ulil))
        for i in range(hjkl+1):
            if b+1 > len(ulil):
                ulil.insert(0, 0)
            if b+1 > len(hfgdf):
                hfgdf.insert(0, 0)
            sa = hfgdf[-b]+ulil[-b]
            if sa == 1:
                ertfgujhik.append('1')
            elif sa > 1:
                ertfgujhik.append('0')
                ulil[-b-1] += 1
            else:
                ertfgujhik.append('0')
            b += 1 
        print(''.join(ertfgujhik))             
    else:
        print("this is not a valid function")