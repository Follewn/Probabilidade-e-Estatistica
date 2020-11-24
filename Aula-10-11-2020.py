# Ex 8:
'''ano = int(input('Insira seu ano de nascimento: '))
if ano<1900 or ano>2020:
  while True:
    print('Ano inválido!')
    ano = int(input('Insira seu ano de nascimento: '))
    if ano>=1900 and ano<=2020:
      break
if ano<=2004:
  print('Você pode votar!')
else:
  print('Você NÃO pode votar!')'''

# Ex 9:
'''senha = input('Insira sua senha: ')
if senha == '1234':
  print('Acesso permitido!')
else:
  print('Acesso negado!')'''

# Ex 10:
'''qde = int(input('Insira a quantidade de maçãs desejadas: '))
if qde<12:
  print('O valor das', qde, 'maçãs foi R$', qde*.3)
else:
  print('O valor das', qde, 'maçãs foi R$', qde*.25)'''

# Ex 11:
'''num1 = int(input('Insira o primeiro valor inteiro: '))
num2 = int(input('Insira o segundo valor inteiro: '))
num3 = int(input('Insira o terceiro valor inteiro: '))
lista = [num1, num2, num3]
lista.sort()
print('Os valores ordenados são:', lista[0],',', lista[1],'e', lista[2])'''

# Ex 12:
'''sexo = input('Insira o sexo da pessoa (1) Feminino e (2) Masculino: ')
if sexo!='1' and sexo!='2':
  while True:
    print('Sexo inválido!')
    sexo = input('Insira o sexo da pessoa (1) Feminino e (2) Masculino: ')
    if sexo=='1' or sexo=='2':
      break
alt = float(input('Insira a altura da pessoa: '))
if sexo=='1':
  print('O peso ideal dela é', round(62.1*alt-44.7,2), 'kg')
else:
  print('O peso ideal dele é', round(72.7*alt-58,2), 'kg')'''

# Ex 14:
'''num = int(input('Insira um número inteiro: '))
for _ in range(0,11): # A cada iteração, _ será 0,1,2,3,4,5,6,7,8,9,10
  print(num, 'x', _, '=', num*_)'''

# Ex 15:
'''num = int(input('Insira um número inteiro maior que 2: '))
while num<=2:
  print('Número inválido!')
  num = int(input('Insira um número inteiro maior que 2: '))
  if num>2:
    break
# exemplo: num = 8 --> 2+4+6+8 = 20
soma=0
# range(INICIO, FIM+1, PULAR) --> Se quero que pare em 8, 8+1=9
for _ in range(2,num+1,2): # Exemplo --> _ = 2,4,6,8
  soma += _ # soma = soma + _
print('A soma dos valores pares até', num, 'é', soma)
# 1º soma = 0+2 = 2
# 2º soma = 2+4 = 6
# 3º soma = 6+6 = 12
# 4º soma = 12+8 = 20'''

# Ex 16:
'''num = int(input('Insira um número inteiro maior que 1: '))
while num<=1:
  print('Número inválido!')
  num = int(input('Insira um número inteiro maior que 1: '))
  if num>1:
    break
# exemplo: num = 10 --> 1+3+5+7+9 = 25
soma=0
# range(INICIO, FIM+1, PULAR) --> Se quero que pare em 10, 11
for _ in range(1,num+1,2): # Exemplo --> _ = 1,3,5,7,9
  soma += _ # soma = soma + _
print('A soma dos valores impares até', num, 'é', soma)'''

# Ex 17
'''saldo = 0
op = input('Selecione: (a) Saldo, (b) Depósito, (c) Saque e (d) Sair: ')
while True:
  if op == 'd':
    print('Saiu')
    break
  elif op == 'a':
    print('Seu saldo é R$', saldo)
    op = input('\nSelecione: (a) Saldo, (b) Depósito, (c) Saque e (d) Sair: ')
  elif op == 'b':
    dep = float(input('Insira o valor de depósito: R$'))
    print('Depósito efetuado')
    saldo += dep  # saldo = saldo + dep
    op = input('\nSelecione: (a) Saldo, (b) Depósito, (c) Saque e (d) Sair: ')
  elif op == 'c':
    saq = float(input('Insira o valor de saque: R$'))
    if saq > saldo:
      print('Saldo insuficiente!')
    else:
      print('Saque realizado com sucesso')
      saldo -= saq # saldo = saldo - saq
    op = input('\nSelecione: (a) Saldo, (b) Depósito, (c) Saque e (d) Sair: ')
  else:
    print('Opção inválida!')
    op = input('\nSelecione: (a) Saldo, (b) Depósito, (c) Saque e (d) Sair: ')'''

# Comandos estatísticos:
'''import statistics
l1 = [2, 3, 6.5, 7.5, 1.5, 9.5, 0.5, 4, 5.6, 7.2, 0.5, 0.5, 0.5]
MediaSimples = statistics.mean(l1)
print('A média simples é', round(MediaSimples,2))
Variancia = statistics.variance(l1)
print('A variância é', round(Variancia,2))
DesvPa = statistics.stdev(l1)
print('O desvio padrão é', round(DesvPa,2))
CV = (DesvPa/MediaSimples)*100
print('O Coeficiente de Variação é', round(CV,2), '%')
Moda = statistics.mode(l1)
print('A moda é', round(Moda,2))
Mediana = statistics.median(l1)
print('A mediana é', round(Mediana,2))'''

'''from scipy.stats.mstats import gmean
l1 = [2, 3, 6.5, 7.5, 1.5, 9.5, 0.5, 4, 5.6, 7.2, 0.5, 0.5, 0.5]
MediaGeom = gmean(l1)
print('A média geométrica é', round(MediaGeom,2))'''

import statistics
l1 = [2, 3, 6.5, 7.5, 1.5, 9.5, 0.5, 4, 5.6, 7.2, 0.5, 0.5, 0.5]
MediaHarm = statistics.harmonic_mean(l1)
print('A média harmônica é', round(MediaHarm,2))