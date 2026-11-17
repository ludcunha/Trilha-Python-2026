# Atividade Prática – Parâmetros e Argumentos em Funções ###

#    Exercício 1 – Argumentos posicionais

# Crie uma função chamada apresentar_jogador que receba:

# nome
# posicao
# A função deve exibir uma mensagem semelhante a:

# Jogador: Marta | Posição: Atacante
# Faça a chamada da função passando os dois argumentos por posição.

# Exemplo:

# apresentar_jogador("Marta", "Atacante")

###################### ###### #########################

# def apresentar_jogador(nome: str, posicao: str) -> None:
#     """
#         Apresenta nome e a posição do jogador
#     Args.:
#         nome: nome do jogador
#         posicao: posição do jogador em campo
#     """
#     print(f"Jogador: {nome} | Posição: {posicao}")

# apresentar_jogador("Marta", "Atacante")

###################### FIM #########################
# Exercício 2 – A ordem dos argumentos

# Crie uma função chamada mostrar_partida que receba:

# mandante
# visitante
# A função deve exibir os dois times no formato:

# Brasil x Argentina
# Faça as seguintes chamadas:

# mostrar_partida("Brasil", "Argentina")mostrar_partida("Argentina", "Brasil")

# Observe como a ordem dos argumentos posicionais altera o resultado.

###################### ###### #########################


# def mostrar_partida(mandante: str, visitante: str) -> None:
#     """
#     Exibe os times que disputarão a partida

#     Args.:
#         mandante: time mandante
#         visitante :time visitante
#     """
#     print(f"{mandante} x {visitante}")


# mostrar_partida("Brasil", "Argentina")
# mostrar_partida("Argentina", "Brasil")

###################### FIM #########################

# Exercício 3 – Argumentos nomeados

# Crie uma função chamada cadastrar_jogador que receba:

# nome
# idade
# posicao

# Faça a chamada utilizando argumentos nomeados e passe os valores em uma ordem diferente da definida na função.

# Exemplo:

# cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)

###################### ###### #########################


# def cadastrar_jogador(nome: str, idade: int, posicao: str) -> None:
#     """
#     Exibe as informações dos jogadores

#      Args.:
#         nome: nome do jogador
#         idade : idade do jogador
#         posicao: posição do jogador em campo
#     """
#     print(f"O jogador {nome} tem {idade} anos e atua como {posicao}.")

# cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)
# cadastrar_jogador(idade=33, posicao="Goleiro", nome="Aisson")

###################### FIM #########################
# Exercício 4 – Posicionais e nomeados juntos

# Crie uma função chamada registrar_gol que receba:

# jogador
# time
# minuto


# Na chamada da função:

# Passe jogador por posição.
# Passe time por posição.
# Passe minuto pelo nome.


# A função deve exibir uma mensagem semelhante a:

# Vini Jr marcou para o Brasil aos 34 minutos.


###################### ###### #########################


# def registrar_gol(jogador: str, time: str, minuto: int) -> None:
#     """
#     Exibe as informações do gol

#      Args.:
#         jogador: nome do jogador
#         time : nome do time do jogador
#         minuto: minuto em que o gol foi marcado.
#     """
#     print(f"{jogador} marcou para o {time} aos {minuto} minutos.")

# registrar_gol("Vini Jr", "Brasil", minuto=34)

###################### FIM #########################

# Exercício 5 – Parâmetro com valor padrão

# Crie uma função chamada criar_partida que receba:

# time_a
# time_b
# estadio

# O parâmetro estadio deve possuir o seguinte valor padrão:

# "Estádio Nacional"

# Depois, faça duas chamadas:

# Uma sem informar o estádio.
# Outra informando um estádio diferente.
###################### ###### #########################


# def criar_partida(time_a: str, time_b: str, estadio="Estádio Nacional") -> None:
#     """
#     Exibe as informações da partida.

#     Args:
#         time_a: nome do primeiro time participante da partida.
#         time_b: nome do segundo time participante da partida.
#         estadio: nome do estádio onde a partida será realizada.
#                  O padrão é "Estádio Nacional".
#     """
#     print(
#         f"A partida entre {time_a} e {time_b} será realizada no estádio {estadio}."
#     )


# criar_partida("Brasil", "Argentina")
# criar_partida("Brasil", "Argentina", estadio="Mineirão")

###################### FIM #########################
# Exercício 6 – Mais de um valor padrão

# Crie uma função chamada registrar_jogador com os seguintes parâmetros:

# nome
# posicao="Não informada"
# titular=False

# A função deve mostrar os dados do jogador.

# Teste as seguintes chamadas:

# registrar_jogador("Marta")
# registrar_jogador("Marta", "Atacante")
# registrar_jogador("Marta", "Atacante", True)


# Depois, faça mais uma chamada alterando apenas o valor de titular, utilizando um argumento nomeado.

###################### ###### #########################


# def registrar_jogador(nome: str, posicao="Não informada", titular=False) -> None:
#     """
#     Exibe as informações do jogador

#      Args.:
#         nome: nome do jogador.
#         posicao: posição do jogador em campo.O padrão é "Não informada".
#         titular: indica se o jogador é titular. O padrão é False.

#     """
#     print(f"O jogador {nome} atua na posição {posicao} - Titular: {titular}.")

# registrar_jogador("Marta")
# registrar_jogador("Marta", "Atacante")
# registrar_jogador("Marta", "Atacante", True)

# registrar_jogador("Marta", titular=True)

###################### FIM #########################
# Exercício 7 – Alterando apenas um valor padrão

# Crie uma função chamada configurar_camisa que receba:

# nome
# numero
# tamanho="M"
# cor="amarela"

# Faça uma chamada informando uma cor diferente, mas mantendo o tamanho padrão.

# Exemplo:
# configurar_camisa("Marta", 10, cor="azul")
# Observe como o argumento nomeado permite alterar cor sem precisar passar um novo valor para tamanho.


###################### ###### #########################


# def configurar_camisa(nome: str, numero: int, tamanho="M", cor="amarela") -> None:
#     """
#     Exibe as informações da camisa do jogador.

#     Args:
#         nome: nome do jogador.
#         numero: número da camisa do jogador.
#         tamanho: tamanho da camisa. O padrão é "M".
#         cor: cor da camisa. O padrão é "amarela".
#     """
#     print(
#         f"O jogador {nome} usa a camisa número {numero}, tamanho {tamanho}, na cor {cor}."
#     )


# configurar_camisa("Marta", 10, cor="azul")

##
###################### FIM #########################
# Exercício 8 – Recebendo vários argumentos com *args

# Crie uma função chamada listar_jogadores que receba uma quantidade variável de nomes utilizando *args.

# def listar_jogadores(*jogadores):

# A função deve percorrer os jogadores recebidos e exibir cada nome.

# Teste a função com diferentes quantidades de argumentos:

# listar_jogadores("Marta")listar_jogadores("Marta","Vini Jr","Alisson")

###################### ###### #########################


# def listar_jogadores(*jogadores):
#     """
#         Apresenta o nome dos jogadores
#     Args.:
#         jogadores: nome do jogador
#     """
#     for jogador in jogadores:
#         print(f" - {jogador}")

# listar_jogadores("Marta")
# listar_jogadores("Marta", "Vini Jr", "Alisson")


###################### FIM #########################
# Exercício 9 – Trabalhando com os valores de *args

# Crie uma função chamada somar_gols que receba uma quantidade indefinida de números utilizando *args.

# A função deve retornar a soma de todos os valores recebidos.

# Exemplo:

# total = somar_gols(2, 1, 3, 2)
# print(total)

# Resultado esperado:

# 8


###################### ###### #########################
# def somar_gols(*gols: int) -> int:
#     """
#         Somar a quantidade de gols
#     Args.:
#         gols: informe os gols da partida
#     """
#     return sum(gols)


# total = somar_gols(2, 1, 3, 2)
# print(total)


###################### FIM ######################## ##
# Exercício 10 – Parâmetro normal e *args

# Crie uma função chamada:
# convocar_selecao(pais, *jogadores)

# O primeiro argumento deve representar o país da seleção.
# Todos os argumentos posicionais seguintes devem representar os jogadores convocados.

# Exemplo de chamada:

# convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")

# A função deve mostrar primeiro o país e depois cada jogador convocado.
###################### ###### #########################


# def convocar_selecao(pais: str, *jogadores) -> None:
#     """
#         Exibir a lista de jogadores da seleção
#     Args.:
#         pais: nome da seleção
#         jogadores: jogadores convocados para a seleção
#     """
#     print(f"Seleção: {pais}")
#     for jogador in jogadores:
#         print(jogador)

# convocar_selecao("Brasil", "Alisson", "Marquinhos", "Bruno Guimarães", "Vini Jr")


###################### FIM #########################
# Exercício 11 – Recebendo argumentos nomeados com **kwargs

# Crie uma função chamada mostrar_jogador que receba uma quantidade variável de argumentos nomeados utilizando **kwargs.

# def mostrar_jogador(**dados):

# Faça uma chamada semelhante a:
# mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")
# Dentro da função, percorra os dados recebidos e mostre cada chave junto com seu respectivo valor.

###################### ###### #########################

# Exercício 11 – Recebendo argumentos nomeados com **kwargs

# def  mostrar_jogador que receba uma quantidade variável de argumentos nomeados utilizando **kwargs.


# def mostrar_jogador(**dados) -> None:
#     """
#     Exibe dados cadastrais dos jogadores

#     Args:
#     dados: conjunto de dados sobre o jogador
#     """
#     for k, v in dados.items():
#         print(f" {k}:{v}")


# mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")
# mostrar_jogador(nome="Marta", idade=40, posicao="Atacante", estado="Alagoas")


###################### FIM #########################
# Exercício 12 – Parâmetro normal e **kwargs

# Crie uma função chamada:

# cadastrar_time(nome, **informacoes)
# O nome do time deve ser obrigatório.

# As demais informações podem variar de uma chamada para outra.

# Exemplo:
# cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)

# A função deve mostrar o nome do time e depois todas as informações adicionais recebidas.
###################### ###### #########################


# def cadastrar_time(nome: str, **informacoes) -> None:
#     """
#     Exibe informações sobre o time
#     Args:
#       nome: nome do time
#       informacoes: conjunto de dados sobre o time
#     """
#     print(f"\nSeleção: {nome}")
#     for k, v in informacoes.items():

#         print(f"{k.capitalize()}: {v}")


# cadastrar_time(
#     "Brasil", tecnico="Carlo Ancelotti", continente="América do Sul", titulos=5
# )
# cadastrar_time("Brasil", continente="América do Sul", titulos=5)

###################### FIM #########################

# Exercício 13 – *args e **kwargs juntos

# Crie uma função chamada:

# registrar_partida(time_a, time_b, *eventos, **informacoes):
# Os dois primeiros argumentos devem representar os times da partida.


# Os argumentos posicionais extras devem representar eventos ocorridos durante o jogo.

# Os argumentos nomeados extras devem representar outras informações sobre a partida.


# Exemplo:

# registrar_partida(
# "Brasil",
# "Argentina",
# "Gol do Brasil",
# "Cartão amarelo",
# "Gol da Argentina",
# estadio="Maracanã",
# publico=70000
# ):


# A função deve mostrar:

# Os dois times.
# Todos os eventos recebidos.
# Todas as informações adicionais.

###################### ###### #########################


def registrar_partida(time_a, time_b, *eventos, **informacoes) -> None:
    """
    Exibe informações sobre a partida.

    Args:
        time_a: nome do primeiro time participante da partida.
        time_b: nome do segundo time participante da partida.
        eventos: eventos ocorridos durante o jogo.
        informacoes: outras informações sobre a partida.
    """

    print("\nInformações da partida:")
    print(f"Seleções: {time_a} x {time_b}")

    print("\nEventos:")
    for evento in eventos:
        print(f"- {evento}")

    print("\nInformações adicionais:")
    for k, v in informacoes.items():
        print(f"{k.capitalize()}: {v}")


registrar_partida(
    "Brasil",
    "Argentina",
    "Gol do Brasil",
    "Cartão amarelo",
    "Gol da Argentina",
    estadio="Maracanã",
    publico=70000,
)

###################### FIM #########################
