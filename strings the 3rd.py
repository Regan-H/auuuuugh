'''
Q1
first, last = input('enetr your full name').split()
print(len(first))
print(len(last))
print(f'your full name is : {first} {last}')

Q2
fn = []
fn.extend(input("Insert your favourite subject here"))
fn=str(fn)
fn=fn.replace(',','')
fn=fn.replace("'","")
fn=fn.replace(' ','-')
fn=fn.replace('[','')
fn=fn.replace(']','')
print(fn)

Q3
poem = "The clean bones crying in the flesh."
print(poem)
s, t = input("Insert a starting and ending position\n").split()
s = int(s)
t = int(t)
s-=1
t-=1
print(poem[s:t])

Q4
while True:
    usi = input("Insert a statement in uppercase")
    c = usi.isupper()
    if c == True:
        break
    else:
        print("Try again")

Q5
up = input("please put your postcode here, i swear this isn't sketchy")
up = up[0:2].upper()
print(up)

Q6
un = input("Insert your first name\n")
un = un.lower()
a = un.count('a')
e = un.count('e')
i = un.count('i')
o = un.count('o')
u = un.count('u')
vc = a+e+i+o+u
print(vc)

Q7
pas = input("Insert new password here\n")
while True:
    pasc = input("insert new password again\n")
    c = pas.isupper()
    h = pasc.isupper()
    if pas == pasc:
        print("Thank you")
        break
    elif c != h:
        print("they must be in the same case")
    else:
        print("Incorrect")

Q8
um = input("Insert message here")
e = len(um)
for i in range(e):
    if i == 0:
        pass
    else:
        i = i*-1
        print(um[i])
print(um[0])
'''