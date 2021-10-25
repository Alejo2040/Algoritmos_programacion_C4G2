"""
Entradas
Lectura anterior de la luz-->int-->L_a
Lectura actual de la luz-->int-->L_A
Costo por kilovatio-->int-->C_Kv
Salida
Monto total a pagar-->int-->Mt
"""
#Entradas
L_a=int(input("De la lectura de la luz del anterior mes: "))
L_A=int(input("De la lectura de la luz mes actual: "))
C_kv=int(input("Digite el costo por kilovatio: "))
#Caja negra
Mt=int((L_A-L_a)*C_kv)
#Salidas
print("EL monto total a pagar en un mes de luz es:",Mt)