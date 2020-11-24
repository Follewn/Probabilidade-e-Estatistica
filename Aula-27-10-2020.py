'''str1 = 'abcdefghijk'
letra = 'g'
if letra in str1:
  print('A letra ' + letra + ' está dentro de ' + str1)
else:
  print('A letra ' + letra + ' não está dentro de ' + str1)'''

'''l1 = [2, 4, 6, 8, 10]
num = 10
if num in l1:
  print('O número', num, 'está dentro de', l1)
else:
  print('O númer', num, 'não está dentro de', l1)'''

'''l2 = [84, 34, 16, 74, 19]
for _ in l2:
  print(_)'''

'''str1 = 'abcdefghijk'
for _ in str1:
  print(_+'001')'''

'''l2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
soma=0
for _ in l2:
  if _ % 2 == 0: 
    print('O número', _, 'é par')
  else:
    print('O número', _, 'é impar')
  soma = soma + _ # 1° soma = 2; 2º soma = 5; 3º soma = 9
print('A soma total da lista é:', soma)'''

'''lista = [(5,1,3), (4,9,2), (7,14,19), (41,95,61)]
for x, y, z in lista:
  print(x*2, y*3, z*4)'''

'''dic1 = {'a':5, 'b':10, 'c':15}
for _ in dic1:
  print(_)
print('---------')
for _ in dic1.values():
  print(_)
print('---------')
for x,y in dic1.items():
  print('A chave é:', x, 'O valor é:', y)'''

'''posicoes = range(4, 17, 3) # range(INICIAL, FINAL+1, AUMENTO)
print(list(posicoes))'''

'''lista = ['a', 'b', 'c', 'd', 'e']
for _ in range(1, len(lista)): # range: 1, 2, 3, 4
  print(lista[_])'''

'''lista = ['moto X', 5000, 'carro Y', 35000, 'lancha z', 5000]
for _ in range(0,len(lista),2):
  print(lista[_])'''

'''for a in range(3,5):
  for b in range(0,a):
    print(a*b)'''
# 1º do for de a --> a=3
#   1º do for de b --> b=0 --> print(0)
#   2º do for de b --> b=1 --> print(3)
#   3º do for de b --> b=2 --> print(6)
# 2º do for de a --> a=4
#   1º do for de b --> b=0 --> print(0)
#   2º do for de b --> b=1 --> print(4)
#   3º do for de b --> b=2 --> print(8)
#   4° do for de b --> b=3 --> print(12)'''

'''str1 = 'Mississipi é um rio'
for _ in str1:
  if _ == 'p':
    break
  print(_)'''

'''str1 = 'Mississipi é um rio'
for _ in str1:
  if _ == 's' or _ =='i':
    continue
  print(_)
  print('Não caiu no Continue')'''

'''lista = list(range(1,11)) # --> [1, 2, ..., 9, 10]
for _ in lista:
  if _ % 2 == 0:
    print('O número', _, 'é par')
  elif _ % 3 == 0:
    print('O número', _, 'é múltiplo de 3')
  else:
    pass
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''

# Multiplicar 2 valores vizinhos a cada iteração
'''lista = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for _ in range(0,len(lista)-1): # range --> 0 até 6
  mult = lista[_]*lista[_+1]
  print('A multiplicação de', lista[_], 'vezes', lista[_+1], 'é:', mult)'''

# 1º _=0; mult = 10*11 = 110
# 2º _=1; mult = 11*12
# 3º _=2; mult = 12*13

'''x = 4
while x<7:
  print(x)
  x+=1 # --> x = x + 1
print('-------')'''

'''y = 4
while True:
  print(y)
  y+=1 # --> y = y + 1
  if y!=7:
    break'''
# Inicialmente y = 4
# While True:
# 1º print(4) ; y = 5; Por acaso 5 é diferente de 7?

'''y = 4
while y!=7:
  print(y)
  y+=1 # --> y = y + 1'''

'''alunos = ['a1', 'a2', 'a3', 'a4']
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

'''alunos = []
Qde = int(input('Insira a quantidade de alunos: '))
for _ in range(1,Qde+1):
  novo_aluno = input('Insira o nome do aluno '+ str(_) + ': ')
  alunos.append(novo_aluno)
print(alunos)
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

str1 = 'abcdefghijk'
for x,y in enumerate(str1):
  print(x,y)