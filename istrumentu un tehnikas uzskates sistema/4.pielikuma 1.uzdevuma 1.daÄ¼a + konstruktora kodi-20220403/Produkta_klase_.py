import itertools #bibliotēka, izmantos, lai automātiski palielinātu id skaitli

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



