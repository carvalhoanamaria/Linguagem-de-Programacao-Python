'''
3. Faça um programa que ordene 
uma lista com 5 valores digitados pelo usuário
'''
#Entrada dos números, podendo ser float 
numero1 = float(input('Primeiro número:'))
numero2 = float(input('Segundo número:'))
numero3 = float(input('Terceiro número:'))
numero4 = float(input('Quarto número:'))
numero5 = float(input('Quinto número:'))

# Armazenamento dos 5 números na lista
Lista=[numero1,numero2,numero3,numero4,numero5]

# Ordenando crecente usando o sorted
print('Os números digitados com suas respectivas ordem crescente são:',sorted(Lista))
# Ordenando crescente usando o sorted juntamente com o reverse como verdadeiro
print('Os números digitados com suas respectivas ordem decrescente são:',sorted(Lista, reverse= True))