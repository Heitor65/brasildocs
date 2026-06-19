def desformatar_cnpj(cnpj: str) -> str:
    return cnpj.replace('.', '').replace('/', '').replace('-', '')

def formatar_cnpj(cnpj: str) -> str:
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

def validar_cnpj(cnpj: str) -> bool:
    cnpj = desformatar_cnpj(cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    for i in range(12, 14):
        soma = sum(int(cnpj[j]) * (i - j) for j in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cnpj[i]):
            return False

    return True

def gerar_cnpj(qtd : int) -> list[str]:
    import random
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