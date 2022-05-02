def parbaudaSteka(v):
    steks = []
    rez = "pareizi"
    for i in v:
        if i == '(':
            steks.append('(')
        elif i == ')':
            if len(steks) == 0:
                rez ="kļūda"; break
            elif steks.pop() != '(':
                rez ="kļūda"; break
    print("steka iekavu'('= ", steks.count('('))

    if steks.count('(')==0:
        return(rez)
    else:
        rez="kļūda"
    return(rez)

    v1 = "(7,9)"; print("(7,9) =" , parbaudaSteka(v1))
    v1 = "(7,9)"; print("(7,9) =" , parbaudaSteka(v1))
    v1 = "(7,9)"; print("(7,9) =" , parbaudaSteka(v1))
