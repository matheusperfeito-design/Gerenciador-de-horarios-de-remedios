# test_api_feriados.py

from unittest.mock import patch, Mock
from api_feriados import buscar_feriados, verificar_feriado_hoje


FERIADOS_SIMULADOS = [
    {"date": "2025-01-01", "name": "Confraternizacao Mundial", "type": "national"},
    {"date": "2025-04-21", "name": "Tiradentes", "type": "national"},
    {"date": "2025-12-25", "name": "Natal", "type": "national"},
]


def test_buscar_feriados_sucesso():
    with patch("api_feriados.requests.get") as mock_get:
        mock_get.return_value = Mock(
            status_code=200,
            json=lambda: FERIADOS_SIMULADOS
        )
        resultado = buscar_feriados(2025)
    assert isinstance(resultado, list)
    assert len(resultado) == 3
    assert resultado[0]["name"] == "Confraternizacao Mundial"


def test_buscar_feriados_falha_api():
    with patch("api_feriados.requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=500)
        resultado = buscar_feriados(2025)
    assert resultado == []


def test_buscar_feriados_sem_conexao():
    import requests
    with patch("api_feriados.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        resultado = buscar_feriados(2025)
    assert resultado == []


def test_verificar_feriado_encontrado():
    feriados = [{"date": "2025-12-25", "name": "Natal", "type": "national"}]
    with patch("api_feriados.date") as mock_date:
        mock_date.today.return_value.isoformat.return_value = "2025-12-25"
        resultado = verificar_feriado_hoje(feriados)
    assert resultado is not None
    assert resultado["name"] == "Natal"


def test_verificar_feriado_nao_encontrado():
    feriados = [{"date": "2025-12-25", "name": "Natal", "type": "national"}]
    with patch("api_feriados.date") as mock_date:
        mock_date.today.return_value.isoformat.return_value = "2025-07-10"
        resultado = verificar_feriado_hoje(feriados)
    assert resultado is None
