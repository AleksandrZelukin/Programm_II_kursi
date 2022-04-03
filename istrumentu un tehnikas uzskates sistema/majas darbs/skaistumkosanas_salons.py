#===============================================
#Skaistumkopšanas salona vadības sistēma
#===============================================
import itertools
import datetime
import fileinput


class Skaistumkopsana:
    Produkta_kategorija = "" #Ķermeņa procedūras, Sejas procedūras, Nagu kopšana un tml.
    Produkta_nosaukums = ""  #Vakuuma korekcija, Pīlings, Manikīrs un tml.
    Produkta_cena = ""

    
    id_iter = itertools.count()
    def __init__(self):
        self.Produkta_id = next(self.id_iter)+1
        self.Produkts_pieejams = True
        
    def __init__(self, prod_kategorija=None, prod_nosaukums=None, produkta_cena=None):
        self.Produkta_id = next(self.id_iter)+1
        self.Produkta_kategorija = prod_kategorija
        self.Produkta_nosaukums = prod_nosaukums
        self.Produkta_cena = produkta_cena
        self.Produkts_pieejams = True
        
    def __repr__(self):
        if self.Produkta_kategorija: return self.prod_categorija
        elif self.Produkta_nosaukums: return self.prod_nosaukums
        elif self.Produkta_cena: return self.produkta_cena
        return ''
    
    def Produkts_info(self):
        return [self.Produkta_kategorija, self.Produkta_nosaukums, self.Produkta_cena]
    
    def Produkts_info_print(self):
        print("Produkta kategorija: " + str(self.Produkta_kategorija))
        print("Produkta nosaukums: " + str(self.Produkta_nosaukums))
        print("Pakalpojuma cena: " + str(self.Produkta_cena))
        print("Pakalpojuma pieejamiba: " + str(self.Produkts_pieejams) + "\n")

        
class Klients:
    Klienta_vards=""
    Klienta_uzvards=""
    Klienta_PK=""
    Klienta_tel_numurs=0
    
    id_iter_nom = itertools.count()
    def __init__(self, _vards, _uzvards, _pk, _tel_numurs):
        self.Klienta_id = next(self.id_iter_nom)+1
        self.Klienta_vards = _vards
        self.Klienta_uzvards = _uzvards
        self.Klienta_PK = _pk
        self.Klienta_tel_numurs = _tel_numurs
        
    def Klients_info(self):
        return[self.Klienta_vards, self.Klienta_uzvards, self.Klienta_PK, self.Klienta_tel_numurs]
    
        
    def Klients_info_print(self):
        print("Klienta vards: " + self.Klienta_vards)
        print("Klienta uzvards: " + self.Klienta_uzvards)
        print("Klienta personas kods: " + self.Klienta_PK)
        print("Klienta telefona numurs: " + str(self.Klienta_tel_numurs) + "\n")
        
        
class Pakalpojums:
    Pakalpojuma_sakuma_datums = 0
    Pakalpojuma_sakuma_laiks = 0
    Pakalpojuma_daudzums = 0
    id_Produkts = 0
    id_Klients = 0
    Pakalpojums_id = 0
    
    id_iter_pakalpojums = itertools.count()
    
    def __init__(self, sakDat, sakLaik, idProdukts, idKlients, daudzums, cenaPakal):
        self.Klienta_id = next(self.id_iter_pakalpojums)+1
        self.Pakalpojuma_sakuma_datums = datetime.datetime.strptime(sakDat, "%d.%m.%Y.").date()
        self.Pakalpojuma_sakuma_laiks = datetime.datetime.strptime(sakLaik, "%H:%M").time()
        self.id_Produkts = idProdukts
        self.id_Klients = idKlients
        self.Pakalpojuma_daudzums = daudzums
        self.Pakalpojuma_cena = cenaPakal
        
    def Cena_kopa(self):
        kopeja_cena = self.Pakalpojuma_cena
        return kopeja_cena
    
    def Pakalpojuma_info_print(self):
        print("Pakalpojuma_sakuma_datums: " + str(self.Pakalpojuma_sakuma_datums.strftime("%d.%m.%Y.")) )
        print("Pakalpojuma_sakuma_laiks: " + str(self.Pakalpojuma_sakuma_laiks.strftime("%H:%M")) )
        
        print("Produkta_id: " + str(self.id_Produkts) )
        print("Klienta_id: " + str(self.id_Klients) )
        print("Pakalpojuma daudzums: " + str(self.Pakalpojuma_daudzums) )
        print("Pakalpojuma cena, EUR: " + str(self.Pakalpojuma_cena) + "\n")
        
#PROGRAMMAS IZPILDES DALA

prod1 = Skaistumkopsana("Ķermeņa procedūras", "Vakuuma terapija",  15)
prod2 = Skaistumkopsana("Ķermeņa procedūras", "Fotoepilācija", 4)
prod3 = Skaistumkopsana("Nagu kopšana", "Manikīrs", 10)
prod4 = Skaistumkopsana("Sejas procedūras","Sejas masāža",15)

print(prod1.Produkta_id)
prod1.Produkts_info()
prod1.Produkts_info_print()
print(prod2.Produkta_id)
prod2.Produkts_info()
prod2.Produkts_info_print()
print(prod3.Produkta_id)
prod3.Produkts_info()
prod3.Produkts_info_print()
print(prod4.Produkta_id)
prod4.Produkts_info_print()
prod4.Produkts_info()

klients1 = Klients("Agnija", "Barto", "122334-12234", 12345)

klients2 = Klients("Biruta", "Dundere", "232323-23345", 34567)
klients3 = Klients("Cielavina", "Egle", "342345-23123", 20394)
klients4 = Klients("Koko", "Chanel", "Nr5", 3456788)



print(klients1.Klienta_id)
klients1.Klients_info()
klients1.Klients_info_print()
a=klients1.Klients_info()
file1 = open("klients.txt","a+")
file1.write(str(a))
file1.close()
print(klients2.Klienta_id)
klients2.Klients_info()
klients2.Klients_info_print()
a=klients2.Klients_info()
file1 = open("klients.txt","a+")
file1.write(str(a))
file1.close()
print(klients3.Klienta_id)
klients3.Klients_info()
klients3.Klients_info_print()
a=klients3.Klients_info()
file1 = open("klients.txt","a+")
file1.write(str(a))
file1.close()

#==========================================================
# Pakalpojuma izveidosana


p1 = Pakalpojums("01.02.2022.", "13:35", 1,1,1,15)
print(p1.id_Klients)
p1.Pakalpojuma_info_print()


