'''
====================================================
ATHON - A melhor Faculdade de Sorocaba
Programa de Introdução à Linguagem Python
Disciplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: 1° semestre de 2024
====================================================
Atividade: Calculadora
Autor: Laura Monize
Data: 16/05/2024
Comentários: Resolução atividade sequencial para entrega
Sequencial simples
Calculadora
====================================================
'''
#ENTRADA DE DADOS
Num_1 = float(input("Digite o primeiro número: "))
Num_2 = float(input("Digite o segundo número: "))

#PROCESSAMENTO
Adicao = Num_1 + Num_2

Subtracao = Num_1 - Num_2

Multiplicacao = Num_1 * Num_2

Divisao = round(Num_1 / Num_2)

#SAÍDA DE DADOS

print("O resultado da soma é: ", Adicao)

print("O resultado da subtração é de: ",Subtracao)

print("O resultado da Multiplicação é de: ", Multiplicacao)

print("O resultado da divisão é de: ", Divisao)