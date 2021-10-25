"""
Entradas
Valores-->int-->P,Q
Salida
Satisface la expresion-->int-->SI
No satisface la expresion-->str-->NO
"""
#Entrada
x=input("Ingrese las valores enteros: ")
(P,Q)=x.split(" ")
P=int(P)
Q=int(Q)
#Caja negra
if P**3+Q**4-2*P**2>680:
    S="Los valores "+ str(P),"y", str(Q),"satisfacen la expresion"
else:
    S="Los valores "+ str(P),"y",str(Q),"no satisfacen la expresion"
#Salida
print(S)