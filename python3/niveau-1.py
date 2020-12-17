"""
    Christmas tree
    NIVEAU 1
    Robin TURPIN & Tudi MOUGEOT
    17 et 18 décembre 2020
    python 3.7
"""
"""
for level in range(4): # répéter n fois
    for size in range(1, 6): # taille de notre sapin
        print(size * "*")

"""
"""
def triangle1(n):
    for size in range(3, n+1):
        print(size * "*")
        
def triangle2(n):
    for size in range(3, n+1):
        print(size * "*")

def triangle3(n):
    for size in range(3, n+1):
        print(size * "*")
    
for i in range(1, 7):
    triangle1(i)
    triangle2(i)
    triangle3(i)
"""

def triangle1(n):
    for size in range(1, n + 1, 2):
        print((size * "*").center(n))

triangle1(5)
