"""
Entradas
Examen_math-->int-->E_M
Tareas_math-->int-->T_M
Examen_Fisica-->int-->E_F
Tareas_fisica-->int-->T_F
Examen_quimica-->int-->E_Q
Tareas_quimica-->int-->T_Q
Salidas
Promedio_math-->int-->P_M
Promedio_fisica-->int-->P_F
Promedio_quimica-->int-->P_Q
Promedio_total-->int-->P_T
"""
#Entradas
E_M=int(input("De su calificacion del examen de matematicas: "))
T_M1=int(input("De su calificacion de la primera tarea de matematicas: "))
T_M2=int(input("De su calificacion de la segunda tarea de matematicas: "))
T_M3=int(input("De su calificacion de la tercera tarea de matematicas: "))
E_F=int(input("De su calificacion en el examen de fisica: "))
T_F1=int(input("De su calificacion de la primera tarea de fisica: "))
T_F2=int(input("De su calificacion de la segunda tarea de fisica: "))
E_Q=int(input("De su calificacion en el examen de quimica: "))
T_Q1=int(input("De su calificacion de la primera tarea de quimica: "))
T_Q2=int(input("De su calificacion de la segunda tarea de quimica: "))
T_Q3=int(input("De su calificacion de la tercera tarea de quimica: "))
#Caja negra
x1=float(E_M*0.90)
y1=float(((T_M1+T_M2+T_M3)/3)*0.10)
x2=float(E_F*0.80)
y2=float(((T_F1+T_F2)/2)*0.20)
x3=float(E_Q*0.85)
y3=float(((T_Q1+T_Q2+T_Q3)/3)*0.15)
P_M=int(x1+y1)
P_F=int(x2+y2)
P_Q=int(x3+y3)
P_T=int((P_M+P_F+P_Q)/3)
#Salidas
print("El promedio general de las tres materias es:",P_T)
print("El promedio de matematicas es",P_M,"el de fisica es",P_F,"y el de quimica es de",P_Q)