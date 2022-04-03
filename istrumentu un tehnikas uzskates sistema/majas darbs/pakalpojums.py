class Noma:
    Nomas_sakuma_datums = 0
    Nomas_beigu_datums = 0
    Nomas_sodienas_datums = 0
    Nomas_daudzums = 0
    Nomas_cena_diena = 10
    id_Produkts = 0
    id_Klients = 0
    Noma_id = 0
    
    id_iter_noma = itertools.count()
    
    def __init__(self, sakDat, beigDat, idProdukts, idKlients, daudzums, cenaDiena):
        self.Klienta_id = next(self.id_iter_noma)+1
        self.Nomas_sakuma_datums = datetime.datetime.strptime(sakDat, "%d.%m.%Y.").date()
        self.Nomas_beigu_datums = datetime.datetime.strptime(beigDat, "%d.%m.%Y.").date()
        self.id_Produkts = idProdukts
        self.id_Klients = idKlients
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
        print("Klienta_id: " + str(self.id_Klients) )
        print("Nomas prieksmeta daudzums: " + str(self.Nomas_daudzums) )
        print("Nomas cena diena, EUR: " + str(self.Nomas_cena_diena) + "\n")
        
