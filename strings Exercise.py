'''
user = input("enter your first name\n")
long = len(user)
print(" this is the length of your name", long)

userf, users = input("Enter your first and surname\n").split()
full = userf+users
lange=len(full)
reallange=lange
print("Your full name is", reallange, "characters long")

userf, users = input("Enter your first and surname in lowercase\n").split()
uno=userf[0].upper()
dos=users[0].upper()
print(uno+userf[1:], dos+users[1:])

ickle = input("insert first line of nursery rhyme here\n")
DesireS, DesireE = input("Put in the wanted section of characters\n").split()
DesireS=int(DesireS)
DesireE=int(DesireE)
DesireS=DesireS-1
DesireE=DesireE-1
print(ickle[DesireS:DesireE])

word = input("Enter any word\n")
word=word.upper()
print(word)

UserF = input("Insert first name here\n")
chonk=len(UserF)
if chonk<5:
    UserS = input("Insert surname here\n")
    full=UserF+UserS
    full=full.upper()
    print(full)
else:
    UserF=UserF.lower()
    print(UserF)
'''
Latint = input("Insert any English word\n").lower()
if Latint[0]=='a':
    ED="way"
    LatinP=Latint+ED
    print(LatinP)
else:
    if Latint[0]=='e':
        ED="way"
        LatinP=Latint+ED
        print(LatinP)
    else:
        if Latint[0]=='i':
            ED="way"
            LatinP=Latint+ED
            print(LatinP)
        else:
            if Latint[0]=='o':
                ED="way"
                LatinP=Latint+ED
                print(LatinP)
            else:
                if Latint[0]=='u':
                    ED="way"
                    LatinP=Latint+ED
                    print(LatinP)
                else:
                    ED=Latint[0]+"ay"
                    print(Latint[1:]+ED)
    