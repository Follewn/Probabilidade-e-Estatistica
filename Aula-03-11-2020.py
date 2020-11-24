'''alunos = []
Qde = int(input('Insira a quantidade de alunos: '))
for _ in range(1,Qde+1):
  novo_aluno = input('Insira o nome do aluno '+ str(_) + ': ')
  alunos.append(novo_aluno)
print('Os alunos são:', alunos)
for _ in alunos:
  nota = float(input('Insira a nota do aluno ' + _ + ': '))
  if nota<0 or nota>10:
    while True:
      print('Nota INVÁLIDA!, Insira uma nota entre 0 e 10!')
      nota = float(input('Insira a nota do aluno ' + _ + ': '))
      if nota>=0 and nota<=10:
        break
  if nota<5:
    print('Aluno ' + _ + ' REPROVADO')
  else:
    print('Aluno ' + _ + ' APROVADO')'''

'''x = 4
while x < 7:
  print(x)
  x += 1''' # x = x + 1
# Antes da 1º: x = 4
# 1º x=4<7? Sim --> print(4); x=5
# 2º x=5<7? Sim --> print(5); x=6
# 3º x=6<7? Sim --> print(6); x=7
# 4º x=7<7? Não --> FIM

'''x = 4
while True: # No lugar do True posso colocar qq comparação verdadeira
  print(x)
  x += 1
  if x == 7:
    break'''
# Antes da 1º: x = 4
# 1º print(4); x=5; x=5 == 7? Não
# 2º print(5); x=6; x=6 == 7? Não
# 3º print(6); x=7; x=7 == 7? Sim --> break

'''X = range(1,8,2) # --> Começa em 1, termina em 7, pula de 2 em 2
# 1, 3, 5, 7
print(list(X))'''

'''cont = 0
palavra = 'Mississipi'
for _ in palavra:
  print('A letra ' + _ + ' está na posição', cont)
  cont += 1  # cont = cont + 1'''

'''palavra = 'Mississipi'
for x,y in enumerate(palavra):
  print('A letra ' + y + ' está na posição', x)'''

'''lista = ['a', 4, 8.5, 'c', 34, 'faca']
for x,y in enumerate(lista):
  print('Valor:', y, 'Posição:', x)'''

'''l1 = ['a1', 'a2', 'a3', 'a4']
l2 = [2.5, 5.6, 4.5, 6.5]
l3 = ['Matutino', 'Matutino', 'Noturno', 'Matutino']
for x,y,z in zip(l1,l2,l3):
  print('O aluno', x, 'tem a nota', y, 'e estuda no período', z)'''

'''lista = ['a', 'b', 'c', 6, 8, [1, 2], 'a', 3, 6, 8, 6, 'c']
print([1, 2] in lista)
print(lista.count(8))'''

'''d1 = {2:'b', 5:75, 'x':9.6}
print('x' in d1.keys())
print(9.7 in d1.values())'''

'''l1 = [5, 1, 36.65, 42, 12, 9, 14, 45, 21, 20.5]
print('O maior valor é', max(l1), 'O maior valor é', min(l1))'''

'''from random import shuffle
l1 = [5, 1, 36.65, 42, 12, 9, 14, 45, 21, 20.5]
l2 = l1
l2.sort()
print('A lista ordenada crescente:', l2)
l3 = l1
shuffle(l3)
print('A lista aleatória:', l3)'''

'''from random import randint
numero_aleatorio = randint(0,10)
print(numero_aleatorio)'''

# Demonstre em X iterações (inseridas pelo usuário) que uma
# moeda tem probabilidade de dar coroa 0,5 e cara também 0,5
'''X = int(input('Insira a quantidade de lançamentos de moeda: '))
cara = 0
coroa = 0
for _ in range(1,X+1):
  sorteio = randint(0,1)
  if sorteio == 0:
    cara += 1 # cara = cara +1
  else:
    coroa += 1
print('A probabilidade de cara é: ', round(cara/X,3))
print('A probabilidade de coroa é: ', round(coroa/X,3))'''

# Demonstre em X iterações (inseridas pelo usuário) que uma
# moeda tem probabilidade de dar coroa 0,5 e cara também 0,5
'''X = int(input('Insira a quantidade de lançamentos de moeda: '))
moeda = [0]*2  # --> [0, 0]
for _ in range(1,X+1):
  sorteio = randint(0,1)
  moeda[sorteio] += 1
print('A probabilidade de cara é: ', round(moeda[0]/X,3))
print('A probabilidade de coroa é: ', round(moeda[1]/X,3))'''

'''X = int(input('Insira a quantidade de lançamentos de dado: '))
dado = [0]*6 # retorna uma lista preenchida com: [0, 0, 0, 0, 0, 0]
for _ in range(1,X+1):
  sorteio = randint(0,5) # 0 representa dado=1, até 5 representa dado=6
  dado[sorteio] += 1 # dado[0] = dado[0] +1
print('A probabilidade de UM é: ', round(dado[0]/X,3))
print('A probabilidade de DOIS é: ', round(dado[1]/X,3))
print('A probabilidade de TRÊS é: ', round(dado[2]/X,3))
print('A probabilidade de QUATRO é: ', round(dado[3]/X,3))
print('A probabilidade de CINCO é: ', round(dado[4]/X,3))
print('A probabilidade de SEIS é: ', round(dado[5]/X,3))
print(dado)'''

'''import random
print(random.uniform(1,1.001))'''

'''import random
lista = []
for _ in range(1,11):
  lista.append(round(random.uniform(1,2),2))
print(lista)'''

'''palavra = 'Mississipi'
lista = []
for _ in palavra:
  lista.append(_)
print(lista)
lista2 = list(palavra)
print(lista2)
lista3 = [_ for _ in palavra]
print(lista3)'''

# Crie uma lista entre 1 e 10 contendo o quadrado do número
# Ou seja: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''lista = [_*_ for _ in range(1,11)] # range entre 1 e 10
print(lista)'''

#Ex 1, Slide 22:
'''ano = int(input('Insira quantos anos você tem: '))
mes = int(input('Insira quantos meses completos se passaram desde seu niver: '))
dia = int(input('Insira quantos dias se passaram desde o dia que voce faz aniversário nesse mês: '))
print('Sua idade em dias é:', ano*365+mes*30+dia)'''

#Ex 3, Slide 22:
'''saldo = float(input('Insira seu saldo: '))
print('Saldo reajustado em 1% é:', saldo*1.01)'''

#Ex 4, Slide 22:
'''ipi = float(input('Insira a porcentagem do IPI (entre 0 e 100): '))
valor1 = float(input('Insira o valor da peça 1: R$ '))
qde1 = int(input('Insira quantas peças 1 serão vendidas: '))
valor2 = float(input('Insira o valor da peça 2: R$ '))
qde2 = int(input('Insira quantas peças 2 serão vendidas: '))
print('O valor total é: R$', round((valor1*qde1 + valor2*qde2)*(ipi/100+1),2))'''

# Ex5, slide 22
'''sal = float(input('Insira seu salário: R$'))
print('Você ganha', round(sal/1045,2), 'salários mínimos!')'''

# Ex6, slide 22
'''num = int(input('Insira um número inteiro: '))
print('O sucessor é', num+1, 'o antecessor é:', num-1,)'''

# Ex7, slide 23
num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))
print('O maior número é:', max(num1,num2))