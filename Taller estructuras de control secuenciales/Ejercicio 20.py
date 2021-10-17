"""
Entradas
Precio de compra-->int-->PC
Salidas
Porcentaje por cuota-->int-->Pc
"""
#Entrada
PC=int(input("Digite el precio de la compra: "))
#Caja negra
Pc=float(((PC/12)*100)/PC)
#Salida
print("El porcentaje que se cobra por el recargo en el pago del computador por cuota es:",Pc,"%")