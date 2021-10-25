"""
Entradas
número total de hot dogs consumidos-->int-->A
número total de participantes-->int-->B
Salida
promedio de perritos calientes consumidos--> -->P_r
"""
#Entradas
M=input().split(" ")
A=int(M[0])
B=int(M[1])
#Caja negra
P_r=float(A/B)
P=round(P_r,2)
#Salida
print(P)


