''' o metodo split() em python é usado para adivinhar uma string em uma
lista de substrings, com base em um caracter ou string especificada
como sepador.
string.split(separador, maxsplit)
parametros

- separador: o caractere ou string que sera usado como separador.se não fopr especificado, o padrao é qualquer espaço em branco
(espaço, tabulação, etc.).
maxsplit: o numero maximo de divisoes de divisoes que serao feitas. se não
for especificado, todas as ocorrencias do separador serao
consideradas.'''

#split por espaços em branco
frase = 'ola mundo python'
print(frase)
palavras = frase.split()
print(palavras)
#usando regra de fatiamento para exibicao dos dados
print(palavras[0]) #exibindo apenas a palavra ola
print(palavras[1]) #exibindo apenas a palavra mundo
print(palavras[2]) #exibindo apenas a palavra python
print(palavras[-1]) #exibindo apenas a palavra python
#['ola', 'mundo', 'python']

#split por virgula
frase = 'maça, banana, laranja'
print(frase)

frutas =  frase.split(',')
print(frutas)
#['maça', 'banana', 'laranja']

#split com maxsplit
frase = 'ola mundo, python é divertido'
palavras = frase.split(' ', 2)
print(palavras)
#['ola', 'mundo', 'pyton é divertido']

'''observaçoes:
Se o separador não for encontrado na string, a lista resultante
contera apenas a stringoriginal.

se a string estiver vazia, a lista resultante sera vazia.
o metodo split() é muito util para processar strings e extrair informaçoes relevantes.'''
