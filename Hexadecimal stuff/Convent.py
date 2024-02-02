total = 0
import Hexconverter
import listmaker
Choice = int(input("""What would you like to do?
1. Hexdecimal to decimal
2. Decimal to hexadecimal
3. Hexadecimal to binary
4. Binary to hexadecimal

"""))
if Choice == 1:
    total = Hexconverter.HexToDec(total)
    print(total)
elif Choice == 2:
    total = Hexconverter.DecToHex(total)
    print(''.join(total[::-1]))
elif Choice == 3:
    total = Hexconverter.HexToBin(total)
    print(total[::-1])
elif Choice == 4:
    total = Hexconverter.BinToHex(total)
    print(''.join(total))