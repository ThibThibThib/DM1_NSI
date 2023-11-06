def indice_max(tab, ind):
    '''
    SPECIFICATION
    Docstring
    Cette fonction détermine et retourne le plus grand indice de la valeur tab[ind].
    : param tab : (list)
    : param ind : (int)
    : return (int)
    Elle retournera un nombre entier
    : CU : tab est un tableau de nombres  (condition d'utilisation)
    : CU : ind est un entier naturel inféreur à l'indice maximum du tableau tab
    Doctest
    >>> indice_max([5,4,1,8,4,6],1)
    4
    >>> indice_max([5,4,1,8,4,6],0)
    0
    >>> indice_max([7,0,7,5,4,1,8,0,7,4,6],0)
    8
    '''
    ind_grand = ind
    for i in range(ind, len(tab)):
        if tab[i] == tab[ind]:
            ind_grand = i
    return ind_grand

    
def sans_doublon(tab):
    '''
    SPECIFICATION
    Docstring
    Cette fonction qui appellera indice_max() doit retourner les valeurs de tab sans doublon.
    : param tab : (list)
    : return (list)
    Elle retournera un nombre entier
    : CU : tab est un tableau de nombres  (condition d'utilisation)

    Doctest
    >>> sans_doublon([5,4,1,8,4,6])
    [5, 1, 8, 4, 6]
    >>> sans_doublon([5,4,1,8,4,6,1,8])
    [5, 4, 6, 1, 8]
    '''
    tab_2 = []
    for g in range(len(tab)):
        index = g
        index_doublon = indice_max(tab, index)
        if index == index_doublon:
            tab_2.append(tab[index])
    return tab_2
    


#######################
# PROGRAMME PRINCIPAL #
#######################           
from random import randint

tab=[]
note = 0
for ind in range (5):
    premier_tirage_nb = randint(1,9)
    deuxieme_tirage_nb = randint(1,9)
    calcul = premier_tirage_nb * deuxieme_tirage_nb
    print(premier_tirage_nb, "x", deuxieme_tirage_nb,"=")
    demande = int(input())
    if demande == calcul:
        print("Bravo")
        note = note + 1
    else:
        if premier_tirage_nb == deuxieme_tirage_nb:
            print("Révise tes tables de multiplications par : ", premier_tirage_nb)
        else :
            print("Révise tes tables de multiplications par" , premier_tirage_nb , "et par" , deuxieme_tirage_nb)
        print(premier_tirage_nb , "x" , deuxieme_tirage_nb , "=" , calcul)
        tab.append(premier_tirage_nb)
        tab.append(deuxieme_tirage_nb)
print("Vous avez obtenu :", note,"/ 5")

if note == 5:
    print("Très bien")
else :
    sans_doublon(tab)  


import doctest
doctest.testmod(verbose=True)
