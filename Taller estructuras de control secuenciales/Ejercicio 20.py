"""
Entradas
Precio de compra-->int-->P
Cuota mensual-->int-->T
Salidas
Porcentaje por cuota-->int-->Pc
"""
#Entrada
P=float(input("Digite el precio de la compra: "))
T=float(input ("Valor de la cuota mensual: "))
#Caja negra
Pc=float(T*12)
Cuota=float(Pc-P)
Pr=int((Cuota*100)/P)
#Salida
print("El porcentaje que se cobra por el recargo en el pago del computador por cuota es:",Pr,"%")