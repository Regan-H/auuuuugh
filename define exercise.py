import random
'''
Q1
def count():
     num = int(input("Enter a number here\n"))
     s = 0
     while s <= num:
         print(s, end=" ")
         s=s+1
count()

Q2
def rng():
    high, low = input("Insert a high and a low number here\n").split()
    high = int(high)
    low=int(low)
    return random.randint(low, high)
comp_num = rng()
def cg():
    return int(input("Im thinking of a number try and guess it\n"))
ug = cg()
def gamble(comp_num, ug):
    while True:
        if comp_num == ug:
            print("You win")
            break
        else:
            print("Try again")
            cg()
            ug=cg()
gamble(comp_num, ug

Q3
def check(ua, ca):
    if ua != ca:
        print(f"incorrect tha answer was {ca}")
    else:
        print("Correct")
def Addition():
    a = random.randint(5,20)
    b = random.randint(5,20)
    ua = int(input(f"What is {a} + {b}?\n"))
    ca = a + b
    check(ua, ca)
def Subtraction():
    a = random.randint(25, 50)
    b = random.randint(1, 25)
    ua = int(input(f"What is {a} - {b}?\n"))
    ca = a - b
    check(ua, ca)
while True:
    uc = int(input(" 1) Addition\n 2)Subtraction\n Enter 1 or 2:"))
    if uc == 1:
        Addition()
        break
    elif uc ==2:
        Subtraction()
        break
    else:
        print("No")
'''
names = []
def listadd(names):
    new = input("Who would you like to add?\n")
    return names.append(new)
def listchange(names):
    sel = input("Who would you like to replace?\n")
    bad = names.index(sel)
    bad = int(bad)
    new = input(f"Who would you like to replace {sel} with?\n")
    names.remove(sel)
    return names.insert(bad, new)
def listremove(names):
    sel = input("Who would you like to remove?\n")
    return names.remove(sel)
def listshow(names):
    print(names)
def menu():
    usel = int(input("What would you like to do?\n 1)Add a name to the list\n 2)Remove a nme from the list\n 3)Change a name on the list\n 4)View the list\n 5)End program\n"))
    if usel == 1:
        listadd(names)
    elif usel == 2:
        listremove(names)
    elif usel == 3:
        listchange(names)
    elif usel == 4:
        listshow(names)
    elif usel == 5:
        print("Thanks for using this program, heres the final list")
        listshow(names)
        exit()
    else:
        print("No")
while True:
    menu()
    