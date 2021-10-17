"""
Entradas
Precio final-->int-->Pf
Precio al publico-->int-->PvP
Salidas
Da-->int-->Descuento aplicado
"""
#Entradas
Pf=int(input("Digite el precio final:"))
PvP=int(input("Digite el precio de venta al publico:"))
#Caja negra
Pd=int(Pf-PvP)
Da=int((Pd*100)/Pf)
#Salidas
print("El descuento que se le aplica a la compra es de:",Da,"%")
