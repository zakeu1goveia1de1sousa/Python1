'''o metodo replace() é usado para substituir uma parte especifica de
uma cadeia de caracteres por outra, se a cores´pondencia
for encontrada. Ele podde receber trÊs argumentos, sendo dois obrigatorios
e um opcional.'''

#exemplo:
'''no script a seguir, o primeiro replace é usado para substituira
palavra 'portugol' pela palavra 'java'.'''

texto = ' eu gosto dede portugol, mas eu gosto mais de python.'
substituicao = texto.replace('portugol', 'java')
#strig original:
# eu gosto de portugol, mas eu gosto mais de python.
print('string original: ', texto)
#string substituida:
#eu gosto de java, mas eu gosto mais de python.
print('string substituida: ', substituicao)

#exemplo2
substituicao_2 = texto.replace("gosto", "nao gosto", 1)
#string original: eu gosto de php, mas eu gosto mais de python
print('string original:', texto)

print('string substituida: ', substituicao_2)

#exemplo3
texto = 'eu gosto de php, mas eu gosto mais de python, gosto muito'
substituicao_3 = texto.replace('gosto', 'nao gosto', 2)
#string original: eu gosto de php, mas eu gosto mais de python
print('string original:', texto)
#string substituida: eu não gosto de php, mas eu gosto mais de python
print('string substituida:', substituicao_3)
