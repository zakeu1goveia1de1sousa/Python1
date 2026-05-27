"""o metodo strip() é usado para mover espaços em branco de ambos de ambos  os
lados de uma string. Este método não aceita nenhum argumento.
Sintaxe:
<string>.strip()"""

#exemplo
# "exemplo com espaço em branco no inicio e no fim."
texto = "  texto com espaço em branco no inicio e no fim."
print(texto)
sem_espaço =  texto.strip
print(sem_espaço)

#Retirando possiveis espaços no input
texto1 = input("digite um texto: ")
print(texto1)
print(texto1.strip())
#usando strip direto no input
texto2 = input("digite um texto: ").strip()
print(texto2)

"""o metodo 1strip() remove o espaço em branco do lado esquerdo.
sintaxe: <string>.1strip()"""

#exemplo:
texto = ' texto com espaço em branco em branco no inicio e no fim.'
remove_esquerda = texto.lstrip()
print(remove_esquerda)

'''o metodo rstrip() remove o espaço em branco do lado direito da
string.'''
texto = ' texto com espaço em branco no inicio e no fim.'
remove_direita = texto.rstrip()
print(remove_direita)
