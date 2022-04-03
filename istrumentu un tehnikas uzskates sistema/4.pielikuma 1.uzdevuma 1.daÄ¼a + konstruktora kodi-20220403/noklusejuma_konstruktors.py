class Trissturis:

	#noklusējuma konstruktors
	def __init__(self):
		self.mala = 6

	#metode (jeb funkcija) izdrukāt perimetru
	def drukat_Perimetru(self):
		print( "Perimetrs: ", self.mala+self.mala+self.mala )

# veido klases objektu, ar noklusējuma datiem
obj1 = Trissturis()

# izsauc perimetra drukāšanas metodi objektam obj1
obj1.drukat_Perimetru()



