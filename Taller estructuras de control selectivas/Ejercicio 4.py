"""
Entradas
Monto de la compra-->float-->M_c
Salidas
Cantida a invertir de los fondos de la empresa -->float-->I
Cantidad a pagar por credito-->float-->C
Cantidad a pagar por intereses-->float-->In
Cantidad que pidio prestada al banco-->float-->P
"""
#Entrada
M_c=float(input("Ingrese el total se su compra: "))
#Caja negra
if(M_c>5000000):
    I=float(M_c-M_c*0.55)
    p=float(M_c-M_c*0.30)
    P=("La cantidad que pidio prestada al banco es de:",p,"COP")
    C=float(M_c-M_c*0.15)
    In=float((M_c-M_c*0.15)*0.30)
else:
    I=float(M_c-M_c*0.70)
    P="No es necesario pedir prestado al banco"
    C=float(M_c-M_c*0.30)
    In=float((M_c-M_c*0.30)*0.20)
#Salida
print("La cantida a invertir de los fondos de la empresa es de",I,"COP")
print("La cantidad a pagar a credito es de",C,"COP")
print("La cantidad a pagar por intereses es de",In,"COP")
print(P)


 