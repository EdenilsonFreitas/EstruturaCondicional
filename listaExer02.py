#questao01

# salario = float(input("Digite o salário: R$ ").replace(',', '.'))
# if salario <= 1903.98:
#     aliquota = 0
# elif salario <= 2826.65:
#     aliquota = 0.075
# elif salario <= 3751.05:
#     aliquota = 0.15
# elif salario <= 4664.68:
#     aliquota = 0.225
# else:
#     aliquota = 0.275

# print(f"Imposto a pagar: R$ {salario * aliquota:.2f}")

#questao02

# ano = int(input("Digite um ano: "))
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print(f"O ano {ano} é bissexto.")
# else:
#     print(f"O ano {ano} não é bissexto.")


#questão03
# numero = int(input("Digite um número entre 1 e 10: "))
# if 1 <= numero <= 10:
#     print("O número digitado está DENTRO da faixa solicitada.")
# else:
#     print("O número digitado está FORA da faixa solicitada.")

#questão04
# valor1 = float(input("Digite o primeiro valor: "))
# valor2 = float(input("Digite o segundo valor: "))
# if valor1 > valor2:
#     print(f"O maior valor é: {valor1}")
# elif valor2 > valor1:
#     print(f"O maior valor é: {valor2}")
# else:
#     print("Os valores são iguais.")

# #questão05
# valor1 = int(input("Digite o primeiro valor inteiro: "))
# valor2 = int(input("Digite o segundo valor inteiro: "))
# if valor1 > valor2:
#     diferenca = valor1 - valor2
# elif valor2 > valor1:
#     diferenca = valor2 - valor1
# else:
#     diferenca = 0
# print(f"A diferença entre o maior valor e o menor valor é: {diferenca}")

# #questão06

# valor1 = int(input("Digite o primeiro valor inteiro: "))
# valor2 = int(input("Digite o segundo valor inteiro: "))
# valor3 = int(input("Digite o terceiro valor inteiro: "))
# if valor1 <= valor2 <= valor3:
#     print(f"Os valores em ordem crescente são: {valor1}, {valor2}, {valor3}")
# elif valor1 <= valor3 <= valor2:
#     print(f"Os valores em ordem crescente são: {valor1}, {valor3}, {valor2}")
# elif valor2 <= valor1 <= valor3:
#     print(f"Os valores em ordem crescente são: {valor2}, {valor1}, {valor3}")
# elif valor2 <= valor3 <= valor1:
#     print(f"Os valores em ordem crescente são: {valor2}, {valor3}, {valor1}")
# elif valor3 <= valor1 <= valor2:
#     print(f"Os valores em ordem crescente são: {valor3}, {valor1}, {valor2}")
# else:
#     print(f"Os valores em ordem crescente são: {valor3}, {valor2}, {valor1}")

#questão07
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# n3 = int(input("Digite o terceiro número: "))

# ordem = input("Digite C para crescente ou D para decrescente: ")

# lista = [n1, n2, n3]

# if ordem == "C":
#     lista.sort()
# else:
#     lista.sort(reverse=True)

# print("Resultado:", lista)

#questão08

# lado1 = float(input("Digite o primeiro lado do triângulo: "))
# lado2 = float(input("Digite o segundo lado do triângulo: "))
# lado3 = float(input("Digite o terceiro lado do triângulo: "))
# if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
#     if lado1 == lado2 == lado3:
#         print("O triângulo é equilátero.")
#     elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#         print("O triângulo é isósceles.")
#     else:
#         print("O triângulo é escaleno.")
# else:
#     print("Os lados fornecidos não formam um triângulo.")


