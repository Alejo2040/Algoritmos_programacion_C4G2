"""
Entradas
Salario bruto-->float-->S_b
Categoria-->int-->C
Aumento-->float-->A
"""
#Entrada
S_b=float(input("Digite el salario bruto: "))
#Caja negra
if(S_b>=5000000):
    C="1"
    A=S_b*0.10+S_b
elif(S_b>=4300000 and S_b<5000000):
    C="2"
    A=S_b*0.15+S_b
elif(S_b>=3600000 and S_b<4300000):
    C="3"
    A=S_b*0.20+S_b
elif(S_b>=2000000 and S_b<3600000):
    C="4"
    A=S_b*0.40+S_b
elif(S_b>=900000 and S_b<2000000):
    C="5"
    A=S_b*0.60+S_b
else:
    C="No se ha detectado ninguna categoria :("
    A="No se ha detectado ningun aumento :c"
#Salida
print("La categoria es:",C)
print("el aumento es de",A)