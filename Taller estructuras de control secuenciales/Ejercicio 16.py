"""
Entradas
Galones-->int-->G
Salida
Precio-->int-->P
"""
#Entrada
G=int(input("De el numero de galones que quiere surtir: "))
#Caja negra
P=int((G*3.785)*50000)
#Salida
print("El precio de lo que surtio es",P,"COP")