import itertools #bibliotēka automātiskai id veidošanai

class Nomnieks:
    #pieraksta sākuma laukus/atribūtus, kā tukšus
    Nomnieka_vards=""
    Nomnieka_uzvards=""
    Nomnieka_PK=""
    Nomnieka_tel_numurs=0
    
    #automātiskai id palielināšanai
    id_iter_nom = itertools.count() 
    #ja sākas ar _ mainīgais ir privāts
    def __init__(self, _vards, _uzvards, _pk, _tel_numurs):
        #veido automātiski nomnieka id
        self.Nomnieka_id = next(self.id_iter_nom)+1
        self.Nomnieka_vards = _vards
        self.Nomnieka_uzvards = _uzvards
        self.Nomnieka_PK = _pk
        self.Nomnieka_tel_numurs = _tel_numurs
    
    #atgriezt nomnieka info, šī ir klases metode nevis parastā metode/funkcija
    #tāpēc jāpadod parametrs self, tāpat arī tālāk klases metodēm
    def Nomnieks_info(self):
        return [self.Nomnieka_vards, self.Nomnieka_uzvards, self.Nomnieka_PK, self.Nomnieka_tel_numurs]
        
    #izdrukāt nomnieka info
    def Nomnieks_info_print(self):
        print("Nomnieka vards: " + self.Nomnieka_vards)
        print("Nomnieka uzvards: " + self.Nomnieka_uzvards)
        print("Nomnieka personas kods: " + self.Nomnieka_PK)
        print("Nomnieka telefons: " + str(self.Nomnieka_tel_numurs) + "\n")

# veido trīs nomnieku objektus nom1, nom2, nom3, padod tiem argumentus (konkrētas vērtības)
nom1 = Nomnieks("Andrejs", "Priede", "123456-78910", 12345678)
nom2 = Nomnieks("Anna", "Balode", "987654-32100", 87654321)
nom3 = Nomnieks("Zane", "Egle", "123456-12345", 10101010)

#pārbauda kā strādā drukāšana un datu atgriešana visiem trīs nomnieku objektiem
print(nom1.Nomnieka_id)
nom1.Nomnieks_info()
nom1.Nomnieks_info_print()
print(nom2.Nomnieka_id)
nom2.Nomnieks_info()
nom2.Nomnieks_info_print()
print(nom3.Nomnieka_id)
nom3.Nomnieks_info()
nom3.Nomnieks_info_print()



