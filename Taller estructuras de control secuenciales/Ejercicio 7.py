"""
Entradas
Metros-->float-->m
Salidas
Pies-->float-->Pi
Pulgadas-->float-->Pu
"""
#Entrada
m=int(input("Ingrese los metros que quiera convertir: "))
#Caja negra
Pi=int(m*39.27)
Pu=int(Pi*12)
#Salida
print("los",m,"metros esquivalen a " ,Pi,"Pies y",Pu, "Pulgadas")
