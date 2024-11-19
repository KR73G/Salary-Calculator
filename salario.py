#Calculadora de Salario

nombre_del_empleado = str(input("ingresa nombre del empleado: "))
salario_por_dia = float(input("Ingresa su salario por dia: "))
dias_trabajados = int(input("Ingresa los dias trabajados: "))
salario = salario_por_dia * dias_trabajados

print(f"El salario de {nombre_del_empleado}")
print(f"Es de {salario}")

