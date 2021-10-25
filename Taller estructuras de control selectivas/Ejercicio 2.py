"""
Entrada
Salario bruto-->float-->S_b
Salida
Salario neto-->float-->S_n
"""
#Entradas
S_b=float(input("Digite el salario bruto: "))
#Caja negra
if(S_b<900000):
    S_n=S_b+S_b*0.15
else:
    S_n=S_b+S_b*0.12
#Salida
print("EL salario neto es de:",S_n)