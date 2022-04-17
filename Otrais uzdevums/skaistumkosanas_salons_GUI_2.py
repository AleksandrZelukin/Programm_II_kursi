#===============================================
#Skaistumkopšanas salona vadības sistēma
#===============================================
import itertools
import datetime
import fileinput
import PySimpleGUI as sg
sg.theme('SandyBeach')

class Produkts:
    Prod_kategorija = ""
    Prod_nosaukums = ""
    Prod_cena = ""

    
    id_iter = itertools.count()
    def __init__(self):
        self.Prod_id = next(self.id_iter)+1
        self.Prod_pieejams = True
        

    def __init__(self, _pakalpojums, _produkts, _cena):
        self.Prod_id = next(self.id_iter)+1
        self.Prod_kategorija = _pakalpojums
        self.Prod_nosaukums = _produkts
        self.Prod_cena = _cena
#        self.Prod_pieejams = True
        
    def __repr__(self):
        if self.Prod_kategorija: return self.prod_categorija
        elif self.Prod_nosaukums: return self.prod_nosaukums
        elif self.Prod_cena: return self.prod_cena
        return ''
    
    def Produkts_info(self):
        return [self.Prod_kategorija, self.Prod_nosaukums, self.Prod_cena]
    
    def Produkts_info_print(self):
        print("Produkta kategorija: " + str(self.Prod_kategorija))
        print("Produkta nosaukums: " + str(self.Prod_nosaukums))
        print("Pakalpojuma cena: " + str(self.Prod_cena))
#        print("Pakalpojuma pieejamiba: " + str(self.Prod_pieejams) + "\n")



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
'''       
prod = Produkts("Ķermeņa procedūras", "Vakuuma terapija",  15)
        
print(prod.Prod_id)
prod.Produkts_info()
prod.Produkts_info_print()        

theme_name_list = sg.theme_list()
#print(theme_name_list)
'''
sadala1 = [[sg.Text('Ķermeņa procedūras, Sejas procedūras, Nagu kopšana un tml.',font='Helvetica 14')],
           [sg.Text('Procedūras kategorija',size=(24,1)),sg.Input('',key='_pakalpojums')],
           [sg.Text('Vakuuma korekcija, Pīlings, Manikīrs un tml.',font='Helvetica 14')],
           [sg.Text('Pakalpojuma nosaukums',size=(24,1)),sg.Input('',key='_produkts')],
           [sg.Text('Pakalpojuma cena',size=(24,1)),sg.Input('',key='_cena')],
           [sg.Button('Saglabat pakalpojuma datus')], 
           
           #def __init__(self, _vards, _uzvards, _pk, _tel_numurs):
           [sg.Text('Klienta vards', size=(22,1)),sg.Input('',key='_vards')],
           [sg.Text('Klienta uzvards', size=(22,1)),sg.Input('',key='_uzvards')],
           [sg.Text('Personas kods', size=(22,1)),sg.Input(' - ',key='_pk')],
           [sg.Text('Telefons', size=(22,1)),sg.Input('(+371)  ',key='_tel_numurs')],
           [sg.Button('Saglabat klienta datus')], 

           #def __init__(self, sakDat, beigDat, idProdukts, idNomnieks, daudzums, cenaDiena, sodienasDat):
           [sg.Text('Sakuma datums', size=(22,1)),sg.Input('',key='sakDat')],
           [sg.Text('Sakuma laiks', size=(22,1)),sg.Input('',key='sakTime')],
           [sg.Text('Produkta id', size=(22,1)),sg.Input('',key='idProdukts')],
           [sg.Text('Klienta id', size=(22,1)),sg.Input('',key='idKlients')],
           [sg.Text('Pakalpijuma daudzums', size=(22,1)),sg.Input('',key='daudzums')],
           
           [sg.Text('Sodienas datums', size=(22,1)),sg.Input('',key='sodienasDat')],
           [sg.Button('Saglabat Skaustuma salona pakalpojuma datus')]]

sadala2 = [[sg.Button('Pakalpojuma info, izvada uz ekrana')],
          [sg.Button('Klienta info, izvada uz ekrana')],
          
          [sg.Button('Cena par pakalpujumu, izvada uz ekrana')]]

sadala3 = [[sg.Button('Pakalpojums: veidot atskaiti teksta faila formata')],
          [sg.Button('Klients: veidot atskaiti teksta faila formata')]]


sadalu_grupa = [[sg.TabGroup
               ([[sg.Tab('Datu ievade', sadala1),
               sg.Tab('Datu izvade', sadala2),
               sg.Tab('Atskaites printesana', sadala3)]]),
               sg.Button('Aizvert',pad=(0,0,1),font='Helvetica 22')]]

           
window =sg.Window("Skaistumkopšanas salons",sadalu_grupa)

file=open("Pakalpojuma_atskaite.txt", "w")
file=open("Klienta_atskaite.txt", "w")

while True: 
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Aizvert':
    break

#======================================= 1 sadala ===============
  elif event == 'Saglabat pakalpojuma datus':
    prod = Produkts(values['_pakalpojums'], values['_produkts'], values['_cena'])

  elif event == 'Saglabat klienta datus':
    klients = Klients(values['_vards'], values['_uzvards'], values['_pk'], values['_tel_numurs'])      
   
 
#======================================= 2 sadala ===============
  elif event == 'Pakalpojuma info, izvada uz ekrana':
    prod.Produkts_info_print()
  elif event == 'Klienta info, izvada uz ekrana':
    klients.Klients_info_print()

    


#======================================= 3 sadala ===============
  elif event == 'Pakalpojums: veidot atskaiti teksta faila formata':
    file=open("Pakalpojuma_atskaite.txt", "a")
    file.write(str(prod.Produkts_info()))
    file.write("\n")
    file.close()

  elif event == 'Klients: veidot atskaiti teksta faila formata':
    file=open("Klienta_atskaite.txt", "a")
    file.write(str(klients.Klients_info()))
    file.write("\n")
    file.close()

window.close() #aizver logu saskarnei



