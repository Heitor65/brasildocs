from brasildocs.cnpj import gerar_cnpj, validar_cnpj

def test_cnpj_valido_formatado():
    assert validar_cnpj("02.998.101/0001-29") == True

def test_cnpj_valido_sem_formatacao():
    assert validar_cnpj("02998101000129") == True

def test_cnpj_invalido():
    assert validar_cnpj("02238101000129") == False

def test_cnpj_tamanho_invalido():
    assert validar_cnpj("124") == False

def test_gerar_cnpj_quantidade():
    assert len(gerar_cnpj(5)) == 5
    
def test_gerar_cnpj_valido():
    for cnpj in gerar_cnpj(10):
        assert validar_cnpj(cnpj) == True