"""
Entradas
cantidad invertida-->int-->C_i
Tasa de interes-->float-->T_i
Salida
Saldo-->float-->S
"""
#Entrada
C_i=float(input("Cantidad a invertir: "))
T_i=float(input("Tasa de interes: "))
#Caja negra
x=C_i*T_i
if x>100_000:
    print("la cantidad generada por concepto de interes es:",x, "supera los 100000")
else:
    print("la cantidad generada por concepto de interes es de:",x, "no supera los 100000")
#Salida
print("Saldo de la cuenta:",C_i+x )