intake = "dil"
def listadd(intake):
    lon = len(intake)
    total = 0
    for i in range(lon):
        total = total + intake[i]
    print(total)
def listmulti(intake):
    lon = len(intake)
    total = 1
    for i in range(lon):
        total = total*intake[i]
    print(total)
def invertstring(intake):
    lon = len(intake)
    d = -1
    out = ""
    for i in range(lon):
        out = out + intake[d]
        d = d -1
    print(out)
def factorio(x):
    total = 1
    y = x
    for i in range(y):
        total = total*x
        x = x-1
    print(total)
def checkran(x, y ,z):
    ranger = []
    for i in range(z):
        ranger.append(y)
        y = y+1
    if x in ranger:
        print("True")
    else:
        print("False")
def casecount(quin):
    bob = len(quin)
    up = 0
    low = 0
    for i in range(bob):
        d = quin[i].isupper()
        if d == True:
            up = up+1
        else:
            low = low+1
    print(f" no. of upper characters = {up}\n no. of lower characters = {low}")
def dlist(intake):
    v1 = len(intake)
    out= []
    for i in range(v1):
        if intake[i] == intake[i-1]:
            pass
        else:
            out.append(intake[i])
    print(out)
def primec(x):
    c = 1
    co = 0
    for i in range(x):
        d = x%c
        c = c+1
        if d == 0: 
            co = co+1
        else:
            pass
    if co == 2:
        print("True")
    else:
        print("False")
def evencheck(pain):
    v1 = len(pain)
    out =[]
    for i in range(v1):
        d = pain[i]%2
        if d == 0:
            out.append(pain[i])
        else:
            pass
    print(out)