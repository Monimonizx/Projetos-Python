'''
====================================================
ATHON - A melhor Faculdade de Sorocaba
Programa de Introdução à Linguagem Python
Disciplina: Lógica de Programação
Professor: Francisco Tesifom Munhoz
Data: 1° semestre de 2024
====================================================
Atividade: Avaliação Modas
Autor: Laura Monize
Data: 16/05/2024
Comentários: Resolução atividade sequencial para entrega
Sequencial simples
Avaliação Modas
====================================================
'''
#ENTRADA DE DADOS
Nota_1 = int(input("Digita a nota da primeira avaliação: "))
Nota_2 = int(input("Digita a nota da segunda avaliação: "))
Nota_3 = int(input("Digita a nota da terceira avaliação: "))
Nota_4 = int(input("Digita a nota da quarta avaliação: "))

#PROCESSAMENTO DE DADOS
Peso_av1 = (Nota_1 * 2)
Peso_av2 = (Nota_2 * 4)
Peso_av3 = (Nota_3 * 6)
Peso_av4 = (Nota_4 * 8)


#SAÍDA DE DADOS
Media_ponderada = (Peso_av1 + Peso_av2 + Peso_av3 + Peso_av4) / 20
print("Sua média ponderada é de: ", Media_ponderada)