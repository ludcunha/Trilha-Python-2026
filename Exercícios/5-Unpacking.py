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

# Observe o comportamento e explique por que o quarto valor deixa de representar uma nota e passa a ocupar o parâmetro bonus.

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


def apresentar_jogador(nome: str, idade: int, posicao: str) -> None:
    """
    Apresenta as informações do jogador
    Args:
        nome: nome do jogador
        idade: idade do jogador
        posicao: posição em campo do jogador

    """
    print(f" A jogadora {nome} tem {idade} anos de idade e joga na posição {posicao}")


jogador = {"nome": "Marta", "idade": 40, "posicao": "Atacante"}
apresentar_jogador(**jogador)


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
