''' L1 = ['Teste1', 10, 5, [11, 13, 17] ]
L1[1] = L1[1] * L1[2]
print(L1)
print(L1[3][1])
L1.append(L1[1] + L1[3][0])
print(L1)'''

''' L2 = ['Teste3', 10, 5, [11, 13, 17] ]
print(L2[0][2].upper()) # Letra s em maiúscula
X = int(L2[0][-1]) * L2[2]
print(X) '''

'''L4 = ['Teste3', 10, 5, 'H', 94, 'H', [5, 77.4] ]
print(L4.index('H'))'''

'''L5 = [9, 7, 14, 7, 14, 9, 10, 13, 7, 7, 7, 9, 10]
print(L5.count(7))
Txt = 'Casa casa moto casa copo moto que de casa que de casamento'
Txt = Txt.lower()
print(Txt)
print(Txt.count('casa '))'''

'''x = 3
L6 = [9, 'Um', 7, 7.5, 9, 10]
print(L6[x+2*-1])
print(L6[x*x-5])'''

'''L7 = [55, 6, 94, -5, 6, -45, 16.5, -3.6, 12.1, -4.6, .9]
print(len(L7))
L7.sort()
print(L7)'''

'''L8 = ['casa', 'moto', 'mata', 'caso', 'mico', 'avião', 'aviao', 'ave']
L8.sort()
print(L8)'''

'''L9 = [55, 6, 94, -5, 6, -45, 16.5, -3.6, 12.1, -4.6, .9]
L9.reverse()
print(L9)
L10 = ['casa', 'moto', 'mata', 'caso', 'mico', 'avião', 'ave']
L10.reverse()
print(L10)'''

'''L11 = [55, 6, 94, -5, 6, -45, 16.5, -3.6, 12.1, -4.6, .9]
L11.sort()
print(L11)
L11.reverse()
print(L11)'''

'''L12 = [55, 6, 94, -5, 6, -45, 16.5, -3.6, 12.1, -4.6, .9]
print(L12[:5:5])'''
# [ VALOR-INICIAL   :  ATÉ ONDE MENOS 1   : INCREMENTO    ]

'''L13 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(L13[::2])
print(L13[1::2])
print(L13[1::3])'''

# Dicionários:
'''Dic1 = {'Virtus':99999, 'A3':139999, 'Sentra':90000, 41:'Cachaça'}
print(Dic1[41])
print(Dic1['A3'])'''

'''Dic2 ={'Loja 1':['Maycon', 'Pedro'], 'Loja 2':['Pablo', 'Isaac'], 'Loja 3':['Jobson', 'Gilherme']}
print(Dic2['Loja 1'])
print(Dic2['Loja 2'])
print(Dic2['Loja 3'])
print(Dic2['Loja 1'][1])'''

'''Dic3 ={'Loja 1':{'Func1':'Maycon', 'Func2':'Pedro'}, 'Loja 2':{'Func1':'Pablo', 'Func2':'Isaac'}}
print(Dic3['Loja 2']['Func1'])'''

'''Valor = {'L1':{'Cebola':6.5, 'Cenoura':3.9, 'Tomate':6.9}, 'L2':{'Cebola':3, 'Cenoura':2.9, 'Tomate':4.9}}
print(Valor['L1']['Cebola'])
print(Valor['L2']['Cebola'])
print( ((Valor['L1']['Cebola'] / Valor['L2']['Cebola']) - 1 )*100, '%') #Que % a Cebola de L1 é mais caro do que em L2
Soma_L1 = Valor['L1']['Cebola']+Valor['L1']['Cenoura']+Valor['L1']['Tomate']
print('A soma dos valores por Kg em L1 é:', Soma_L1)
Soma_L2 = Valor['L2']['Cebola']+Valor['L2']['Cenoura']+Valor['L2']['Tomate']
print('A soma dos valores por Kg em L2 é:', Soma_L2)
print('Três Kg de Tomate em L1 será:', 3*Valor['L1']['Tomate'])'''


'''Valor = {'L1':{'Cebola':{'Branca':3.99, 'Roxa':8.99}, 'Banana':{'Prata':3.99,'Nanica':2.99}},
         'L2':{'Cebola':{'Branca':2.99, 'Roxa':5.99},'Banana':{'Prata':2.99,'Nanica':1.99}}}
print(Valor['L1']['Cebola']['Roxa'])
print(Valor['L2']['Banana']['Prata'])
Valor['L1']['Cebola']['Branca'] = 3.99 + 1 # Aumentou 1 real a Cebola Branca em L1
print(Valor)'''

# Tuples: Imutável!
'''T1 = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
print(T1[::2])
print(T1[1::2])
print(T1[1::3])
X = T1[0] + T1[-1]
print(X)
print(T1.index(6))
T1[0] = 8 # Erro! Tentativa de mudança na Tuple'''

'''L14 = ['Carro', 6.5, True, 5, 'Moto']
Set_L14 = set(L14)
print(Set_L14)'''

'''L14 = ['Carro', 6.5, True, 5, 'Moto', 5, 'Carro', 7, 6.5, False, 2, True]
print(L14)
Set_L14 = set(L14)
print(Set_L14)
print(type(Set_L14))
L14_Sem_Repetidos = list(Set_L14)
print(L14_Sem_Repetidos)
L14_Sem_Repetidos.append(88)
print(L14_Sem_Repetidos)'''

'''Texto = 'casa do Iesb'
Texto_set = set(Texto)
print(Texto_set)'''

# No seguinte Texto, imprima os caracteres utilizados sem repetição, sem contar com o
# caractere ESPAÇO, ordenado alfabeticamente e em uma só String.
# Exemplo 'Probabilidade e Estatistica IESB 2020' --> '02BEIPSabcdeirst'
Texto = 'Probabilidade e Estatistica IESB 2020'
Texto2 = Texto.split()
print(Texto2)
Texto3 = ''.join(Texto2)
print(Texto3)
Texto4 = set(Texto3)
print(Texto4)
Texto5 = list(Texto4)
print(Texto5)
Texto5.sort()
print(Texto5)
Texto6 = ''.join(Texto5)
print(Texto6)