import random
'''
Q1
e = random.randint(1, 100)
print(e)

Q2
choice = random.choice(["apple", "banana", "orange", "pineaple", "kiwi"])
print(choice)

Q3
user = input("guess the result of the coinflip\n")
user.lower()
act = random.choice(["heads", "tails"])
if user == act:
    print("You win")
else:
    print("Bad luck")

Q4
rng = random.randint(1, 5)
for i in (1, 2):
    user = int(input("Insert number between 1 and 5\n"))
    if user == rng:
        break
    elif user > rng:
        print("too high")
    elif user < rng:
        print("Too low")
if i == 1:
    print("well done")
elif user == rng:
    print("correct")
else:
    print("You lose")

Q5 + 6
ges = random.randint(1 ,10)
while True:
    ug = int(input("Guess a number between 1 and 10\n"))
    if ug == ges:
        break
    elif ug > ges:
        print("too high")
    elif ug < ges:
        print("too low")
print("You 'win'")

Q7
score = 0
for i in range(5):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    uans = int(input(f"What is {a} + {b}?\n"))
    ans = a+b
    if uans == ans:
        score = score+1
print(f"You got {score} ammount of quetions out of 5")

Q8
colours = ["red", "orange", "yellow", "green", "blue"]
sytcol= random.choice(colours)
order = colours.index(sytcol)+1
print(colours)
while True:
    uc = input("Choose a colour from the list\n")
    uc.lower()
    if uc == sytcol:
        print("Well done")
        break
    else:
        print(f"The colour you're looking for is the {order} one on the rainbow")
'''