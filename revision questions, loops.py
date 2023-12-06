'''
Q1
for i in range(11):
    print(i)

Q2
x = 0
while x<21:
    print(x)
    x+=1

Q3
for i in range(11):
    

Q4
n = int(input("Insert a number here\n"))
for i in range(n):
    print(i+1)

Q5
n = int(input("Insert a number here\n"))
for i in range(n):
    if i%2 == 1:
        print(i)

Q6
for i in range(5):
    print("Happy Birthday!")

Q7
n = int(input("Insert a number here\n"))
for i in range(n+1):
    print(i**2)

Q8
n = int(input("Insert a number here\n"))
for i in range(n+1):
    a = n*i
    print(n, "x", i, "=", a)

Q9
n = 3
for i in range(8):
    n +=4
    print(n)

Q10
n = 2
for i in range(6):
    n *=3
    print(n)

Q11
n = int(input("Insert a number here\n"))
a = 0
for i in range(n):
    a +=i
    print(a)

Q12
a = 0
n = int(input("Insert a number here\n"))
for i in range(n+1):
    if i == 0:
        pass
    else:
        a += 1/i
        print(a)

Q13
ans = 0
for i in range(5):
    n = int(input("Insert a number here\n"))
    ans+=n
print(ans)

Q14
a = 1
n = int(input("Insert a number here\n"))
for i in range(n+1):
    if i == 0:
        pass
    else:
        a*=i
    print(a)

Q15
b = int(input("Insert a base here\n"))
ex = int(input("Insert a n exponent here\n"))
ans = 0
temp = b
for i in range(ex-1):
    temp = temp*b
    ans = temp
print(ans)

Q16
de = 0
tot = 0
c = 0
for i in range(5):
    c +=1
    de +=1
    n = int(input(f"Enter number{c}: "))
    while n <= 0:
        print("This is an invalid value. All numbers must be positive.")
        n = int(input(f"Enter number{c}: "))
    tot += n
mean = tot/de
print(f"The sum of the 5 numbers entered is {tot}.\nThe average of the 5 numbers entered is {mean}.")
'''
