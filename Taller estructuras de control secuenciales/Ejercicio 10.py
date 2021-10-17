"""
Entradas
Chelines austriacos-->float-->C_a
Dracmas griegos-->float-->D_g
Pesetas-->float-->P
Salidas
Pesetas-->float-->P_a
Francos franceses-->float-->F_f
Dolares-->float-->D
Liras italianas-->float-->L_i
"""
#Entradas
C_a=float(input("Ingrese los chelines que desee imprimir: "))
D_g=float(input("Ingrese las dracmas que desee imprimir: "))
P=float(input("Ingrese las pesetas que desee imprimir: "))
#Caja negra
P_a=float(C_a*9568.51)
F_f=float((D_g*886.07)/20110)
D=float(P*122499)
L_i=float(P*92.89)
#Salidas
print("Los",C_a,"chelines equivalen a:",P_a,"pesetas")
print("Las",D_g,"dracmas equivalen a:",F_f,"francos franceses")
print("Las",P,"pesetas equivalen a:",D,"dolares y a",L_i,"liras")
