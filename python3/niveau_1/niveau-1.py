# -*- coding:latin1 -*
"""
    Christmas tree
    NIVEAU 1
    Robin TURPIN & Tudi MOUGEOT
    17 et 18 décembre 2020
    python 3.7
"""

"""
     Initialisations des constantes :
"""
width=23

"""
    Cette procédure permet d'afficher un sapin à trois étages.
    On ne demande pas à l'utilisateur de rentrer le nombre d'étages qu'il veut.
"""
def triangles(t, m, b):
    for size in range(1, t + 1, 2):
        print((size * "*").center(width))
    for size in range(3, m + 1, 4):
        print((size * "*").center(width))
    for size in range(5, b + 1, 6):
        print((size * "*").center(width))
        
"""
    Programme principal
"""        
def main():
    triangles(8, 16, 24)
main()