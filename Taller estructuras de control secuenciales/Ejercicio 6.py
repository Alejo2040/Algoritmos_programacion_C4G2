"""
Entradas
numero_hombres-->int-->p_h
numero_mujeres-->int-->p_m
Salidas
Porcentaje de hombres-->float-->p_h
Porcentaje de mujeres-->float-->p_m
"""

numero_hombres=int(input("digite total de hombres: "))
numero_mujeres=int(input("digite total de mujeres: "))
#caja negra
p_h=numero_hombres*100/(numero_hombres+numero_mujeres)#float
p_m=numero_mujeres*100/(numero_hombres+numero_mujeres)#float
#salida
print("porcentaje de hombres:", p_h, "y el porcentaje de mujeres: ",p_m)