#Em Python, True vale 1 e False vale 0.
# 
print(True + True)    # 2
print(False + 5)      # 5
print(int(True))      # 1
print(int(False))     # 0
print(True == 1)      # True
print(False == 0)     # True

# Conta uma condição
notas = [7, 4, 9, 5, 8]
aprovados = sum(n >= 6 for n in notas)
print(aprovados)  # 3

# avaliar variavel
print(bool(0))      # False
print(bool(""))     # False vazio
print(bool(10))     # True
print(bool("oi"))   # True

x=10
y=20

x /= 5
print(x)
x*=100
print(x)

y+=40
print(y)
y-=50
print(y)

#O operador % (módulo) devolve o resto da divisão.


print(10 % 3)   # 1  (10 dividido por 3 dá 3 e sobra 1)
print(10 % 5)   # 0  (divisão exata, não sobra nada)
print(7 % 2)    # 1
print(2 % 5)    # 2  (5 não cabe em 2, então o resto é o próprio 2)

# Usos comuns do módulo

# Saber se um número é par ou ímpar:

numero = 8
if numero % 2 == 0:
    print("par")
else:
    print("ímpar")

# Saber se um número é divisível por outro:

if 15 % 3 == 0:
    print("15 é divisível por 3")

# Converter minutos em horas e minutos:

total = 135
horas = total // 60      # 2 (parte inteira)
minutos = total % 60     # 15 (o que sobrou)
print(f"{horas}h{minutos}min")   # 2h15min

#Forma abreviada, igual ao /= que você viu antes:

x = 10
x %= 3      # o mesmo que x = x % 3
print(x)    # 1