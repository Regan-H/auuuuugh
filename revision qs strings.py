'''
Q1
e = input("put something here")
e.lower()
count = 0
long = len(e)
for i in range(long):
    c = e[i]
    if "a"in c:
        count +=1
    if "e"in c:
        count +=1
    if "i"in c:
        count +=1
    if "o"in c:
        count +=1
    if "u"in c:
        count +=1
    else:
        pass
print(f"You have {count} vowels in your word")

Q2
e = input("put something here\n")
lower = 0
upper = 0
digits = 0
white = 0
for i in e:
    v = i.isupper()
    h = i.islower()
    k = i.isdigit()
    if v == True:
        upper+=1
    elif h == True:
        lower+=1
    elif k == True:
        digits+=1
    else:
        white+=1
print(f"uppercase letters={upper}\nlowercase letters={lower}\nno of digits={digits}\nwhitespace={white}")

Q3
e = input("put something here\n")
e = list(e)
first = e[0]
last = e[-1]
e.remove(first)
e.remove(last)
e.insert(0, last)
e.append(first)
print("".join(e))

Q4
e = input("put something here\n")
a = ''
long = len(e)
for i in range(long+1):
    if i == 0:
        pass
    else:
        a += e[-i]
print(a)

Q5
e = input("put something here\n")
e = list(e)
first = e[0]
e.remove(first)
e.append(first)
print(''.join(e))

Q6
e = input("put something here\n")
init = ''
for i in e:
    c = i.isupper()
    if c == True:
        init +=i
print(init)

Q7
e = input("put something here\n")
forw = []
backw = []
long = len(e)
long = long/2
long = int(long)
for i in range(long*1):
    forw.append(e[i])
    c = -i -1
    backw.append(e[c])
if forw == backw:
    print("It is a palindrome")
else:
    print("try again")
    
Q8
e = input("put something here\n")
long = len(e)
for i in range(long):
    e = (e[1:long] +e[0])
    print(e)

Q9
e = input("put something here\n")
long = len(e)
if long >=8:
    init = 0
    for i in e:
        c = i.isupper()
        if c == True:
            init +=1
    if init >= 1:
        init = 0
        for i in e:
            c = i.isdigit()
            if c == True:
                init +=1
        if init >= 1:
            print("password accepted")
        else:
            print("NO.")
    else:
        print("NO.")
else:
    print("NO.")
'''