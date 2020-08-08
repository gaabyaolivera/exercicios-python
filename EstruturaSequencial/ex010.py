#Faça um Programa que peça a temperatura em graus Celsius,
#transforme e mostre em graus Farenheit.
c = float(input('Digite uma temperatura em C°: '))
conversão = c * 1.8 + 32
print('A temperatura em F° é {}'.format(conversão))