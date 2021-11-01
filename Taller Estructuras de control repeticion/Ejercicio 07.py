"""
Entradas
(X,M)-->int-->valores
Salida
Nueva experiencia Monster-->int-->E
"""
#Caja negra 1
while True:
    #Entrada
    X  , M= input().split()
    #Caja negra 2
    if(X=='0' and M=='0'):
        break
    #Salida
    print(int(X)*int(M))