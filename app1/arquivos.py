arquivo = open('texto.txt', 'r')
lista = []
dic = {}
#criando uma lista com os itens do arquivo
for linha in arquivo:
    linha = linha.strip()
    lista.append(linha)
arquivo.close

#lista onde cada item são todas as informações do livro
print(lista)
aux = 0
#iterando sobre a lista para criar um dicionario e obter as informações das chaves CHAVE ID(informações sao os itens 1,2,3 de cada lista)
for item in lista:
    a = lista[aux].split(",") 
    print(a)

