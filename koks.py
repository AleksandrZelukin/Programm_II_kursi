class koks:
    lauks1 = koka_tips
    lauks2 = koka_veids
    
    # Metode jeb funkcija
    def drukat(self):
        print("Koka tips: ", self.lauks1)
        print("Koka veids: ", self.lauks2)
    #objekta instance
    Liepa = Koks()
    #Piekļūšana klases atribūtiem caur objektiem
    print(Liepa.lauks1)
    
    
