'''
Q1
total = 0
while total <50 :
    a = int(input("Insert number here\n"))
    total=total+a
print(f"The total is {total}")

Q2
while True:
    g = int(input("Enter a number\n"))
    if g > 5:
        break
print(f"The last number you entered was a {g}")

Q3
a, b = input("Insert 2 numbers here\n").split()
a = int(a)
b = int(b)
ans =a+b
d = input("Would you like to add another?[Y/N]\n")
d.lower()
if d == "y":
    while d == "y":
        c = int(input("Insert new number here\n"))
        ans = ans+c
        d = input("Would you like to add another?[Y/N]\n")
        d.lower()
print(ans)

Q4
gl= []
while True:
    gn = input("Insert name of someone you want invited to party\n")
    gl.append(gn)
    print(f"{gn} has been invited to the party")
    d = input("Would you like to invite someone else?\n")
    d.lower()
    if d == "n":
        break
print(gl)

Q5
compnum=50
attempts = 0
while True:
    g = int(input("Insert guess here\n"))
    attempts=attempts+1
    if g > 50:
        print("Too high")
    elif g < 50:
        print("Too low")
    else:
        break
print(f"Well done you took {attempts} attempts")

Q6
while True:
    ug = int(input("Insert number betwwen 10 and 20\n"))
    if ug > 20:
        print("too high")
    elif ug < 10:
        print("Too low")
    else:
        break
print("Thank you")

Q7
degroot = 100
while degroot > 0:
    print(f"There are {degroot} green bottles hanging on the wall, {degroot} green bottles on the wall, and if 1 green bottle were to fall")
    degroot = degroot - 1
    while True:
        ua = int(input("how many green bottles are hanging on the wall?\n"))
        if ua == degroot:
            print(f"There will be {degroot} green bottles hanging on the wall")
            break
        else:
            print("try again")
print("There are no more green bottles left on the wall")
'''