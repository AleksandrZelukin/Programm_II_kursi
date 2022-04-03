import itertools # bibliotēka id veidošanai, automātiski palielināsim id skaitli
import datetime # bibliotēka, datumiem (piem., 01.01.2022) un laikiem (piem., 14:50:55)
from datetime import date #bibliotēka, izmantosim datumiem, var importēt tikai daļu no lielās bibliotēkas, ietaupa vietu

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
n2 = Noma("01.08.2022.", "31.08.2022.", 2, 2, 1, 25)
dienu_sk = n2.Nomas_atlikusais_laiks("10.08.2022.")
print("Nomas atlikuso dienu skaits, neskaitot sodienu, ir: " + str(dienu_sk))
cena_kopa = n2.Cena_kopa()
print("Kopeja nomas cena, EUR, ir: " + str(cena_kopa))

print(n2.id_Nomnieks)
n2.Noma_info_print()
