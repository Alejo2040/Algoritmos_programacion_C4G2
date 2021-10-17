"""
Entradas
Capital prestada-->int-->Cp
Razon-->int-->R
Salida
Porcentaje anual-->int-->Pa
"""
#Entradas
C_p=int(input("Digite valor del prestamo: "))
r=int(input("Digite valor de la razon: "))
#Caja negra
Interes_total=float((C_p*4*r)/100)
Interes_anual=float((C_p*1*r)/100)
Pa=int((Interes_anual*100)/Interes_total)
#Salida
print("El porcentaje cobrado anualmente:",Pa,"%")