"""
Entradas
Sueldo base-->float-->Sb
Venta 1-->float-->V1
Venta 2-->float-->V2
Venta 3-->float-->V3
Salidas
comision-->float-->C
Dinero total-->float-->Dt
"""
#Entradas
Sb=float(input("Digite sueldo base: "))
V1=float(input("Digite venta 1: "))
V2=float(input("Digite venta 2: "))
V3=float(input("Digite venta 3: "))
#Caja negra
C=float((V1+V2+V3)*0.10)
Dt=float(Sb+C)
#Salidas
print("Por comisión obtendra:",C, "y el dinero total que recibirá es:",Dt)