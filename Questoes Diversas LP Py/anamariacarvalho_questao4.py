'''
4. Faça um programa que leia receba 3 valores e imprima o maior deles
'''
#Entrada dos valores
valor1 = float(input('Primeiro valor:')) 
valor2 = float(input('Segundo valor:'))
valor3 = float(input('Terceiro valor:'))
#Armazenamento dos valores em lista
lista = [valor1,valor2,valor3]

maior = max(lista)
menor = min(lista)

print('O maior valor digitado é {} e o menor valor digitado é {}'.format(maior,menor,))
