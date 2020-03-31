'''
6. Faça um programa de rifa (sorteio), o programa deve receber a quantidade total de
#participantes e sortear um número. Lembrando que cada participante recebe um
#cupom (número)
'''

#importando pag random
import  random 
#Entrada número de participantes
numero = int (input('Digite o número de participante do sorteio:'))
#Recebido o número total de participantes percorre do zero até o numero digitado escolhendo 
#aleatoriamente um número final 
escolhido = random.choice(range(0, numero))
print('O número escolhido é:',escolhido)