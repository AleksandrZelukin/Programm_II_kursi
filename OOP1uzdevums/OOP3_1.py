class Figura:
    def __init__(self, malas, nosaukums):
        self.malas = malas
        self.nosaukums = nosaukums

    def drukatMaluSkaitu(self):
        print ("Malu skaits "+f"{self.malas}")

    def drukaNosaukumu(self):
        print ("Figuras nosaukums "+f"{self.nosaukums}")



   
trijsturis1 = Figura(3, "Trijstūris")
tainsturis1 = Figura(4, "Tainstūris")
kvadrats1 = Figura(4,"Kvadrāts")

visi = [trijsturis1, tainsturis1, kvadrats1]
for x in visi:
    
    x.drukaNosaukumu()
    x.drukatMaluSkaitu()
