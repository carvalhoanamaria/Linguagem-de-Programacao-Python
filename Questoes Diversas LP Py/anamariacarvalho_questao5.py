'''
5. Faça um programa que imprima os 1000 primeiros números inteiros
'''

#O conjunto dos números inteiros é formado por todos os números que não são decimais. Em outras palavras,
#  o conjunto dos números inteiros é formado pelo conjunto dos números naturais e seus opostos aditivos.
#Sendo o numero 0 um numero neutro.

#Os primeiros numeros inteiros positivos +1 ao +1000
# No laço i recebe 1, percorrendo até o 1000 em seguida imprime lado a lado 
for i in range(1,1000 +1):
    print('[{}]'.format(i), end='')