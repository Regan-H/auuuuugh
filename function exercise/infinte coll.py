import collatz
x = int(input("Insert number here"))
while x !=1:
    x = collatz.collatz(x)
    print(x)