class Trijsturis:
    def __init__(self, nosaukums,malas):
        self.nosaukums = nosaukums
        self.malas = malas
    def drukaNosaukumu(self):
        print ("Figuras nosaukums "+f"{self.nosaukums}")   
    def drukatMaluSkaitu(self):
        print ("Malu skaits "+f"{self.malas}")

class Tainsturis:
    def __init__(self, nosaukums,malas):
        self.nosaukums = nosaukums
        self.malas = malas    
    def drukaNosaukumu(self):
        print ("Figuras nosaukums "+f"{self.nosaukums}")
    def drukatMaluSkaitu(self):
        print ("Malu skaits "+f"{self.malas}")

class Kvadrats:
    def __init__(self, nosaukums,malas):
        self.nosaukums = nosaukums
        self.malas = malas    
    def drukaNosaukumu(self):
        print ("Figuras nosaukums "+f"{self.nosaukums}")   
    def drukatMaluSkaitu(self):
        print ("Malu skaits "+f"{self.malas}")


tr1 = Trijsturis("Trijstūris",3)
tr2 = Tainsturis("Tainstūris",4)
tr3 = Kvadrats("Kvadrāts",4)
   
visi = [tr1, tr2, tr3]
for x in visi:
    
    x.drukaNosaukumu()
    x.drukatMaluSkaitu()
