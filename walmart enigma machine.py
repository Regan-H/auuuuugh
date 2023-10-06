alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
messager = []
messaget=[]
key = int(input("What would you like your key to be?\n"))
if key > 25:
    print("no")
else:
    um = input("Insert message here\n")
    um.lower()
    messager.extend(um)
    d = input("Would you like eo encode this message or decode this message?\n")
    d.lower()
    if d == "encode":
        jerry = len(messager)
        loop = 0
        for i in [1]*jerry:
            test = alphabet.index(messager[loop])
            temp = alphabet[test+key]
            messaget.append(temp)
            loop+=1
        messaget=str(messaget)
        messaget=messaget.replace(',','')
        messaget=messaget.replace("'","")
        messaget=messaget.replace(' ','')
    elif d == "decode":
        jerry = len(messager)
        loop = 0
        for i in [1]*jerry:
            test = alphabet.index(messager[loop])
            temp = alphabet[test-key]
            messaget.append(temp)
            loop+=1
        messaget=str(messaget)
        messaget=messaget.replace(',','')
        messaget=messaget.replace("'","")
    else:
        print("Bruh")
    print(messaget)