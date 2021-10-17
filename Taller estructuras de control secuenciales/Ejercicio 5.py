"""
Entradas
Nota del primer parcial-->int-->a
Nota del segundo parcial-->int-->b
Nota del tercer parcial-->int-->c
Nota del examen final-->int-->d
Nota del trabajo final-->int-->e
Salidas
Calificacion final-->int-->NF
"""
#Entradas
a=int(input("Cual es la nota del primer parcial? "))
b=int(input("Cual es la nota del segundo parcial? "))
c=int(input("Cual es la nota del tercer parcial? "))
d=int(input("Cuales es su nota en el examen final? "))
e=int(input("Cuales es su nota en el trabajo final? "))
#Caja negra
P=float((a+b+c)/3*0.55)
EF=float(d*0.30)
TF=float(e*0.15)
NF=int(P+EF+TF)
#Salida
print("Su nota final es de: ",NF)