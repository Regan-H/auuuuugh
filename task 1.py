import gates
import listmaker

logi = gates.Logic()   
'''
ui = list(input("What values would you like?\n"))
ui = listmaker.listint(ui)
'''
ui = input("What gate would you like?\n1. and\n2. or\n3. not\n4. xor\n5. nand\n6. nor\n7. nxor\n")
ui = ui.lower()
gate = logi.Choice[int(ui)]
print(logi.TRUTH(gate))
