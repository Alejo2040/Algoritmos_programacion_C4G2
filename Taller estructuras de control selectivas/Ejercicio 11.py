"""
Entradas
temperatura-->float-->Tmp
Salidas
deporte-->str-->D
"""
Tmp=float(input("Digite la temperatura: "))
#Caja negra
D=""
if(Tmp>85):
    D="Natacion"
elif(Tmp>=71.0 and Tmp<=85.9):
    D="Tenis"
elif(Tmp>=33.0 and Tmp<=70.9):
    D="Golf"
elif(Tmp>=11.0 and Tmp<=32.9):
    D="Esquí"
elif(Tmp<=10):
    D="Marcha"
else:
    D="No se ha reconocido ningun deporte :c"
#Salida
print(D)