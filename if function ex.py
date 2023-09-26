'''
Q1
a, b = input("Insert two numbers here\n").split()
a=int(a)
b=int(b)
if a>b:
    print(b, a)
else:
    print(a, b)

Q2
N= int(input("insert a number that is under 20\n"))
if N>20:
    print("too high")
elif N<0 or N==0:
    print("What are you trying here")
else:
    print("Thank you")

Q3
N= int(input("insert a number between 10 and 20\n"))
if 10<=N<=20:
    print("thank you")
else:
    print("incorrect answer")

Q4
c = input("What is your favourite colour?\n")
if c== "red" or "Red" or "RED":
    print("I like red too")
else:
    print("I don't like", c, "I prefer red")

Q5
w= input("Is it raining?\n")
w.lower()
if w=="yes":
    ay= input("is it windy?\n")
    ay.lower()
    if ay=="yes":
        print("It's too windy for an unbrella")
    elif ay=="no":
        print("Take an unbrella")
    else:
        print("I was asking a yes or no question")
elif w=="no":
    print("Enjoy your day")
else:
    print("I was asking a yes or no question")

Q6
ua = int(input("how old are you?\n"))
if ua>=18:
    print("You can vote")
elif ua==17:
    print("You can learn to drive")
elif ua==16:
    print("You can buy a lottery ticket")
elif 0<ua<16:
    print("You can trick or treat")
elif ua==0:
    print("I doubt you were born today")
else:
    print("you can't be a negative age")

Q7
n = int(input("enter a number\n"))
if n<10:
    print("Too low")
elif 10<=n<=20:
    print("Correct")
else:
    print("Too high")

Q8
n = int(input("Input 1 2 or 3\n"))
if n==1:
    print("Thank you")
elif n==2:
    print("Well done")
elif n==3:
    print("Correct")
else:
    print("Error message: uhh no")
'''