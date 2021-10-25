"""
Entradas
Horas trabajadas-->int-->H_T
Precio de la hora-->int-->P_h
Salidas
Salario neto-->int-->S_n
"""
#Entradas
P_h=float(input("Precio por cada hora trabajada: "))
H_t=int(input("Numero de horas trabajadas: "))
#Caja negra
S=float((H_t*P_h))
S_n=int((S-S*0.20))
#Salida
print("El salario neto es de:",S_n)




