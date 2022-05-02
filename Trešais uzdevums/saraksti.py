def drukaSarakstu(saraksts):
    print("saraksts garums = ", len(saraksts))
    for x in saraksts:
        print(x)
    print()

saraksts = ["Vārna","Gulbis","Žagata"]
drukaSarakstu (saraksts)

saraksts.append("Kaija")
drukaSarakstu(saraksts)

saraksts.pop(2)

drukaSarakstu(saraksts)

skaitli = [1,2,3]
drukaSarakstu(skaitli)

