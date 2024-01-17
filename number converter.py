ui = input("insert a number here")
ulil = []
choice = input("What would you like to convert it to?")
choice.lower()
dec = ["2", "3", "4", "5", "6", "7", "8", "9"]
total = 0
if ui in dec:
    kind = "decimal"
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
    else:
        ui = int(ui)
        while ui>0:
            ulil.append(ui%2)
            ui -= (ui//2)*2
        print(''.join(ulil))