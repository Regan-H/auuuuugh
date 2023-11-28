import math
'''
Q1
user = input("Enter your name:\t")
print(f"Hello {user}")

Q2
n1, n2 = input("Insert 2 numbers here").split()
n1 = int(n1)
n2 = int(n2)
ans = n1+n2
print(ans)

Q3
realtemp= int(input("Insert a temperature in celsius"))
americatemp = ((9/5)*realtemp)+32
print(americatemp)

Q4
pri, rate, time = input("Insert priciple, rate and time\n").split()
pri = int(pri)
rate = int(rate)
time= int(time)
simpint = (pri*rate*time)/100
print(simpint)

Q5
secim = int(input("Insert time in seconds:\n"))
hours = secim//3600
secim = secim-(hours*3600)
mins = secim//60
sec = secim-(mins*60)
print(hours, mins, sec)

Q6
x, y = input("insert 2 numbers\n").split()
print(x, y, "before swap")
z = y
y =x
x = z
print(x, y, "after swap")

Q7
x, y = input("insert 2 numbers\n").split()
print(x, y, "before swap")
x, y = y, x
print(x, y, "after swap")

Q8
r = int(input("Insert radius of circle"))
area = math.pi*(r*r)
circ = 2*(math.pi*r)
print(area, circ)

Q9
l, w = input("Insert length and width of rectangle here\n").split()
l = int(l)
w = int(w)
area = l*w
perm = 2*(l+w)
print(area, perm)

Q10
a, b, c = input("Insert the 3 sides of a triangle").split()
a = int(a)
b = int(b)
c = int(c)
s = (a+b+c)/2
temp = s*((s-a)*(s-b)*(s-c))
area = math.sqrt(temp)
print(area)

Q11
pri, rate, time = input("Insert priciple, rate and time\n").split()
pri = int(pri)
rate = int(rate)
time= int(time)
comp = pri*((1+(rate/100)**time)) - pri
print(comp)
'''