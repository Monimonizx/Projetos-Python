'''
A FUNÇÃO DESTE PROGRAMA É CALCULAR O SALÁRIO LÍQUIDO DE UM EMPREGADO BASEADO EM SEU SALÁRIO LÍQUIDO,
BASEADO NAS HORAS TRABALHADAS MENSAIS, AUXÍLIO ALIMENTAÇÃO E VALOR  DESCONTADO PELO INSS.
'''
#ENTRADA DE DADOS
Auxilio_Alimentacao = 87
Dias_Trabalhados = 20

#PROCESSAMENTO DE DADOS
Horas_Trabalhadas=float(input("digite horas trabalhadas diariamente: "))
Valor_Por_Hora=float(input("Digite valor recebido por hora trabalhada: "))
Quantidade_Filhos=int(input("Digite quantidade de filhos: "))

#SAÍDA DE DADOS
Horas_Mensal = Horas_Trabalhadas * Dias_Trabalhados
print("O total mensal de horas trabalhadas foi: ", Horas_Mensal)

Salario_Bruto = Valor_Por_Hora * Horas_Mensal
print("Seu salário bruto mensal é de: R$", Salario_Bruto)

Valor_Auxilio = Quantidade_Filhos * Auxilio_Alimentacao
print("Valor recebido em auxílio alimentação: R$", Valor_Auxilio)

Desconto_INSS = Salario_Bruto * (13/100)
print("Desconto INSS: ", Desconto_INSS)

Salario_liquido = Salario_Bruto + Valor_Auxilio
print("Seu salário líquido mensal é de: R$", Salario_liquido)






