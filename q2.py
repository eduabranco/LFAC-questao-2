# Função auxiliar para contar o número de filhos homens e mulheres em uma string 
# (HM|MH) (h|m)* (( m (h|m)* m (h|m)*) | (h (h|m)*) )

def contar_criancas(familia):
    filhos = familia.count('h')
    filhas = familia.count('m')
    return filhos, filhas

# Função auxiliar para verificar se o casal é heterossexual (homem e mulher)
def verificar_casal_hetero(familia):
    return ('H' in familia[:2] and 'M' in familia[:2]) and (familia[0] != familia[1])

# Função auxiliar para verificar se o casal é homossexual (dois homens ou duas mulheres)
def verificar_casal_homo(familia):
    return (familia[:2] == 'HH' or familia[:2] == 'MM')

# Função principal que avalia a validade do arranjo para cada caso
def is_valid_arrangement(familia, case):
    if len(familia) < 2:
        return False
    
    # Separando o casal (os dois primeiros caracteres) dos filhos (do terceiro em diante)
    couple = familia[:2]
    criancas = familia[2:]
    
    # Contagem de filhos homens e mulheres
    filhos, filhas = contar_criancas(criancas)

    if case == 'a':
        # a) Casais heterossexuais mais velhos que os filhos com pelo menos duas filhas mulheres,
        # ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher.
        if not verificar_casal_hetero(familia):
            return False
        return filhas >= 2 or filhos >= 1

    elif case == 'b':
        # b) Casais heterossexuais mais velhos que os filhos e com uma quantidade ímpar de filhas mulheres.
        if not verificar_casal_hetero(familia):
            return False
        return filhas % 2 != 0

    elif case == 'c':
        # c) Casais heterossexuais mais velhos que os filhos, com a filha mais velha mulher e o filho mais novo homem.
        if not verificar_casal_hetero(familia) or len(criancas) == 0:
            return False
        return criancas[0] == 'm' and criancas[-1] == 'h'

    elif case == 'd':
        # d) Casais homossexuais mais velhos que os filhos, com pelo menos seis filhos,
        # em que os dois primeiros filhos formam um casal e os últimos também.
        if not verificar_casal_homo(familia) or len(criancas) < 6:
            return False
        return criancas[:2] in ['hm', 'mh'] and criancas[-2:] in ['hm', 'mh']

    elif case == 'e':
        # e) Casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado conforme a ordem de nascimento.
        if not verificar_casal_homo(familia):
            return False
        for i in range(len(criancas) - 1):
            if criancas[i] == criancas[i + 1]:
                return False
        return True

    elif case == 'f':
        # f) Casais homossexuais mais velhos que os filhos, com qualquer quantidade de filhos homens e mulheres,
        # mas que não tiveram dois filhos homens consecutivos.
        if not verificar_casal_homo(familia):
            return False
        return 'hh' not in criancas

    elif case == 'g':
        # g) Arranjo de no mínimo x e no máximo y adultos mais velhos que os filhos,
        # com qualquer quantidade de filhos homens e mulheres, mas que os três filhos mais novos não foram homens.
        # Vamos assumir que x = 2 e y = 5 como exemplo.
        x, y = 2, 5
        if not (x <= len(couple) <= y):
            return False
        return not criancas[-3:] == 'hhh'  # Três filhos mais novos não podem ser todos homens

    return False

# Exemplos de uso:
familias = ['MHhmm', 'HHhmhmh', 'MMhmh', 'MHmmmh', 'MMhmhm', 'HHhmm']
for familia in familias:
    print()
    print(f"Familia: {familia}, caso 'a': {is_valid_arrangement(familia, 'a')}")
    print(f"Familia: {familia}, caso 'b': {is_valid_arrangement(familia, 'b')}")
    print(f"Familia: {familia}, caso 'c': {is_valid_arrangement(familia, 'c')}")
    print(f"Familia: {familia}, caso 'd': {is_valid_arrangement(familia, 'd')}")
    print(f"Familia: {familia}, caso 'e': {is_valid_arrangement(familia, 'e')}")
    print(f"Familia: {familia}, caso 'f': {is_valid_arrangement(familia, 'f')}")
    print(f"Familia: {familia}, caso 'g': {is_valid_arrangement(familia, 'g')}")
