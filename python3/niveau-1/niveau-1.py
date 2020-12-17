"""
    Christmas tree
    NIVEAU 1
    Robin TURPIN & Tudi MOUGEOT
    17 et 18 décembre 2020
    python 3.7
"""

def triangle1(n, width):
    for size in range(1, n + 1, 2):
        print((size * "*").center(width))

def triangle2(n, width):
    for size in range(3, n + 1, 4):
        print((size * "*").center(width))
        
def triangle3(n, width):
    for size in range(5, n + 1, 6):
        print((size * "*").center(width))

triangle1(8, 24)
triangle2(16, 24)
triangle3(24, 24)
