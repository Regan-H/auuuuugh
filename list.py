'''
Q1
Athlete = ["soccer", "rugby"]
userA = input("what is your faourite sport?\n")
Athlete.append(userA)
print(Athlete)

Q2
pain = ["Engineering", "Physics", "biology", "English", "irish", "chinese"]
print(pain)
dis = input("Which of these subjects do you not like? (pick one)\n")
pain.remove(dis)
print("here's your list of subjects", pain)

Q3
user1,user2,user3,user4,user5,user6,user7,user8,user9,user10 = input("Insert 10 colours here\n").split()
CL = [user1,user2,user3,user4,user5,user6,user7,user8,user9,user10]
sta = int(input("enter starting number between 1 and 4\n"))
ED = int(input("enter end number between 5 and 9\n"))
if 1<=sta<=4 and 5<=ED<=9:
    print(CL[sta:ED])
else:
    print("bruh try again")

Q4
Pass = [234, 123, 546, 461]
print(Pass[0], "\n", Pass[1], "\n", Pass[2], "\n", Pass[3])
userI = int(input("insert a 3 digit number\n"))
if userI in Pass:
    pain=Pass.index(userI)
    pain=pain+1
    print(pain)
else:
    print("That isn't in the list")

Q5
n1, n2, n3 = input("Insert 3 names of people you want to invite to the party\n").split()
gu=[n1,n2,n3]
ex= input("Would you like to addmore?\n")
ex.lower()
if ex=="yes":
    while ex=="yes":
        nN = input("Insert the name here\n")
        gu.append(nN)
        ex= input("Would you like to addmore?\n")
        ex.lower()
        if ex=="no":
            break
print(gu)
sad = input("insert a name on the list\n")
block = input("Would you like to revoke their invite? [Yes/No]\n")
block.lower()
if block=="yes":
    rem=gu.index(sad)
    rem=int(rem)
    del gu[rem]
print(gu)

Q6
quality=["Star wars the clone wars", "Bob the builder", "dora the explora", "thomas the tank engine"]
print(quality[0], "\n", quality[1], "\n",quality[2], "\n",quality[3])
mor, pos = input("insert anther show and what order you want it on the list\n").split()
pos=int(pos)
pos=pos1
quality.insert(pos, mor)
print(quality)

Q7
numbs=[]
for i in range(3):
    n= int(input("Insert a number to the list\n"))
    numbs.append(n)
rem= input("Would you like to save the last number?\n")
if rem=="no":
    del numbs[-1]
print(numbs)
'''