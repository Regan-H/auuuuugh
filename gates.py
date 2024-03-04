import listmaker
class Logic:
    def AND(self,x,y):
        if x == 1 and y == 1:
            return 1
        else:
            return 0
    def OR(self,x,y):
        if x == 1 or y ==1:
           return 1
        else:
            return 0
    def NOT(self,x):
        if x ==1:
            return 0
        else:
            return 1
    def XOR(self,x, y):
        if (x == 1 and y == 0) or (x == 0 and y == 1):
           return 1
        else:
            return 0
    def NAND(self,x,y):
        return NOT(AND(x,y))
    def NOR(self,x,y):
        return NOT(OR(x,y))
    def NXOR(self,x,y):
        return NOT(XOR(x,y))
    Choice = {
        1 : 'AND',
        2 : 'OR',
        3 : 'NOT',
        4 : 'XOR',
        5 : 'NAND',
        6 : 'NOR',
        7 : 'XNOR',
        }
    def TRUTH(self, gate : str):
        x = 0
        y = 0
        for i in range(4):
            match (gate):
                case 'AND':
                    ans = Logic.AND(self,x,y)
                case 'OR':
                    ans = Logic.OR(self,x,y)
                case 'NOT':
                    print(f"0¦ {Logic.NOT(self,0)}")
                    print(f"1¦ {Logic.NOT(self,1)}")
                    break
                case 'XOR':
                    ans = Logic.XOR(self,x,y)
                case 'NAND':
                    ans = Logic.NAND(self,x,y)
                case 'NOR':
                    ans = Logic.NOR(self,x,y)
                case 'XNOR':
                    ans = Logic.XNOR(self,x,y)
            print(f"{x} ¦ {y} ¦ {ans}")
            if i == 0 or i == 2:
                x+=1
            elif i == 1:
                x,y = y,x
            
            
        