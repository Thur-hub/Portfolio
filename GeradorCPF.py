import random

 # Gera 9 digitos aleatórios
for _ in range(100):
    nove_digitos = ''
    contador = 0
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    
    # Faz o calculo para o 10 digito
    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Faz o calculo para o 11 digito
    dez_digitos = f'{nove_digitos}{digito_1}'

    contador_2 = 11

    resultado_2 = 0
    for digito_2 in dez_digitos:
        resultado_2 += int(digito_2) * contador_2
        contador_2 -= 1
    digito_2 = (resultado_2 *10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'
    print(novo_cpf)
