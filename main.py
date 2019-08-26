# FUNDAMENTOS DA PROGRAMACAO 2016/2017 - PROJETO 1 | 86430 | GUILHERME GALAMBAS

# VERSAO SIMPLIFICADA

'''
Recebe um tuplo de 5 elementos e devolve um tuplo de 5 tuplos, 
cada um com 5 elementos (matriz). O tuplo devolvido e a chave.
'''
def gera_chave1(letras):
	return letras[:5], letras[5:10], letras[10:15], letras[15:20], letras[20:]

'''
Recebe um caracter e uma chave e devolve a posicao onde se encontra na mesma.
'''
def obtem_codigo1(car, chave):
	# A chave tem 5 elementos.
	for linha in range(5):
		# Cada elemento da chave tem 5 elementos.
		for coluna in range(5):
			if car == chave[linha][coluna]:
				return str(linha) + str(coluna)

'''
Recebe uma cadeia de caracteres e uma chave. Utilizando a funcao anterior 
e encontrada a posicao de cada caracter e devolvida uma cadeia de caracteres
composta por todas a posicoes dos caracteres recebidos, em cadeia.
'''
def codifica1(cad, chave):
	if cad == '':
		return ''
	else:
		return obtem_codigo1(cad[0], chave) + codifica1(cad[1:], chave)

'''
Recebe um codigo e uma chave e devolve o caracter correspondente 
a posicao na chave. A posicao e dada fazendo corresponder o primeiro
caracter do codigo a linha e o segundo a coluna, da chave.
'''
def obtem_car1(cod, chave):
	# cod[0] e o primeiro caracter do codigo introduzido e corresponde a linha.
	# cod[1] e o segundo caracter do codigo introduzido e corresponde a coluna.
	return chave[ int(cod[0]) ][ int(cod[1]) ]

'''
Recebe uma cadeia de caracteres e uma chave. A cadeia de caracters
e um codigo que corresponde as posicoes de cada caracter da chave, em cadeia.
Utilizando a funcao anterior, e encontrado o caracter correspondente cada a posicao
da cadeia e devolvido, numa cadeia de caracteres, a mensagem desencriptada.
'''
def descodifica1(cad_codificada, chave):
	if cad_codificada == '':
		return ''
	else:
		return obtem_car1(cad_codificada, chave) + descodifica1(cad_codificada[2:], chave)

# VERSAO FINAL

'''
Recebe um tuplo de x elementos e devolve um tuplo de y tuplos, 
cada um com y ou y-1 elementos (matriz). O tuplo devolvido e a chave.
'''
def gera_chave2(letras):
	
	# Funcao que devolve a chave.
	def chave(letras, num_elementos):
		if len(letras) <= num_elementos:
			return (letras,)
		else:
			return (letras[:num_elementos],) + chave(letras[num_elementos:], num_elementos)
	
	# Descobre a raiz do menor quadrado perfeito nao inferior ao comprimento da sequencia,
	# que corresponde ao numero de tuplos da chave (num_tuplos).
	num_tuplos = 0
	while num_tuplos * num_tuplos < len(letras):
		num_tuplos = num_tuplos + 1
	
	# Caso o comprimento da sequencia seja menor ou igual que o produto
	# de num_tuplos por num_tuplos-1 siginifica que cada tuplo apenas tera
	# num_tuplos-1 elementos.
	# Isto acontece para que o ultimo tuplo nao seja vazio.
	if len(letras) <= num_tuplos * (num_tuplos - 1):
		return chave(letras, num_tuplos - 1)
	else:
		return chave(letras, num_tuplos)

'''
Recebe um caracter e uma chave e devolve a posicao onde se encontra na mesma.
Caso o caracter nao se encontre na chave, devolve XX.
'''
def obtem_codigo2(car, chave):
	# A chave tem len(chave) elementos.
	for linha in range( len(chave) ):
		# Cada elemento da chave tem len(chave[linha]) elementos.
		for coluna in range( len(chave[linha]) ):
			if car == chave[linha][coluna]:
				return str(linha) + str(coluna)
	return 'XX'

'''
Recebe uma cadeia de caracteres e uma chave. Utilizando a funcao anterior 
e encontrada a posicao de cada caracter e devolvida uma cadeia de caracteres
composta por todas a posicoes dos caracteres recebidos, em cadeia.
'''
def codifica2(cad, chave):
	if cad == '':
		return ''
	else:
		return obtem_codigo2(cad[0], chave) + codifica2(cad[1:], chave)

'''
Recebe um codigo e uma chave e devolve o caracter correspondente 
a posicao na chave. A posicao e dada fazendo corresponder o primeiro
caracter do codigo a linha e o segundo a coluna, da chave. Caso a 
posicao seja XX, devolve ?.
'''
def obtem_car2(cod, chave):
	if cod[:2] != 'XX':
		# cod[0] e o primeiro caracter do codigo introduzido e corresponde a linha.
		# cod[1] e o segundo caracter do codigo introduzido e corresponde a coluna.
		return chave[ int(cod[0]) ][ int(cod[1]) ]
	else:
		return '?'

'''
Recebe uma cadeia de caracteres e uma chave. A cadeia de caracters
e um codigo que corresponde as posicoes de cada caracter da chave, em cadeia.
Utilizando a funcao anterior, e encontrado o caracter correspondente cada a posicao
da cadeia e devolvido, numa cadeia de caracteres, a mensagem desencriptada.
'''
def descodifica2(cad_codificada, chave):
	if cad_codificada == '':
		return ''
	else:
		return obtem_car2(cad_codificada, chave) + descodifica2(cad_codificada[2:], chave)