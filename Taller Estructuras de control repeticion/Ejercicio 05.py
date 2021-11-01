"""
Salidas
Valores de k antes de que la sumatoria de los más cercano a 1000
"""
k=1
A=0
B=0
#Caja negra
print()
while(A<=1000):
    A=((k**2)+1)/k
    k=k+1
    B=B+1
    if A>=1000:
        A=((k**2)+1)/k
        k=k+1
        B=B-1
        break
    #salida
    print (B)