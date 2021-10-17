"""
Entradas
Monto presupuestado-->int-->M_p
Salidas
Ginecologia-->int-->G
Traumatologia y Pediatria-->int-->T_P
"""
#Entrada
M_p=int(input("Digite el monto presupuestado:"))
#Caja negra
G=int(M_p*0.40)
T_P=int(M_p*0.30)
#Salida
print("La cantidad de dinero que recibira el area de ginecologia es:",G)
print("La cantidad de dinero que recibiran el area de Traumatologia y el de Pediatria es:",T_P)