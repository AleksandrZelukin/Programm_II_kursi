import itertools
import datetime
import fileinput
#with fileinput.FileInput(files=(prieksmeti.txt, nomnieki.txt, noma.txt), mode=rU)):
class Produkts:
    Produkta_kategorija = ""
    Produkta_nosaukums = ""
    Tehniskie_raksturojumi = ""
    Nomas_cena_diena = 0
    
    id_iter = itertools.count()
    def __init__(self):
        self.Produkta_id = next(self.id_iter)+1
        self.Produkts_pieejams = True
        
    def __init__(self, prod_kategorija=None, prod_nosaukums=None, tehn_raksturojums=None, nomas_cena=10):
        self.Produkta_id = next(self.id_iter)+1
        self.Produkta_kategorija = prod_kategorija
        self.Produkta_nosaukums = prod_nosaukums
        self.Tehniskie_raksturojumi = tehn_raksturojums
        self.Nomas_cena_diena = nomas_cena
        self.Produkts_pieejams = True
        
    def __repr__(self):
        if self.Produkta_kategorija: return self.prod_categorija
        elif self.Produkta_nosaukums: return self.prod_nosaukums
        elif self.Tehniskie_raksturojumi: return self.tehn_raksturojumi
        elif self.Nomas_cena_diena: return self.nomas_cena
        return ''
    
    def Produkts_info(self):
        return [self.Produkta_kategorija, self.Produkta_nosaukums, self.Tehniskie_raksturojumi, self.Nomas_cena_diena]
    
    def Rrodukts_info_print(self):
        print("Produkta kategorija: " + str(self.Produkta_kategorija))
        print("Produkta nosaukums: " + str(self.Produkta_nosaukums))
        print("Tehniskie raksturojumi: " + str(self.Tehniskie_raksturojumi))
        print("Nomas cena par dienu: " + str(self.Nomas_cena_diena))
        print("Produkts pieejams: " + str(self.Produkts_pieejams) + "\n")
        
class Nomnieks:
    Nomnieka_vards=""
    Nomnieka_uzvards=""
    Nomnieka_PK=""
    Nomnieka_tel_numurs=0
    
    id_iter_nom = itertools.count()
    def __init__(self, _vards, _uzvards, _pk, _tel_numurs):
        self.Nomnieka_id = next(self.id_iter_nom)+1
        self.Nomnieka_vards = _vards
        self.Nomnieka_uzvards = _uzvards
        self.Nomnieka_PK = _pk
        self.Nomnieka_tel_numurs = _tel_numurs
        
    def Nomnieks_info(self):
        return[self.Nomnieka_vards, self.Nomnieka_uzvards, self.Nomnieka_PK, self.Nomnieka_tel_numurs]
    
        
    def Nomnieks_info_print(self):
        print("Nomnieka vards: " + self.Nomnieka_vards)
        print("Nomnieka uzvards: " + self.Nomnieka_uzvards)
        print("Nomnieka personas kods: " + self.Nomnieka_PK)
        print("Nomnieka telefona numurs: " + str(self.Nomnieka_tel_numurs) + "\n")
        
class Noma:
    Nomas_sakuma_datums = 0
    Nomas_beigu_datums = 0
    Nomas_sodienas_datums = 0
    Nomas_daudzums = 0
    Nomas_cena_diena = 10
    id_Produkts = 0
    id_Nomnieks = 0
    Noma_id = 0
    
    id_iter_noma = itertools.count()
    
    def __init__(self, sakDat, beigDat, idProdukts, idNomnieks, daudzums, cenaDiena):
        self.Nomnieka_id = next(self.id_iter_noma)+1
        self.Nomas_sakuma_datums = datetime.datetime.strptime(sakDat, "%d.%m.%Y.").date()
        self.Nomas_beigu_datums = datetime.datetime.strptime(beigDat, "%d.%m.%Y.").date()
        self.id_Produkts = idProdukts
        self.id_Nomnieks = idNomnieks
        self.Nomas_daudzums = daudzums
        self.Nomas_cena_diena = cenaDiena
        
    def Nomas_atlikusais_laiks(self, sodienasDat):
        self.Nomas_sodienas_datums = datetime.datetime.strptime(sodienasDat, "%d.%m.%Y.").date()
        return abs((self.Nomas_beigu_datums - self.Nomas_sodienas_datums).days)
    
    def Cena_kopa(self):
        kopeja_cena = self.Nomas_cena_diena*(((self.Nomas_beigu_datums-self.Nomas_sakuma_datums).days)+1)
        return kopeja_cena
    
    def Noma_info_print(self):
        print("Nomas_sakuma_datums: " + str(self.Nomas_sakuma_datums.strftime("%d.%m.%Y.")) )
        print("Nomas_beigu_datums: " + str(self.Nomas_beigu_datums.strftime("%d.%m.%Y.")) )
        print("Produkta_id: " + str(self.id_Produkts) )
        print("Nomnieka_id: " + str(self.id_Nomnieks) )
        print("Nomas prieksmeta daudzums: " + str(self.Nomas_daudzums) )
        print("Nomas cena diena, EUR: " + str(self.Nomas_cena_diena) + "\n")
        
#PROGRAMMAS IZPILDES DALA

prod1 = Produkts("zagis", "Bosch GSR 18", "2.gab. /18V / 5,0 Ah / Li-oh", 15)
prod2 = Produkts()
prod3 = Produkts("slipmasina", "AS123456")

print(prod1.Produkta_id)
prod1.Produkts_info()
prod1.Rrodukts_info_print()
print(prod2.Produkta_id)
prod2.Produkts_info()
prod2.Rrodukts_info_print()
print(prod3.Produkta_id)
prod3.Produkts_info()
prod3.Rrodukts_info_print()

nom1 = Nomnieks("A", "P", "12-12", 12345)
nom2 = Nomnieks("B", "D", "23-23", 34567)
nom3 = Nomnieks("C", "E", "34-23", 20394)

print(nom1.Nomnieka_id)
nom1.Nomnieks_info()
nom1.Nomnieks_info_print()
print(nom2.Nomnieka_id)
nom2.Nomnieks_info()
nom2.Nomnieks_info_print()
print(nom3.Nomnieka_id)
nom3.Nomnieks_info()
nom3.Nomnieks_info_print()

n1 = Noma("07.12.2022.", "17.12.2022.", 1,1,1,15)
dienu_sk = n1.Nomas_atlikusais_laiks("08.12.2022.")
print("Nomas atlikuso dienu skaits, neskaitot sodienu, ir: " + str(dienu_sk))
cena_kopa = n1.Cena_kopa()
print("Kopeja nomas cena, EUR, ir: " + str(cena_kopa))
      
print(n1.id_Nomnieks)
n1.Noma_info_print()

