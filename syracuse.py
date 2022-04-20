class Syracuse:

    def __init__(self,nb,file):
        self.nbr = nb
        self.f = file

    def SyrCalc(self):
        while (self.nbr != 1) and (self.nbr > 1):
            self.f.write(str(self.nbr)+' ')
            if(self.nbr%2 == 0):
                self.nbr //=2
            else:
                self.nbr = (self.nbr*3)+1



f = open('SyrOutput.txt', 'w')

a = int(input("a = "))

syra = Syracuse(a,f)
syra.SyrCalc()
f.close()