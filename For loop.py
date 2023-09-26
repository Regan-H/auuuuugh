'''
Q1 & Q2
u = input("Enter your name\n")
n = int(input("enter a number\n"))
for i in [1]*n:
    print(u)

Q3 & Q4
un= input("insert name here")
auu = int(input("insert number here"))
bruh= len(un)
bruh=int(bruh)
e=0
for i in [1]*auu:
    for f in [1]*bruh:
        print(un[e])
        e=e+1
    e=0

Q5
ui= int(input("Insert number between 1 and 12 here\n"))
pain = 1
for i in range(12):
    urk=ui*pain
    print(urk)
    pain=pain+1

Q6
uc = int(input('enter a number under 50'))
c = 51-uc
ack=51
for i in [1]*c:
    d=ack-1
    print(d)
    ack=ack-1

Q7
un, rn = input("input your name and a number\n").split()
rn=int(rn)
if rn<10:
    for i in [1]*rn:
        print(un)
else:
    print("too high")

Q8
total = 0
for i in range(5):
    ui= int(input("Insert a number here\n"))
    ans= input("Would you like to add this to the total? [Y/N]\n")
    ans.lower()
    if ans=="y":
        total=total+ui
print(total)

Q9
dir= input("Which direction would you like to count (up or down)\n")
dir.lower()
if dir=="up":
    top= int(input("where would you like to count to?\n"))
    a=1
    for i in [1]*top:
        print(a)
        a=a+1
elif dir=="down":
    ver= int(input("What number would you like to count down towards?\n"))
    diff=21-ver
    a=20
    for i in [1]*diff:
        print(a)
        a=a-1
else:
    print("Bro what did you type?")

Q10
uque = int(input('How many guests would you like to invite?\n'))
if uque<10:
    for i in [1]*uque:
        name= input("Insert name of someone you want to invite\n")
        print(name, "has been invited")
else:
    print("Too many people")
'''