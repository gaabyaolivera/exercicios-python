#Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius.
fa = float(input('Temperatura em F°: '))
conversão = 5 * ((fa - 32) / 9)
print('A temperatura em C° é {:.2f}'.format(conversão))
