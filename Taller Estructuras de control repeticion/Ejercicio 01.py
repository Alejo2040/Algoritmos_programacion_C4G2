"""
Entradas
(K,N)-->int-->numero entero positivo
Salidas
N-->int-->N con el mismo valor de K
"""
#Entradas
K, N=map(int, input("Digite los 2 valores: ").split())
#Caja negra
if K<N:
    while K<=N:
        #Salida 1
        print(N)
        N=N-1
else:
    #Salida 2
    print("Intenta que el primero sea mayor que el segundo ")