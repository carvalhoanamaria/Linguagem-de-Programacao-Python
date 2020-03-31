'''
2. Faça um programa que leia 1 valor e 
identifique se este número é número primo,repita isso até que usuário digite 0 (zero).
'''
# É classificado como número primo os números divisiveis por 1 e por ele mesmo, 
# ou seja apenas duas vezes.

# Entrada do numero
numero = int(input('Digite um número: '))
# Contagem iniciada do zero
cont = 0
#Laço iniciando do 1 
#enquanto o resto da divisao do numero não corresponder a zero 
#o lanço continua e vai contando
for i in range(1, numero + 1):
    if numero % i == 0:
        cont += 1

print('O número {} é divisivel {} vezes.'.format(numero, cont))
# Se a contagem foi igual a 2 vezes é primo, se não não é primo
if cont == 2:
    print('O número é primo')
else:
    print('O número não é primo')

