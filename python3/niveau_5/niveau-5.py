# -*- coding:latin1 -*
"""
    Christmas tree
    NIVEAU 5
    Robin TURPIN & Tudi MOUGEOT
    17 et 18 décembre 2020
    python 3.7
"""

"""
     Initialisations des constantes :
"""
width=23

"""
    Procédure permettant d'imprimer l'étoile de la mort en haut du sapin, et la centre par rapport au sapin.
"""
def star(n):
    for i in range(n):
        print(("*" + (" " * 4) + "*" + (" " * 4) + "*").center(width))
        print(((" " * 2) + "*" + (" " * 2) + "*" + (" " * 2) + "*"+ (" " * 2)).center(width))
        print(((" " * 5) + "*" + (" " * 5)).center(width))
        print(("*" + " " + "*" + " " + "*" + " " + "*" + " " + "*" + " " + "*").center(width))
        print(((" " * 5) + "*" + (" " * 5)).center(width))
        print(((" " * 2) + "*" + (" " * 2) + "|" + (" " * 2) + "*"+ (" " * 2)).center(width))
        print(("*" + (" " * 4) + "|" + (" " * 4) + "*").center(width))

"""
    Cette procédure permet d'imprimer un sapin à trois étages, et centre le sapin.
    On ne demande pas à l'utilisateur de rentrer le nombre d'étages qu'il veut.
"""
def triangles(t, m, b):
    for size in range(1, t + 1, 2):
        print((size * "*").center(width))
    for size in range(3, 3 + 1, 4):
        print(("0 " + size * "*" + " 0").center(width))
    for size in range(7, m + 1, 4):
        print((size * "*").center(width))
    for size in range(5, 5 + 1, 4):
        print(("0" + ( " " * 4 ) + size * "*" + ( " " * 4 ) + "0").center(width))
    for size in range(11, b + 1, 6):
        print((size * "*").center(width))
"""
    Cette procédure permet d'imprimer la guirlande en bas du sapin.
"""
def tinsel(n):
    for size in range(n):
        print((4 * "| " + 5 * "*" + 4 * " |").center(width))
    for size in range(n):
        print((4 * "0 " + 5 * "*" + 4 * " 0").center(width))

"""
    Cette procédure imprime un tronc à la suite du sapin et le centre par rapport au sapin.
"""
def trunc(n):
    for i in range(n):
        print((5 * "*").center(width))
        
"""
    Programme principal
"""        
def main():        
    star(1)
    triangles(8, 16, 24)
    tinsel(1)
    trunc(1)
main()