# -*- coding:latin1 -*
"""
    Christmas tree
    NIVEAU 2
    Robin TURPIN & Tudi MOUGEOT
    17 et 18 d�cembre 2020
    python 3.7
"""

"""
     Initialisations des constantes :
"""
width=23

"""
    Cette proc�dure permet d'imprimer un sapin � trois �tages, et centre le sapin.
    On ne demande pas � l'utilisateur de rentrer le nombre d'�tages qu'il veut.
"""
def triangles(t, m, b):
    for size in range(1, t + 1, 2):
        print((size * "*").center(width))
    for size in range(3, m + 1, 4):
        print((size * "*").center(width))
    for size in range(5, b + 1, 6):
        print((size * "*").center(width))
"""
    Cette proc�dure imprime un tronc � la suite du sapin et le centre par rapport au sapin.
"""
def trunc(n):
    for size in range(n):
        print((5 * "*").center(width))
        
"""
    Programme principal
"""
def main():
    triangles(8, 16, 24)
    trunc(3)
main()