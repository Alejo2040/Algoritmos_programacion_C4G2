"""
Entradas
primer lado-->int-->a
segundo lado-->int-->b
tercer lado-->int-->c
Salidas
Area-->float-->A
"""
#Entradas
a=float(input("Digite el primer lado: "))
b=float(input("Digite el segundo lado: "))
c=float(input("Digite el tercer lado: "))
#Caja negra
s=float((a+b+c)/2)
A=float((s*(s-a)*(s-b)*(s-c))**0.5)
#Salida
print("El area es:",A)