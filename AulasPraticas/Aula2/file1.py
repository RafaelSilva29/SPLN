#!/usr/bin/env python3

texto = """
		O Lorem Ipsum é um texto modelo da indústria tipográfica e de impressão.
		O Lorem Ipsum tem vindo a ser o texto padrão usado por estas indústrias desde o ano de 1500,
		quando uma misturou os caracteres de um texto para criar um espécime de livro.
		Este texto não só sobreviveu 5 séculos, mas também o salto para a tipografia electrónica,
		mantendo-se essencialmente inalterada. Foi popularizada nos anos 60 com a disponibilização das folhas de Letraset,
		que continham passagens com Lorem Ipsum, e mais recentemente com os programas de publicação como o Aldus PageMaker que incluem versões do Lorem Ipsum.
		"""

texto = texto.replace(",", "").replace(".","")
lista = texto.split()

ocorrencias = {}

for word in lista:
	ocorrencias[word] = ocorrencias.get(word,0) + 1


for w,v in sorted(ocorrencias.items(),key= lambda x : x[1],reverse=True):
	print(w,"->",v)