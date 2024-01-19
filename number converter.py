ui = input("insert a number here")
ulil = []
hfgdf = []
ertfgujhik = []
num1 = 0
num2 = 0
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
        for i in range(len(ulil)):
            num1 += ulil[-i-1]*(2**(i))
        for i in range(len(hfgdf)):
            num2 += hfgdf[-i-1]*(2**(i))
        total = num1 + num2
        while total>0:
            rem = total % 2
            ertfgujhik.append(rem)
            total = total//2
        ertfgujhik = list(map(str, ertfgujhik))
        print(''.join(ertfgujhik[::-1]))
    else:
        print("this is not a valid function")