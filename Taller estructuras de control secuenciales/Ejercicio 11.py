"""
Entradas
Nombre-->str-->N
Número de hijos-->int-->H
Horas normales trabajadas-->float-->H_n
Valor de la hora-->float-->V_h
Horas extra trabajadas-->float-->H_e
Salidas
Asignaciones-->float-->A
Deducciones-->float-->D
Sueldo neto-->float-->S_n
"""
#Entradas
N=str(input("Ingrese su nombre: "))
H_n=float(input("Digite las horas normales trabajadas: "))
V_h=float(input("Digite el valor de una hora normal de trabajada: "))
H_e=float(input("Digite las horas extra trabajadas: "))
H=int(input("Digite su numero de hijos: "))
#Caja negra
S_n=float(V_h*H_n)
valor_hx=float(V_h+(V_h*0.25))
S_hx=float(H_e*valor_hx)
S_b=float(S_n+S_hx)
D=float(S_b*0.05+S_b*0.02+S_b*0.07)
A=float(250000+173000*H+180000)
S_n=float(S_b-D+A)
#Salidas
print(N,"sus asignaciones son de:",A,"COP. Sus deducciones son de:",D,"COP.Y su salario neto es de:",S_n,"COP")