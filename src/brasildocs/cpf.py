import random

def desformatar_cpf(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))

def formatar_cpf(cpf: str) -> str:
    cpf = desformatar_cpf(cpf)
    if len(cpf) != 11:
        raise ValueError("CPF deve conter 11 dígitos.")
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def validar_cpf(cpf: str) -> bool:
    cpf = desformatar_cpf(cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False

    return True

def gerar_cpf(qtd : int) -> list[str]:
    if qtd <= 0:
        raise ValueError("A quantidade de documentos a ser gerada deve ser maior que zero.")
    
    cpfs = []
    for _ in range(qtd):
        
        cpf = ''.join(str(random.randint(0, 9)) for _ in range(9))

        for i in range(9, 11):
            soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digito = (soma * 10) % 11
            if digito == 10:
                digito = 0
            cpf += str(digito)
        cpfs.append(formatar_cpf(cpf))
    return cpfs