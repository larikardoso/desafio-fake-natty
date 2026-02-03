import os
import pytest
from desafio_fake_natty.audio_service import gerar_audio_temporario, limpar_temporario



def test_gerar_audio_cria_arquivo():
    caminho = gerar_audio_temporario("Olá, teste de áudio")

    assert os.path.exists(caminho)

    limpar_temporario(caminho)


def test_gerar_audio_texto_vazio():
    with pytest.raises(ValueError):
        gerar_audio_temporario("   ")


def test_limpar_temporario_remove_arquivo():
    caminho = gerar_audio_temporario("Teste de remoção")

    assert os.path.exists(caminho)

    limpar_temporario(caminho)

    assert not os.path.exists(caminho)
