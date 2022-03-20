class Viesis:
    def __init__(self, vards, parole):
        self.vards = vards
        self.parole = parole

    def drukaVardu(self):
        print ("Viesis "+f"{self.vards}"+" izveidots")

    def drukaParoli(self):
        print ("Lietotajs "+f"{self.parole}"+" parole izveidota")
#Mantosana - Наследование
class Darbinieks(Viesis):
    def drukaVardu(self):
        print ("Darbinieks "+f"{self.vards}"+" izveidots")

vards = "Valdis"
parole = "$$$$$$"

viesis1 = Viesis(vards, parole)
viesis1.drukaVardu()
viesis1.drukaParoli()

vards = "Daina"
parole = "DDDDDDD"

darbinieks1 = Darbinieks(vards, parole)
darbinieks1.drukaVardu()
darbinieks1.drukaParoli()

print(isinstance(darbinieks1,Viesis))
print(isinstance(darbinieks1,Darbinieks))
print(isinstance(viesis1,Viesis))
print(isinstance(viesis1,Darbinieks))

#Polimorfizm

visi = [viesis1, darbinieks1]
for x in visi:
    x.drukaVardu()
    x.drukaParoli()
