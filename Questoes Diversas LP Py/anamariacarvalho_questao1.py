'''
1. Faça um programa que leia 3 notas,
  calcule e imprima a média aritmética deles.
'''
# Média é a soma das notas dividido pela quantidade
#Entrada das três notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terceira nota:'))
#Calculo da média das três notas
média = (nota1 + nota2 + nota3) /3
# Saida do resultado
print('A média entre as notas {} , {} e {} é  {}'.format(nota1,nota2,nota3,média))
