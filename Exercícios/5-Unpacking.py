# #Unpacking é o processo de "desempacotar" os elementos de uma coleção (lista, tupla, etc.) em variáveis individuais.

## O que é Unpacking em Python?

## Unpacking é o processo de "desempacotar" os elementos de uma coleção (lista, tupla, etc.) em variáveis individuais.

# dados = ("João", 25)
#
# nome, idade = dados
#
# print(nome) # João
# print(idade) # 25

# #Também pode ser usado em chamadas de função.

# def somar(a, b):
# return a + b
#
# numeros = [10, 20]
#
# resultado = somar(*numeros)
# print(resultado) # 30
# O operador *

## O * tem dois usos principais:

# #1. Unpacking de iteráveis
# Python
# numeros = [1, 2, 3]
#
# print(*numeros)

# #Saída:


## 1 2 3

# É como se fosse:


# print(1, 2, 3)

# #2. Quantidade variável de argumentos

# def soma_tudo(*numeros):
# return sum(numeros)
#
# print(soma_tudo(1, 2, 3, 4))

# #Saída:

# #10

# Aqui numeros vira uma tupla:

# #(1, 2, 3, 4)
# O operador **

# Funciona parecido com *, mas para dicionários.

# Unpacking de dicionários
# Python
# dados = {
# "nome": "Maria",
# "idade": 30
# }
#
# def apresentar(nome, idade):
# print(nome, idade)
#
# apresentar(**dados)

# #Equivale a:

#
# apresentar(nome="Maria", idade=30)
# Receber quantidade variável de argumentos nomeados
# Python
# def mostrar_dados(**kwargs):
# print(kwargs)
#
# mostrar_dados(nome="Ana", idade=20)

# Saída:

# Python
# {'nome': 'Ana', 'idade': 20}

# #kwargs será um dicionário.

# #Parâmetro especial /

## O / define que os parâmetros antes dele são posicionais apenas.


# def saudacao(nome, /):
# print(f"Olá, {nome}")

# ✅ Correto:


# saudacao("João")

# ❌ Erro:


# saudacao(nome="João")

# O argumento deve ser passado pela posição.

# Parâmetro especial *

# O * sozinho define que os parâmetros seguintes são nomeados obrigatoriamente.


# def criar_usuario(nome, *, idade):
# print(nome, idade)

# #✅ Correto:

#
# criar_usuario("João", idade=25)

# #❌ Erro:

#
# criar_usuario("João", 25)

# Após o *, deve-se informar o nome do parâmetro.

# #Combinando / e *
#
# def exemplo(a, b, /, c, *, d):
# print(a, b, c, d)

# Regras:

# #Parâmetro	Tipo
## a, b	Apenas posicionais
## c	Posicional ou nomeado
# #d	Apenas nomeado

## Exemplo correto:


# #exemplo(1, 2, 3, d=4)

# #Também válido:


# exemplo(1, 2, c=3, d=4)

# # Inválido:

# # Python
# # exemplo(a=1, b=2, c=3, d=4)

# # Porque a e b são posicionais.

# # Resumo rápido
# # Python
# # *args -> recebe vários argumentos posicionais
# # **kwargs -> recebe vários argumentos nomeados
# #
# # *lista -> desempacota lista/tupla
# # **dict -> desempacota dicionário
# #
# # / -> parâmetros anteriores são posicionais apenas
# # * -> parâmetros posteriores são nomeados apenas

## Exemplo completo:


# def funcao(a, b, /, c, *args, d, **kwargs):
# print(a, b)
# print(c)
# print(args)
# print(d)
# print(kwargs)
#
# funcao(
# 1, 2,
# 3, 4, 5,
# d=10,
# nome="João",
# cidade="BH"
# )

# Saída:


# 1 2
# 3
# (4, 5)
# 10
# {'nome': 'João', 'cidade': 'BH'}

# #Essa sintaxe (/, *args, *, **kwargs) é muito usada na criação de
# APIs e funções mais profissionais em Python.


# def função(
#     a,  # / força ARGS POSICIONAIS
#     b,  # / força ARGS POSICIONAIS
#     /,  # SEPARADOR QU E INIDICA QUE TUDO ANTES DA BARRA TEM QUE SER POSICONAL
#     c,  # pode ser ARG POSICIONAL OU ARG  NOMEADO
#     d,  # pode ser ARG POSICIONAL OU ARG  NOMEADO
#     *args,  # NÚMERO VARIÁVEL DE ARG POSICIONAIS
#     e,  # ARG NOMERADO, COMO O *ARGS É POSICIONAL OBRIGA OS DEMAIS APÓS ELE A SER NOEMADO
#     f,  # ARG NOMERADO, COMO O *ARGS É POSICIONAL OBRIGA OS DEMAIS APÓS ELE A SER NOEMADO
#     **kwargs,  # NÚMERO VARIÁVEL DE ARG NOMERADO
# ):
#     pass


####################################################
# Exercício 14 – Unpacking com * e retorno

# Considere a seguinte lista:

# times = ["Brasil", "Argentina"]
# Crie uma função chamada montar_confronto que receba dois parâmetros:

# time_a
# time_b

# A função deve:

# Utilizar type hints nos parâmetros e no retorno.
# Possuir uma docstring explicando o que ela faz.
# Retornar uma string no formato Brasil x Argentina.
# Depois, chame a função desempacotando a lista com *.

# Você não deve acessar os valores manualmente com:

# times[0]
# times[1]

# Exemplo esperado de uso:

# confronto = montar_confronto(*times)
# print(confronto)

####################################################

# times = ["Brasil", "Argentina"]

# def montar_confronto(time_a: str, time_b: str) -> str:
#     """
#     Monta o texto do confronto entre dois times.

#     Args:
#         time_a: nome do primeiro time
#         time_b: nome do segundo time

#     Returns:
#         Texto no formato "Time A x Time B".
#     """
#     confronto = f"{time_a} x {time_b}"
#     return confronto

# confronto = montar_confronto(*times)
# print(confronto)

###################### FIM #########################
# Exercício 15 – Unpacking com * e valores padrão

# Crie uma função chamada calcular_media com os seguintes parâmetros:

# nota1
# nota2
# nota3
# bonus=0

# A função deve:

# Utilizar type hints em todos os parâmetros e no retorno.
# Possuir uma docstring.
# Calcular a média das três notas.
# Somar o valor de bonus ao resultado final.
# Retornar a média calculada.


# Considere:
# notas = [8.5, 7.0, 9.5]

# Chame a função utilizando * para desempacotar as notas:

# resultado = calcular_media(*notas)
# print(resultado)


# Depois, faça uma segunda chamada utilizando a mesma lista, mas informe bonus como argumento nomeado.

# Por fim, altere a lista para possuir quatro notas:
# notas = [8.5, 7.0, 9.5, 10.0]


# Tente realizar novamente:
# calcular_media(*notas)
# Observe o comportamento e explique por que o quarto valor deixa de representar uma nota e passa a ocupar o parâmetro bonus.

#
####################################################


# def calcular_media(nota1: float, nota2: float, nota3: float, bonus: float = 0) -> float:
#     """
#     Calcula a média de três notas e soma o bônus

#     Args:
#         nota1: primeira nota
#         nota2: segunda nota
#         nota3: terceir nota
#         bonus: nota bonus, o padrão é 0
#     Returns:
#         Média das três notas somada ao bônus
#     """

#     media_notas = (nota1 + nota2 + nota3) / 3
#     resultado = media_notas + bonus
#     return resultado


# notas = [8.5, 7.0, 9.5]

# resultado = calcular_media(*notas)
# print(f"{resultado:.2f}")

# # Segunda chamada

# notas = [8.5, 7.0, 9.5, 10.0]
# resultado = calcular_media(*notas)
# print(f"{resultado:.2f}")

# #Observe o comportamento e explique por que o quarto valor deixa de representar uma nota e passa a ocupar o parâmetro bonus.

# O * desempacota os itens da lista na ordem, um em cada parâmetro.
# Os três primeiros valores vão para nota1, nota2 e nota3, e o quarto elemento vai para o próximo parâmetro da fila, que é o bonus.
# A função não sabe que aquele valor era uma nota: para ela, é só o quarto argumento.
###################### FIM #########################
# Exercício 16 – Unpacking com ** e argumentos nomeados


# Considere o seguinte dicionário:

# jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}


# Crie uma função chamada apresentar_jogador que receba:

# nome
# idade
# posicao


# A função deve:

# Utilizar type hints em todos os parâmetros.
# Indicar através do type hint que a função não retorna nenhum valor.
# Possuir uma docstring.
# Exibir uma mensagem com os dados do jogador.


# Chame a função desempacotando o dicionário com **.

# Você não deve acessar manualmente:

# jogador["nome"]
# jogador["idade"]
# jogador["posicao"]

# Depois, responda em um comentário no código:

# Por que as chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função?

####################################################


# def apresentar_jogador(nome: str, idade: int, posicao: str) -> None:
#     """
#     Apresenta as informações do jogador
#     Args:
#         nome: nome do jogador
#         idade: idade do jogador
#         posicao: posição em campo do jogador

#     """
#     print(f" A jogadora {nome} tem {idade} anos de idade e joga na posição {posicao}")


# jogador = {"nome": "Marta", "idade": 40, "posicao": "Atacante"}
# apresentar_jogador(**jogador)


# Por que as chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função?

# O ** desempacota o dicionário como argumentos nomeados: cada chave vira
# o nome do argumento e cada valor vira o que é passado. Por isso as chaves
# precisam ter os mesmos nomes dos parâmetros da função, para o Python saber
# em qual parâmetro encaixar cada valor. Se uma chave tiver outro nome,
#  o Python dá TypeError, porque a função não tem nenhum parâmetro com aquele nome.
###################### FIM #########################
# Exercício 17 – *args recebendo e * desempacotando


# Crie uma função chamada calcular_total_gols que receba uma quantidade variável de números utilizando *args.


# A função deve:

# Utilizar type hint no *args.
# Possuir uma docstring.
# Somar todos os valores recebidos.
# Retornar o total de gols.
# Considere as listas:

# primeiro_tempo = [1, 2, 1]
# segundo_tempo = [2, 1]


# Chame a função desempacotando as duas listas na mesma chamada:

# total = calcular_total_gols(*primeiro_tempo,*segundo_tempo)
# print(total)


# Depois, escreva comentários no código explicando a diferença entre:

# def calcular_total_gols(*gols):...
# e:

# calcular_total_gols(*primeiro_tempo)

# Explique qual * está recebendo vários argumentos e qual está desempacotando uma coleção.

####################################################


# def calcular_total_gols(*gols: int) -> int:
#     """
#     Soma uma quantidade variável de gols e retorna o total
#     Args:
#         *gols: quantidade variável de gols
#     Returns:
#         Retornar o total de gols
#     """
#     total_gols = sum(gols)
#     return total_gols


# primeiro_tempo = [1, 2, 1]
# segundo_tempo = [2, 1]

# total = calcular_total_gols(*primeiro_tempo, *segundo_tempo)
# print(total)

# #Explique qual * está recebendo vários argumentos e qual está desempacotando uma coleção.

# O * na definição (def calcular_total_gols(*gols)) recebe vários argumentos
# posicionais e junta todos em uma tupla chamada gols.
# O * na chamada (calcular_total_gols(*primeiro_tempo)) desempacota a lista,
# enviando cada elemento como um argumento separado.

###################### FIM #########################
# Exercício 18 – Parâmetros somente posicionais com /

# Crie uma função chamada registrar_placar com a seguinte assinatura:
# def registrar_placar(time_a: str,time_b: str,/,gols_a: int,gols_b: int) -> str:...

# A função deve:

# Possuir uma docstring.
# Utilizar os type hints indicados.
# Retornar uma string contendo o placar da partida.
# Exigir que time_a e time_b sejam passados somente por posição.
# Permitir que gols_a e gols_b sejam passados por posição ou pelo nome.

# Faça uma chamada válida utilizando:

# resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
# print(resultado)

# Depois, tente:

# registrar_placar(time_a="Brasil",time_b="Argentina",gols_a=2,gols_b=1)
# Observe o erro e explique em um comentário qual é a função do / na assinatura.

###################### ##### #########################

# def registrar_placar(time_a: str, time_b: str, /, gols_a: int, gols_b: int) -> str:
#     """
#     Registra o placar de uma partida entre dois times.

#     Args:
#         time_a: nome do primeiro time (somente posicional)
#         time_b: nome do segundo time (somente posicional)
#         gols_a: gols do primeiro time
#         gols_b: gols do segundo time

#     Returns:
#         String com o placar da partida
#     """
#     placar = f"O placar da partida foi {time_a} {gols_a} x {gols_b} {time_b}"
#     return placar

# resultado = registrar_placar("Brasil", "Argentina", gols_a=2, gols_b=1)
# print(resultado)
# # Chamada inválida
# registrar_placar(time_a="Brasil", time_b="Argentina", gols_a=2, gols_b=1)

# #Observe o erro e explique em um comentário qual é a função do / na assinatura.

# # O / é um separador. Os parâmetros à esquerda dele (time_a e time_b) são
# somente posicionais: devem ser passados pela ordem, sem usar o nome.
# Os parâmetros à direita (gols_a e gols_b) podem ser passados por posição
# ou pelo nome, por isso gols_a=2 e gols_b=1 funcionaram na primeira chamada.
# # Na segunda chamada, time_a e time_b foram passados pelo nome, o que gera:
# TypeError: registrar_placar() got some positional-only arguments passed
# as keyword arguments: 'time_a, time_b'
###################### FIM #########################
# Exercício 19 – Parâmetros somente nomeados com *

# Crie uma função chamada criar_jogador com a seguinte assinatura:
# def criar_jogador(nome: str,*,posicao: str,numero: int,titular: bool = False) -> str:...
# A função deve:

# Possuir uma docstring.
# Utilizar type hints.
# Utilizar um valor padrão para titular.
# Retornar uma string com os dados do jogador.
# O parâmetro nome pode ser informado por posição.

# Os parâmetros após * devem ser informados pelo nome.
# Faça uma chamada válida:

# jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
# print(jogador)

# Depois, faça outra chamada informando:
# titular=True
# Por fim, tente executar:
# criar_jogador("Marta","Atacante",10)

# Observe o erro e explique em um comentário por que posicao e numero não podem
# ser passados por posição.
# ####################################################


# def criar_jogador(
#     nome: str, *, posicao: str, numero: int, titular: bool = False
# ) -> str:
#     """
#     Monta um texto com os dados do jogador.

#     Args:
#         nome: nome do jogador
#         posicao: posição do jogador em campo
#         numero: número da camisa do jogador
#         titular: indica se o jogador é titular; o padrão é False

#     Returns:
#         Texto com os dados do jogador.
#     """
#     dados_jogador = f"A Jogadora {nome} joga na posição {posicao} com a camisa de numero {numero} situação: {titular}"
#     return dados_jogador


# # chamada válida:

# jogador = criar_jogador("Marta", posicao="Atacante", numero=10)
# print(jogador)

# # chamada informando titular=True:
# jogador = criar_jogador("Marta", posicao="Atacante", numero=10, titular=True)
# print(jogador)

# # chamada inválida:
# criar_jogador("Marta", "Atacante", 10)
# erro: TypeError: criar_jogador() takes 1 positional argument but 3 were given

# #Observe o erro e explique em um comentário por que posicao e numero não podem ser passados por posição.

# O * foi usado como separador, determinando que os parâmetros após o * sejam
# obrigatoriamente nomeados. Assim, a função aceita apenas um argumento por
# posição (o nome). Na chamada criar_jogador("Marta", "Atacante", 10), "Atacante"
# e 10 foram passados por posição, e o Python não tem onde encaixá-los,
# por isso apresenta TypeError.

# ###################### FIM #########################

# Exercício 20 – Desafio final: trabalhando com todos os tipos de argumentos

# Crie uma função chamada registrar_jogo com a seguinte assinatura:

# def registrar_jogo(
# mandante: str,visitante: str,
# /,
# competicao: str,
# *eventos: str,
# estadio: str,
# encerrado: bool = True,
# **informacoes
# ) -> dict:

# A função deve possuir uma docstring completa explicando:

# O objetivo da função.
# O que cada parâmetro representa.
# O que a função retorna.

# A função também deve seguir estas regras:

# mandante e visitante devem ser informados somente por posição.
# competicao pode ser passada por posição ou pelo nome.
# *eventos deve receber uma quantidade variável de eventos da partida.
# estadio deve obrigatoriamente ser informado pelo nome.
# encerrado deve possuir True como valor padrão.
# **informacoes deve receber informações adicionais da partida.

# Dentro da função, crie e retorne um dicionário contendo:

# Mandante.
# Visitante.
# Competição.
# Eventos.
# Estádio.
# Situação da partida.
# Informações adicionais.
# Teste a função com:

# partida = registrar_jogo(
# "Brasil",
# "Argentina",
# "Copa do Mundo",
# "Gol do Brasil",
# "Cartão amarelo",
# "Substituição",
# estadio="Maracanã",
# publico=70000,
# transmissao="TV"
# )
# print(partida)

# Depois, considere os seguintes dados:

# times = ["França", "Espanha"]
# dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}

# Faça uma segunda chamada utilizando:

# *times para desempacotar os dois primeiros argumentos.
# Uma competição informada normalmente.
# Dois ou mais eventos posicionais.
# **dados para desempacotar as informações nomeadas.

# Ao final, escreva comentários identificando o papel de cada elemento da assinatura:

# /
# *eventos
# estadio
# encerrado=True
# **informacoes

# Explique também a diferença entre:

# *eventos
# na definição da função e:

# *times
# na chamada, assim como a diferença entre:

# **informacoes
# na definição e:

# **dados
# na chamada.
####################################################


# def registrar_jogo(
#     mandante: str,
#     visitante: str,
#     /,
#     competicao: str,
#     *eventos: str,
#     estadio: str,
#     encerrado: bool = True,
#     **informacoes,
# ) -> dict:
#     """
#     Registra os dados de uma partida em um dicionário.

#     Args:
#         mandante: nome da seleção mandante (somente por posição)
#         visitante: nome da seleção visitante (somente por posição)
#         competicao: nome da competição (por posição ou pelo nome)
#         eventos: eventos da partida, em quantidade variável
#         estadio: nome do estádio (obrigatoriamente pelo nome)
#         encerrado: situação da partida; o padrão é True
#         informacoes: informações adicionais da partida

#     Returns:
#         Dicionário com os dados da partida.
#     """
#     dados_partida = {
#         "Mandante": mandante,
#         "Visitante": visitante,
#         "Competição": competicao,
#         "Eventos": eventos,
#         "Estádio": estadio,
#         "Situação da partida": encerrado,
#         "Informações adicionais": informacoes,
#     }
#     return dados_partida


# # Primeira chamada

# partida = registrar_jogo(
#     "Brasil",
#     "Argentina",
#     "Copa do Mundo",
#     "Gol do Brasil",
#     "Cartão amarelo",
#     "Substituição",
#     estadio="Maracanã",
#     publico=70000,
#     transmissao="TV",
# )
# print(partida)

# # Depois, considere os seguintes dados:

# # times = ["França", "Espanha"]
# # dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}
# partida = registrar_jogo(
#     "França",
#     "Espanha",
#     "Copa do Mundo",
#     estadio="Stade de France",
#     publico=65000,
#     transmissao="Streaming",
# )
# print(partida)
# # Segunda chamada, com *times e **dados

# times = ["França", "Espanha"]
# dados = {"estadio": "Stade de France", "publico": 65000, "transmissao": "Streaming"}

# partida = registrar_jogo(
#     *times, "Copa do Mundo", "Gol da França", "Gol da Espanha", **dados
# )
# print(partida)

# # #Papel de cada elemento da assinatura:

# # /  -> separador: mandante e visitante, que vêm antes dele, só podem ser informados por posição, nunca pelo nome.
# # *eventos -> recebe os argumentos posicionais que sobram e junta todos em  uma tupla. Os parâmetros que vêm depois dele só podem ser passados pelo nome.
# # estadio -> parâmetro obrigatório e somente nomeado: está depois de *eventos e não tem valor padrão, então precisa ser informado pelo nome.
# # encerrado=True -> parâmetro somente nomeado com valor padrão: se não for
# #       informado, vale True.
# # **informacoes -> recebe os argumentos nomeados que sobram e junta todos em um dicionário.

# # Diferença entre *eventos (na definição) e *times (na chamada):
# # Na definição, o * EMPACOTA: junta vários argumentos posicionais em uma tupla.
# # Na chamada, o * DESEMPACOTA: abre a lista times e entrega cada item como
# # um argumento posicional separado.

# # Diferença entre **informacoes (na definição) e **dados (na chamada):
# # Na definição, o ** EMPACOTA: junta os argumentos nomeados que sobram em# um dicionário. Na chamada,
# # o ** DESEMPACOTA: abre o dicionário dados e  entrega cada chave como nome de argumento e cada valor como o valor passado.
