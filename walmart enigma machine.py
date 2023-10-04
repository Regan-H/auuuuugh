alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
codexabet = ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c"]
messager = []
messaget=[]
while True:
    um = input("Insert message here\n")
    um.lower()
    messager.extend(um)
    re = input("Would you like to add another word?[Y/N]\n")
    if re == "n":
        break
d = input("Would you like eo encode this message or decode this message?\n")
d.lower()
if d == "encode":
    jerry = len(messager)
    loop = 0
    for i in [1]*jerry:
        test = alphabet.index(messager[loop])
        temp = codexabet[test]
        messaget.append(temp)
        loop+=1
    messaget = str(messaget)
    messaget=messaget.replace(',','')
    messaget=messaget.replace("'","")
    messaget=messaget.replace(' ','')
else:
    jerry = len(messager)
    loop = 0
    for i in [1]*jerry:
        test = codexabet.index(messager[loop])
        temp = alphabet[test]
        messaget.append(temp)
        loop+=1
    messaget = str(messaget)
    messaget=messaget.replace(',','')
    messaget=messaget.replace("'","")
    messaget=messaget.replace(' ','')
print(messaget)
