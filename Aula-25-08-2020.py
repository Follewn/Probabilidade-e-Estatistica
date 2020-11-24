'''Palavra1 = 'Texto 1'
Palavra2 = "Texto 2"
#print(Palavra1)
print(Palavra2)'''

'''VarTexto = 'abcdefghijkl'
print(VarTexto)
tamanho = len(VarTexto)
print(tamanho)
print(VarTexto[::-1])'''

'''MeuTexto = 'IESB'
print(MeuTexto[0])
MeuTexto2 = 'O' + MeuTexto[1:]
print(MeuTexto2)'''

'''a = 'x'
b = 'y'
c = a + b   # A veriável c é 'xy'
c = 3*c     # A nova variável c é 'xyxyxy'
print(c)'''

'''MeuTexto = 'Caros alunos, Esse é o espaço para postar as dúvidas gerais...'
Palavras = MeuTexto.split()
#print(Palavras)
#print(Palavras[2])
SeparaLetra_s = MeuTexto.split('s')
print(SeparaLetra_s)'''

# Como contar palavras de um texto:
'''MeuTexto = 'Caros alunos, Esse é o espaço para postar as dúvidas gerais...'
print(MeuTexto.split())
print(len(MeuTexto.split()))'''

'''Carros = 'Os carros que tive são: {}, {}, {}, {} e {}.'
Carro0 = 'Ka'
Carro1 = 'Gol'
Carro2 = 'Sentra'
Carro3 = 'Bravo'
Carro4 = 'Virtus'
print(Carros.format(Carro0, Carro1, Carro2, Carro3, Carro4))'''

'''Carros = 'Os carros que tive são: {4}, {3}, {2}, {1} e {0}.'
Carro0 = 'Ka'
Carro1 = 'Gol'
Carro2 = 'Sentra'
Carro3 = 'Bravo'
Carro4 = 'Virtus'
print(Carros.format(Carro0, Carro1, Carro2, Carro3, Carro4))'''

'''Texto = 'Esse governo que aí está passou um ano e meio sem se preocupar com o Fundeb, tentou pegar uma carona no final. Mas, felizmente, como isso aqui é uma emenda constitucional, Bolsonaro, você não vai poder vetar. Nós vamos promulgar e o seu governo vai ter que cumprir. Você não vai pegar carona nem vai vetar essa grande conquista do povo'
print( Texto.split('g') )
print( len( Texto.split('g') ) -1 )'''