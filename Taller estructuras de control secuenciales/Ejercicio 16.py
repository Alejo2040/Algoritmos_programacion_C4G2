"""
Entradas
Galones-->int-->G
Salida
Precio-->int-->P
"""
#ENTRTADA
G=int(input("De el numero de galones que quiere surtir: "))
#CAJA NEGRA
P=int((G*3.785)*50000)
#SALIDA
print("El precio de lo que surtio es",P,"COP")