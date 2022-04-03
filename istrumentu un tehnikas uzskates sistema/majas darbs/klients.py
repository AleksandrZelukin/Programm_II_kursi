import itertools
import datetime

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
        
