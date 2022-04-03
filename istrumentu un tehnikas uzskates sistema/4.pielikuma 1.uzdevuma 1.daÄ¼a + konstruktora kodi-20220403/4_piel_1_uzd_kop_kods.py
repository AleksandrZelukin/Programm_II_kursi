#=========================================================================
# SĀKUMA KOMENTĀRI
#=========================================================================

'''
No Programmēšana II kursa, 4. pielikuma, 1.uzdevuma
Izveidotas klases, konstruktori un metodes, pievienotas bibliotēkas, 
nākamreiz izveidosim saskarni un ielasīšanu no teksta datnes un ierakstīšanu teksta datnē.

1. uzdevums 
Instrumentu un tehnikas uzskaites sistēma 
(1. temats. Objektorientēta programmēšana un ārējās bibliotēkas)
'''

#=========================================================================
# BIBLIOTĒKAS
#=========================================================================

import itertools # bibliotēka id veidošanai, automātiski palielināsim id skaitli
import datetime # bibliotēka, datumiem (piem., 01.01.2022) un laikiem (piem., 14:50:55)
from datetime import date #bibliotēka, izmantosim datumiem, var importēt tikai daļu no lielās bibliotēkas, ietaupa vietu

#=========================================================================
# KLASES
#=========================================================================
class Produkts:
    #pieraksta sākuma laukus/atribūtus, kā tukšus
    Produkta_kategorija = ""
    Produkta_nosaukums = ""
    Tehniskie_raksturojumi = ""
    Nomas_cena_diena = 0
    
    #veido id iterāciju, lietos count funkciju, saskaitīs klāt nākamo sk.
    id_iter = itertools.count() 
    def __init__(self):
        #pieskaita nakamo id ar next(), lai nesāktos no 0 pieskaita +1
        self.Produkta_id = next(self.id_iter)+1
        self.Produkts_pieejams = True
    ''' 
    likt # nav obligāti, ja ir vairāku rindiņu komentārs, tas labākam izskatam
    #nedrīkst rakstīt ar punktu prod._kategorija, sintakses kļūda nosaukumā Python
    #ar __init__() veido konstruktoru Python valodā
    #pievienoju konstruktorā arī nomas cenas ievadi, lai varētu to mainīt dažādiem produktiem
    
    #Python nevar viegli izveidot vairākus konstruktorus (Javā var utt.)
    #Tāpēc, pieliek =None pie laukiem, kas var būt tukši
    #Uzd. 1 šis konstruktors saukts Noma(), bet __repr__(self) būs tad, ja nebūs tukšas vērtības
    
    #Public Noma() {Produkts_pieejams = true} – konstruktors nesaņem nekādus parametrus,
    #bet pēc noklusējuma iestata, ka produkts ir pieejams.
    
    #Public Noma (string prod._kategorija, string prod._nosaukums, string tehn._raksturojumi)
    #{ Produkta_kategorija = prod._kategorija; Produkta_nosaukums = prod._nosaukums;
    #Tehniskie_raksturojumi = tehn._raksturojumi; Nomas_cena_dienā = nomas_
    #cena; Produkts_pieejams = true; } – konstruktors piedāvā savadīt visu nepieciešamo
    #informāciju par produktu un iestata, ka produkts ir pieejams.
    ''' 
    #noklusējuma cena dienā 10, pārējie lielumi None
    def __init__(self, prod_kategorija=None, prod_nosaukums=None, tehn_raksturojumi=None, nomas_cena=10):
        #pieskaita nakamo ar next(), lai nesāktos no 0 pieskaita +1
        self.Produkta_id = next(self.id_iter)+1
        self.Produkta_kategorija = prod_kategorija
        self.Produkta_nosaukums = prod_nosaukums
        self.Tehniskie_raksturojumi = tehn_raksturojumi
        #Ja nevēlas pievienot maināmu cenu, pēc noklusējuma var uzlikt 15, kā uzd. noteikumos
        self.Nomas_cena_diena = nomas_cena
        self.Produkts_pieejams = True
    #Ja nebūs tukšs konstruktors, tad izvada datus, citādi izvada neko
    #uzd.1 šis konstruktos nav tukšs Noma(prod_kategorija, prod_nosaukums, tehn_raksturojumi)
    def __repr__(self):   
        if self.Produkta_kategorija:  return self.prod_kategorija
        elif self.Produkta_nosaukums:  return self.prod_nosaukums
        elif self.Tehniskie_raksturojumi:  return self.tehn_raksturojumi
        elif self.Nomas_cena_diena:  return self.nomas_cena
        return ''
    
    #atgriezt produkta info
    def Produkts_info(self):
        return [self.Produkta_kategorija, self.Produkta_nosaukums, self.Tehniskie_raksturojumi, self.Nomas_cena_diena]
    
    #drukāt produkta info, str() pārvērš lietas, kas nav simbolu virknes par simbolu virknēm
    # \n ir kā enter, pāriet uz jaunu rindu
    def Produkts_info_print(self):
        print("Produkta kategorija: " + str(self.Produkta_kategorija))
        print("Produkta nosaukums: " + str(self.Produkta_nosaukums))
        print("Tehniskie raksturojumi: " + str(self.Tehniskie_raksturojumi))
        #str() pārvērš skaitli par simbolu virkni
        print("Nomas cena par dienu: " + str(self.Nomas_cena_diena))
        print("Produkts pieejams: " + str(self.Produkts_pieejams) + "\n")

#=========================================================================

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

#=========================================================================

class Noma:
    #definē atribūtu/lauku sākuma vērtības, tās vēlāk tiek pārrakstītas ja vien nav tukšs konstruktors
    Nomas_sakuma_datums = 0
    Nomas_beigu_datums = 0
    Nomas_sodienas_datums = 0
    Nomas_daudzums = 0
    Nomas_cena_diena = 10
    id_Produkts = 0
    id_Nomnieks = 0
    Noma_id = 0
    
    #automātiskai id palielināšanai
    id_iter_noma = itertools.count() 
    
    #mainīgie konstruktorā jasakārto tā, ka noklusējuma parametri ir pēc tiem, kas jāievada ar roku
    def __init__(self, sakDat, beigDat, idProdukts, idNomnieks, daudzums, cenaDiena):
        #reālā daļu kur notiek id palielināšana ar funkciju next(). +1, jo citādi sāk skaitīt id no 0
        self.Nomnieka_id = next(self.id_iter_noma)+1
        #1)lieto datetime bibliotēku, tad 2) apakšbibliotēku ar tādu pašu vārdu datetime
        #3)strptime() metode pārvērš simbolu virkni par datuma objektu
        #4)date() metode pārvērš datumu no 01.01.2022 - > 2022-01-01, noklusējuma formā, lai varētu atņemtu datumus vēlāk
        self.Nomas_sakuma_datums = datetime.datetime.strptime(sakDat,"%d.%m.%Y.").date() 
        self.Nomas_beigu_datums = datetime.datetime.strptime(beigDat,"%d.%m.%Y.").date() 
        self.id_Produkts = idProdukts
        self.id_Nomnieks = idNomnieks
        self.Nomas_daudzums = daudzums
        self.Nomas_cena_diena = cenaDiena
    
    #Padod metodē ierakstītu simb. virkni ar 'šodienas datumu', to pārvērš par datetime objektu
    #Tad var atņemt datumus, pārvērst rezultātu dienās (dienas ir skaitlis), [un ņemt absolūto vērtību <- neobligāti]
    def Nomas_atlikusais_laiks(self, sodienasDat):
        self.Nomas_sodienas_datums = datetime.datetime.strptime(sodienasDat,"%d.%m.%Y.").date() 
        return abs((self.Nomas_beigu_datums - self.Nomas_sodienas_datums).days)
    
    #rēķina kopējo cenu = nomas cena dienā * (dienu skaits + 1) jo neieskaita vienu dienu, tāpēc +1
    def Cena_kopa(self):
        kopeja_cena = self.Nomas_cena_diena*(((self.Nomas_beigu_datums-self.Nomas_sakuma_datums).days)+1)
        return kopeja_cena
    
    #izdrukā info par nomu, str() pārvērš skaitli vai datumu par simbolu virkni, '\n' - pāriet uz jaunu rindiņu
    def Noma_info_print(self):
        print("Nomas sakuma datums: " + str(self.Nomas_sakuma_datums.strftime("%d.%m.%Y.")) )
        print("Nomas beigu datums: " + str(self.Nomas_beigu_datums.strftime("%d.%m.%Y.")) )
        print("Produkta id: " + str(self.id_Produkts) )
        print("Nomnieka id: " + str(self.id_Nomnieks) )
        print("Nomas prieksmeta daudzums: " + str(self.Nomas_daudzums) )
        print("Nomas cena diena, EUR: " + str(self.Nomas_cena_diena)  + "\n")

#=========================================================================
# PROGRAMMAS IZPILDES DAĻA
#=========================================================================

#veido produktu objektu
prod1 = Produkts("zagis", "Bosch GSR 18", "2.gab. / 18V / 5,0 Ah / Li-oh", 15)
prod2 = Produkts()
prod3 = Produkts("slipmasina", "Slipm. AS12345")

#izdrukā informaciju par 3 produktu objektiem
print(prod1.Produkta_id)
prod1.Produkts_info()
prod1.Produkts_info_print()
print(prod2.Produkta_id)
prod2.Produkts_info()
prod2.Produkts_info_print()
print(prod3.Produkta_id)
prod3.Produkts_info()
prod3.Produkts_info_print()

#=========================================================================

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

#=========================================================================

# veido nomas objektu n1, padod argumentus, konkrētas vērtības
n1 = Noma("07.12.2022.", "17.12.2022.", 1, 1, 1, 15)
#ievada 'šodienas datumu', lai noteiktu cik dienas palikušas nomai
dienu_sk = n1.Nomas_atlikusais_laiks("08.12.2022.")
print("Nomas atlikuso dienu skaits, neskaitot sodienu, ir: " + str(dienu_sk))
#rēķina kopējo cenu par visu nomu
cena_kopa = n1.Cena_kopa()
print("Kopeja nomas cena, EUR, ir: " + str(cena_kopa))

print(n1.id_Nomnieks)
n1.Noma_info_print()

#tas pats, kas par pirmo nomas objektu, tagad veido un drukā par otro nomas objektu n2
n2 = Noma("01.08.2022.", "31.08.2022.", 2, 2, 3, 25)
dienu_sk = n2.Nomas_atlikusais_laiks("10.08.2022.")
print("Nomas atlikuso dienu skaits, neskaitot sodienu, ir: " + str(dienu_sk))
cena_kopa = n2.Cena_kopa()
print("Kopeja nomas cena, EUR, ir: " + str(cena_kopa))

print(n2.id_Nomnieks)
n2.Noma_info_print()
