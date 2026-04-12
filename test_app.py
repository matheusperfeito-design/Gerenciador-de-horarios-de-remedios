# test_app.py

import os
import pytest
from app import adicionar_remedio, carregar_remedios, remover_remedio, salvar_remedios

ARQUIVO = "remedios.json"


@pytest.fixture(autouse=True)
def limpar_arquivo():
    """Garante que cada teste comeca com arquivo limpo."""
    if os.path.exists(ARQUIVO):
        os.remove(ARQUIVO)
    yield
    if os.path.exists(ARQUIVO):
        os.remove(ARQUIVO)


def test_lista_vazia_sem_arquivo():
    remedios = carregar_remedios()
    assert remedios == []


def test_adicionar_remedio():
    adicionar_remedio("Paracetamol", "08:00", "1 comprimido")
    remedios = carregar_remedios()
    assert len(remedios) == 1
    assert remedios[0]["nome"] == "Paracetamol"
    assert remedios[0]["horario"] == "08:00"
    assert remedios[0]["dosagem"] == "1 comprimido"


def test_adicionar_multiplos_remedios():
    adicionar_remedio("Vitamina C", "07:00", "1 capsula")
    adicionar_remedio("Omeprazol", "19:00", "1 comprimido")
    remedios = carregar_remedios()
    assert len(remedios) == 2


def test_remover_remedio():
    adicionar_remedio("Ibuprofeno", "12:00", "1 comprimido")
    remover_remedio(1)
    remedios = carregar_remedios()
    assert len(remedios) == 0


def test_remover_indice_invalido(capsys):
    adicionar_remedio("Dipirona", "06:00", "1 comprimido")
    remover_remedio(99)
    captured = capsys.readouterr()
    assert "invalido" in captured.out.lower()


def test_salvar_e_carregar():
    dados = [{"nome": "Aspirina", "horario": "10:00", "dosagem": "1 comprimido"}]
    salvar_remedios(dados)
    resultado = carregar_remedios()
    assert resultado == dados
