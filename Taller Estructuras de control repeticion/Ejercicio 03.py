"""
Entrada 
No hay
Salida
Sumatoria de los números dentro del rango dado-->
"""
#Caja negra
a=0
for i in range(97, 1003):
  if(i % 2 == 0):
    a = a+i
#Salidas
print(a)