'''print('a'=='a')
print(2.000000001 == 2)
print(3>=3)
print(9>5>4>1>=1)
print(9>5 and 5>4 and 4>1 and 1>=1)
print(9>5 or 1>2)
print(not(9>5 or 1>2))
print(not(not(9>5 or 1>2)))'''

'''fome = False
if fome:
  print('Comida!')
else:
  print('Sem comida')'''

'''Nota = input('Insira a nota: ')
Nota = float(Nota)
if Nota<0 or Nota>10:
  print('Nota errada!')
elif Nota<5:  # elif = else if
  print('Reprovado!')
else:
  print('Aprovado!')'''

frase = 'Meu carro não liga de manhã'
palavra = 'moto'
if palavra in frase:
  print('A palavra ' + palavra + ' está presente')
else:
  print('A palavra ' + palavra + ' está ausente')