def desformatar_pis(pis: str) -> str:
    return ''.join(filter(str.isdigit, pis))

def formatar_pis(pis: str) -> str:
    pis = desformatar_pis(pis)
    if len(pis) != 11:
        raise ValueError("PIS deve conter 11 dígitos.")
    return f"{pis[:3]}.{pis[3:8]}.{pis[8:10]}-{pis[10]}"

def gerar_pis(qtd : int) -> list[str]:
    import random
    pises = []
    for _ in range(qtd):
        pis = ''.join(str(random.randint(0, 9)) for _ in range(10))
        pesos = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(pis[i]) * pesos[i] for i in range(10))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        pis += str(digito)
        pises.append(formatar_pis(pis))
    return pises

def validar_pis(pis: str) -> bool:
    pis = ''.join(filter(str.isdigit, pis))

    if len(pis) != 11 or pis == pis[0] * 11:
        return False

    pesos = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(pis[i]) * pesos[i] for i in range(10))
    digito = (soma * 10) % 11
    if digito == 10:
        digito = 0

    return digito == int(pis[10])