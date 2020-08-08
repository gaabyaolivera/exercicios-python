#Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.
hora = float(input('Ganhos por hora R$: '))
horasT = float(input('Horas trabalhadas por mês: '))
salario = hora * horasT
print('Você deve receber {} por mês'.format(salario))