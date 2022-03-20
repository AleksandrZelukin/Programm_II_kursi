class Figura:
    def __init__(self, malas, nosaukums):
        self.malas = malas
        self.nosaukums = nosaukums

    def drukatMaluSkaitu(self):
        print ("Malu skaits "+f"{self.malas}")

    def drukaNosaukumu(self):
        print ("Figuras nosaukums "+f"{self.nosaukums}")


class Trijsturis(Figura):
    def drukatInfo(self):
        self.drukatMaluSkaitu(self)
        self.drukaNosaukumu(self)


class Tainsturis(Figura):
    def drukatInfo(self):
        self.drukatMaluSkaitu(self)
        self.drukaNosaukumu(self)


class Kvadrats(Figura):
    def drukatInfo(self):
        self.drukatMaluSkaitu(self)
        self.drukaNosaukumu(self)

   
trijsturis1 = Trijsturis(3, "Trijstūris")
tainsturis1 = Tainsturis(4, "Tainstūris")
kvadrats1 = Kvadrats(4,"Kvadrāts")

visi = [trijsturis1, tainsturis1, kvadrats1]
for x in visi:
    
    x.drukaNosaukumu()
    x.drukatMaluSkaitu()
