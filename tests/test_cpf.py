from brasildocs.cpf import gerar_cpf, validar_cpf

def test_cpf_valido_formatado():
    assert validar_cpf("529.982.247-25") == True

def test_cpf_valido_sem_formatacao():
    assert validar_cpf("52998224725") == True

def test_cpf_invalido():
    assert validar_cpf("111.111.111-11") == False

def test_cpf_tamanho_errado():
    assert validar_cpf("123") == False

def test_gerar_cpf_quantidade():
    resultado = gerar_cpf(5)
    assert len(resultado) == 5

def test_gerar_cpf_todos_validos():
    for cpf in gerar_cpf(10):
        assert validar_cpf(cpf) == True