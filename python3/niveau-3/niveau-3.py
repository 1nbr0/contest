"""
    Christmas tree
    NIVEAU 3
    Robin TURPIN & Tudi MOUGEOT
    17 et 18 décembre 2020
    python 3.7
"""
width=24

def triangle1(n):
    for size in range(1, n + 1, 2):
        print((size * "*").center(width))

def triangle2(n):
    for size in range(3, n + 1, 4):
        print((size * "*").center(width))
        
def triangle3(n):
    for size in range(5, n + 1, 6):
        print((size * "*").center(width))

def tinsel(n):
    for size in range(n):
        print((4 * "| " + 5 * "*" + 4 * " |").center(width))
    for size in range(n):
        print((4 * "0 " + 5 * "*" + 4 * " 0").center(width))

def trunc(n):
    for size in range(n):
        print((5 * "*").center(width))

triangle1(8)
triangle2(16)
triangle3(24)
tinsel(1)
trunc(1)