'''
7. Faça um programa que receba a umidade relativa do ar e informe os cuidados a
serem tomados, de acordo com a seguinte tabela (Fonte: wikipedia):
● Entre 20 e 30% - Estado de Atenção
○ Evitar exercícios físicos ao ar livre entre 11 e 15 horas
○ Umidificar o ambiente através de vaporizadores, toalhas
molhadas, recipientes com água,
○ Sempre que possível permanecer em locais protegidos do sol,
em áreas vegetadas etc.
○ Consumir água à vontade.
● Entre 12 e 20% - Estado de Alerta
○ Suprimir exercícios físicos e trabalhos ao ar livre entre 10 e 16
horas
○ Evitar aglomerações em ambientes fechados
○ Usar soro fisiológico para as narinas e lubrificantes para os
olhos
● Abaixo de 12% - Estado de emergência
○ Determinar a interrupção de qualquer atividade ao ar livre entre
10 e 16 horas como aulas de Educação Física
○ Determinar a suspensão de atividades que exijam
aglomerações de pessoas em recintos fechados
○ Durante as tardes, manter com umidade os ambientes internos,
principalmente ambientes onde há crianças e idosos
○ Usar soro fisiológico para as narinas e lubrificantes para os
olhos
'''


umidade = int(input('Quanto está a umidade nesse momento?'))
if umidade >= 20 and umidade <=30 : 
    print('\033[1;35m Entre 20 e 30 - Estado de Atenção')
    print('\033[1;97m \n ○ Evitar exercícios físicos ao ar livre entre 11 e 15 horas. \n ○ Umidificar o ambiente através de vaporizadores, toalhas molhadas, recipientes com água. \n ○ Sempre que possível permanecer em locais protegidos do sol,em áreas vegetadas etc. \n ○ Consumir água à vontade.' )
elif umidade >=12 and umidade <= 20 :  
    print('\033[1;93m Entre 12 e 20 - Estado de Alerta')
    print('\033[1;97m \n ○ Suprimir exercícios físicos e trabalhos ao ar livre entre 10 e 16 horas. \n ○ Evitar aglomerações em ambientes fechados. \n ○ Usar soro fisiológico para as narinas e lubrificantes para os olhos.')
elif umidade < 12:
    print('\033[31m Abaixo de 12 - Estado de emergência')
    print('\033[1;97m \n ○ Determinar a interrupção de qualquer atividade ao ar livre entre 10 e 16 horas como aulas de Educação Física \n ○ Determinar a suspensão de atividades que exijam aglomerações de pessoas em recintos fechados. \n ○ Durante as tardes, manter com umidade os ambientes internos, principalmente ambientes onde há crianças e idosos. \n ○ Usar soro fisiológico para as narinas e lubrificantes para os olhos.')
else:
   print('Umidade incorreta, tente novamente')
