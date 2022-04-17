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
        return ['Produkta kategorija: '+self.Produkta_kategorija, ' Produkta nosaukums: '+self.Produkta_nosaukums, ' Tehniskie raksturojumi: ' +self.Tehniskie_raksturojumi, ' Noklusejuma nomas cena diena: '+str(self.Nomas_cena_diena)]
    
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
        return ['Nomnieka vards: ' + self.Nomnieka_vards, ' Nomnieka uzvards: '+self.Nomnieka_uzvards, ' Nomnieka pers. kods: '+self.Nomnieka_PK, ' Telefona numurs: '+self.Nomnieka_tel_numurs]
        
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
    def __init__(self, sakDat, beigDat, idProdukts, idNomnieks, daudzums, cenaDiena, sodienasDat):
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
        self.Nomas_sodienas_datums = sodienasDat
    
    #Padod metodē ierakstītu simb. virkni ar 'šodienas datumu', to pārvērš par datetime objektu
    #Tad var atņemt datumus, pārvērst rezultātu dienās (dienas ir skaitlis), [un ņemt absolūto vērtību <- neobligāti]
    def Nomas_atlikusais_laiks(self, sodienasDat):
        self.Nomas_sodienas_datums = datetime.datetime.strptime(sodienasDat,"%d.%m.%Y.").date() 
        return abs((self.Nomas_beigu_datums - self.Nomas_sodienas_datums).days)
    
    #rēķina kopējo cenu = nomas cena dienā * (dienu skaits + 1) jo neieskaita vienu dienu, tāpēc +1
    def Cena_kopa(self):
        n_cena = int(self.Nomas_cena_diena)
        dienu_sk = int ( ((self.Nomas_beigu_datums-self.Nomas_sakuma_datums).days) + 1 )
        daudz = int (self.Nomas_daudzums)
        kopeja_cena = n_cena * dienu_sk * daudz #self.Nomas_cena_diena*(((self.Nomas_beigu_datums-self.Nomas_sakuma_datums).days)+1)
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


'''
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
'''
#=========================================================================

# veido trīs nomnieku objektus nom1, nom2, nom3, padod tiem argumentus (konkrētas vērtības)
nom1 = Nomnieks("Andrejs", "Priede", "123456-78910", 12345678)
nom2 = Nomnieks("Anna", "Balode", "987654-32100", 87654321)
nom3 = Nomnieks("Zane", "Egle", "123456-12345", 10101010)
'''
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
'''
#=========================================================================

# veido nomas objektu n1, padod argumentus, konkrētas vērtības
n1 = Noma("07.12.2022.", "17.12.2022.", 1, 1, 1, 15, "15.12.2022.")
#ievada 'šodienas datumu', lai noteiktu cik dienas palikušas nomai
dienu_sk = n1.Nomas_atlikusais_laiks("08.12.2022.")
cena_kopa = n1.Cena_kopa()
'''
print("Nomas atlikuso dienu skaits, neskaitot sodienu, ir: " + str(dienu_sk))
#rēķina kopējo cenu par visu nomu
print("Kopeja nomas cena, EUR, ir: " + str(cena_kopa))
print(n1.id_Nomnieks)
n1.Noma_info_print()
'''
#tas pats, kas par pirmo nomas objektu, tagad veido un drukā par otro nomas objektu n2
n2 = Noma("01.08.2022.", "31.08.2022.", 2, 2, 3, 25, "20.08.2022.")
dienu_sk = n2.Nomas_atlikusais_laiks("10.08.2022.")
cena_kopa = n2.Cena_kopa()

'''
print("Nomas atlikuso dienu skaits, neskaitot sodienu, ir: " + str(dienu_sk))
print("Kopeja nomas cena, EUR, ir: " + str(cena_kopa))
print(n2.id_Nomnieks)
n2.Noma_info_print()
'''

#=========================================================================
# SASKARNE AR TRIM SADAĻĀM
#=========================================================================
import PySimpleGUI as sg #saskarnes bibliotēka

#definē sadaļas
            #def __init__(self, prod_kategorija=None, prod_nosaukums=None, tehn_raksturojumi=None, nomas_cena=10):
            #teksta ievades no klaviatūras atslēgas, key, ir tādi paši nosaukumi, kā konstruktorā __init__() 
            #(bet tas nav obligāti, ka nosaukumiiem jābūt tādiem pašiem, vienkārši atvieglo izpratni, par to, kur jāieliek ierakstītās vērtības)
            #atslēgas, key, ir nepieciešamas, jo no tām tiek veidota vērtību (angliski values) vārdnīca (angliski dictionary), 
            #kurā saglabā kā masīva elementus ievadītās vērtības 
            #Taču Python to sauc par list, kas nozīmē saraksts, bet citās valodās pēc šāda list veida tiek veidoti masīvi, un saraksti satur elementus ar norādēm.
sadala1 = [[sg.Text('Produkta kategorija', size=(19,1)),sg.Input('',key='prod_kategorija')],
           [sg.Text('Produkta nosaukums', size=(19,1)),sg.Input('',key='prod_nosaukums')],
           [sg.Text('Tehniskie raksturojumi', size=(19,1)),sg.Input('',key='tehn_raksturojumi')],
           [sg.Button('Saglabat produkta datus')], 
           
           #def __init__(self, _vards, _uzvards, _pk, _tel_numurs):
           [sg.Text('Nomnieka vards', size=(19,1)),sg.Input('',key='_vards')],
           [sg.Text('Nomnieka uzvards', size=(19,1)),sg.Input('',key='_uzvards')],
           [sg.Text('Personas kods', size=(19,1)),sg.Input('',key='_pk')],
           [sg.Text('Telefons', size=(19,1)),sg.Input('',key='_tel_numurs')],
           [sg.Button('Saglabat nomnieka datus')], 

           #def __init__(self, sakDat, beigDat, idProdukts, idNomnieks, daudzums, cenaDiena, sodienasDat):
           #!!!PIELIKTS KLAT SODIENAS DATUMS
           [sg.Text('Sakuma datums', size=(19,1)),sg.Input('',key='sakDat')],
           [sg.Text('Beigu datums', size=(19,1)),sg.Input('',key='beigDat')],
           [sg.Text('Produkta id', size=(19,1)),sg.Input('',key='idProdukts')],
           [sg.Text('Nomnieka id', size=(19,1)),sg.Input('',key='idNomnieks')],
           [sg.Text('Prieksmeta daudzums', size=(19,1)),sg.Input('',key='daudzums')],
           [sg.Text('Nomas cena diena', size=(19,1)),sg.Input('',key='cenaDiena')],
           [sg.Text('Sodienas datums', size=(19,1)),sg.Input('',key='sodienasDat')],
           [sg.Button('Saglabat nomas datus')]]

sadala2=[[sg.Button('Produkta info, izvada uz ekrana')],
          [sg.Button('Nomnieka info, izvada uz ekrana')],
          [sg.Button('Noma: atlikusais laiks, izvada uz ekrana')],
          [sg.Button('Noma: Cena par nomu kopa, izvada uz ekrana')]]

sadala3= [[sg.Button('Produkts: veidot atskaiti teksta faila formata')],
          [sg.Button('Nomnieks: veidot atskaiti teksta faila formata')]]

#Definē sadaļas virsrakstu joslas nosaukumus, tab angliski  
#ja nelieto tēmu (theme), var manuāli veidot izskatu
tabgrp = [[sg.TabGroup([[sg.Tab('Datu ievade', sadala1, title_color='Red',border_width =10,
              background_color='Yellow', element_justification= 'center'),
            sg.Tab('Datu izvade', sadala2,title_color='Yellow',
              background_color='Green', element_justification= 'center'),
            sg.Tab('Atskaites printesana', sadala3, title_color='Red',border_width =10,
              background_color='Yellow',
              tooltip='Veido atskaites teksta failu', element_justification= 'center')]],
              tab_location='centertop', title_color='Black', 
              tab_background_color='Brown',selected_title_color='Yellow',
              selected_background_color='Gray', border_width=5), sg.Button('Aizvert')]]  
        
#Definē saskarnes logu
window =sg.Window("  Noma",tabgrp)

#izveido tukšus atskaites failus
file=open("Produkta_atskaite.txt", "w")
file=open("Nomnieka_atskaite.txt", "w")

#Ielasa vērtības, ko ievadījis lietotājs, tā kā vērtības vairākas veido ciklu while
while True: 
  #pogu nospiešana arī ir notikums, angliski - event, ciklā ielasa notikušos notikumus, 
  #kas var būt ne tikai pogas nospiešanas, bet šajā uzdevumā tie lielākoties būs tikai pogas nospiešanas notikumi, 
  #veido vārdnīcu ar vērtībām no visām iegūtajām vērtībām pēc pogas nospiešanas, kas ir event jeb notikums
  event, values = window.read()
  #ja aizver logu, tad aizver programmas saskarni
  if event == sg.WIN_CLOSED or event == 'Aizvert':
    break
#======================================= 1 sadala ===============
    #nosaukumus ņem no klases konstruktoriem, lai nesajauktu
    #def __init__(self, prod_kategorija=None, prod_nosaukums=None, tehn_raksturojumi=None, nomas_cena=10):
  elif event == 'Saglabat produkta datus':
    prod4 = Produkts(values['prod_kategorija'], values['prod_nosaukums'], values['tehn_raksturojumi'])
  #def __init__(self, _vards, _uzvards, _pk, _tel_numurs):
  elif event == 'Saglabat nomnieka datus':
    nom4 = Nomnieks(values['_vards'], values['_uzvards'], values['_pk'], values['_tel_numurs'])
  #def __init__(self, sakDat, beigDat, idProdukts, idNomnieks, daudzums, cenaDiena):
  elif event == 'Saglabat nomas datus':
    n4 = Noma(values['sakDat'], values['beigDat'], values['idProdukts'], values['idNomnieks'], values['daudzums'], values['cenaDiena'], values['sodienasDat'])
#======================================= 2 sadala ===============
  # izmanto jau gatavās funkcijas no klasēm, ko veidojām 1. daļā
  elif event == 'Produkta info, izvada uz ekrana':
    # uzlecosais logs ar informaciju
    prod4.Produkts_info_print()
  elif event == 'Nomnieka info, izvada uz ekrana':
    nom4.Nomnieks_info_print()

    
  elif event == 'Noma: atlikusais laiks, izvada uz ekrana':
    print("Nomas atlikusais laiks: " + str(n4.Nomas_atlikusais_laiks(values['sodienasDat'])))
  elif event == 'Noma: Cena par nomu kopa, izvada uz ekrana':
    print("Cena kopa: " + str(n4.Cena_kopa()))
#======================================= 3 sadala ===============
#================================================================
# ATSKAITES UZ TEKSTA DATNI
#================================================================
  #tukšs dokuments jau izveidots, ar "w" - pārraksta visu un sāk dokumentu no jauna, bet ar "a" - append, pieliek klāt informāciju
  elif event == 'Produkts: veidot atskaiti teksta faila formata':
    file=open("Produkta_atskaite.txt", "a")
    file.write(str(prod4.Produkts_info()))
    file.write("\n")
    file.close()
  # open() - atver datni, write() ieraksta datnē jaunas rindiņas, jo ierakstīšanas forma ir a - append, pievienot klāt beigās
  #close() - aizver failu
  elif event == 'Nomnieks: veidot atskaiti teksta faila formata':
    file=open("Nomnieka_atskaite.txt", "a")
    file.write(str(nom4.Nomnieks_info()))
    file.write("\n")
    file.close()
#======================================= sadalu beigas ==========

window.close() #aizver logu saskarnei
