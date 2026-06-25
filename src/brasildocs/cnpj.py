import random

def desformatar_cnpj(cnpj: str) -> str:
    return cnpj.replace('.', '').replace('/', '').replace('-', '')

def formatar_cnpj(cnpj: str) -> str:
    cnpj = desformatar_cnpj(cnpj)
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

def validar_cnpj(cnpj: str) -> bool:
    cnpj = desformatar_cnpj(cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    soma = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return digito1 == int(cnpj[12]) and digito2 == int(cnpj[13])

def gerar_cnpj(qtd : int) -> list[str]:
    if qtd <= 0:
        raise ValueError("A quantidade de documentos a ser gerada deve ser maior que zero.")
    
    cnpjs = []
    for _ in range(qtd):
        cnpj = ''.join(str(random.randint(0, 9)) for _ in range(12))
        for i in range(12, 14):
            soma = sum(int(cnpj[j]) * (i - j) for j in range(i))
            digito = (soma * 10) % 11
            if digito == 10:
                digito = 0
            cnpj += str(digito)
        cnpjs.append(formatar_cnpj(cnpj))

    return cnpjs