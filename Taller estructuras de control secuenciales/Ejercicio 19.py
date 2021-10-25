"""
Entradas:
Cantidad de naranjas--->int--->X
Precio por docena--->float--->Y
Valor venta--->float--->K
Salidas:
Porcentaje de ganancia--->float--->P_g
"""
#Entradas
X=int(input ("Numero de naranjas: "))
Y=float(input ("Valor por docena: "))
K=float(input ("Valor de las ventas: "))
#Caja negra
docena=(X/12)
P=(Y*docena)
ganancia=(K-P)
P_g=((ganancia*100)/P)
#Salida
print("El porcentaje de ganancias es: ",P_g, "%")