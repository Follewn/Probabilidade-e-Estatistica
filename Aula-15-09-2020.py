# No seguinte Texto, imprima os caracteres utilizados sem repetição, sem contar com o
# caractere ESPAÇO, ordenado alfabeticamente e em uma só String.
# Exemplo 'Probabilidade e Estatistica IESB 2020' --> '02BEIPSabcdeilorst'
'''Texto = 'Probabilidade e Estatistica IESB 2020'
Texto = list(set(Texto))
print(Texto)
Texto.remove(' ')
print(Texto)
Texto.sort()
print(Texto)
Texto = ''.join(Texto)
print(Texto)'''

'''MeuArquivo = open('TextoPadrão.txt')
print(MeuArquivo.read())
MeuArquivo.seek(0)
print(MeuArquivo.read())'''

'''Arq1 = open('TextoPadrão.txt')
Str1 = Arq1.read()
print(Str1)'''

'''Arq1 = open('TextoPadrão.txt')
Str2 = Arq1.readlines()
print(Str2)
Arq1.close()'''

# Abra o arquivo 'TextoPadrão.txt', insira como primeira linha
# o texto 'Probabilidade e Estatistica IESB 2020', dê 2 quebras
# de linha e salve o resultado em outro arquivo chamado 'Novo.txt' 

'''x = 'Probabilidade e Estatistica IESB 2020'
Arq1 = open('TextoPadrão.txt')
Str1 = Arq1.read()
StrFinal = x + '\n\n' + Str1
print(StrFinal)
Arq2 = open('Novo.txt', 'w')
Arq2.write(StrFinal)
Arq2.close()'''

'''Arq1 = open('TextoPadrão.txt', 'w')
y = 'ABC'
Arq1.write(y)
Arq1.close()'''

Arq1 = open('TextoPadrão.txt')
Str1 = Arq1.read()
StrFinal = x + '\n\n' + Str1
print(StrFinal)