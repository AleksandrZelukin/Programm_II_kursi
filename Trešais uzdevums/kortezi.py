gads = ('janvāris',
        'februāris',
        'marts',
        'āprīlis',
        'maijs',
        'jūnijs',
        'jūlijs',
        'augusts',
        'septembris',
        'oktobris',
        'novembris',
        'decembris')
dzimMenesis = str(input("Ievadi mēmesi: "))
num = gads.index(dzimMenesis)
print("Dzimšanas mēnesis: ",dzimMenesis," numurs ir: ",num+1)
