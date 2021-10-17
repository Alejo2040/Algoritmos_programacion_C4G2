"""
Entradas
Billetes de 50000-->int-->N1
Billetes de 20000-->int-->N2
Billetes de 10000-->int-->N3
Billetes de 5000-->int-->N4
Billetes de 2000-->int-->N5
Billetes de 1000-->int-->N6
Billetes de 500-->int-->N7
Billetes de 100-->int-->N8
Salida
Dinero total del banco-->int-->Dt
"""
#Entrada
N1=int(input("Ingrese los billetes de 50000 "))
N2=int(input("Ingrese los billetes de 20000 "))
N3=int(input("Ingrese los billetes de 10000 "))
N4=int(input("Ingrese los billetes de 5000 "))
N5=int(input("Ingrese los billetes de 2000 "))
N6=int(input("Ingrese los billetes de 1000 "))
N7=int(input("Ingrese los billetes de 500 "))
N8=int(input("Ingrese los billetes de 100 "))
#Caja negra
Dt=int((N1*50000)+(N2*20000)+(N3*10000)+(N4*5000)+(N5*2000)+(N6*1000)+(N7*500)+(N8*100))
#Salida
print("El dinero total del banco es:",Dt)