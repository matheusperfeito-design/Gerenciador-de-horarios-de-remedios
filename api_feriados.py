# api_feriados.py

import requests
from datetime import date


def buscar_feriados(ano: int) -> list:
    try:
        url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        return []
    except requests.exceptions.RequestException:
        return []


def verificar_feriado_hoje(feriados: list) -> dict | None:
    hoje = date.today().isoformat()
    for feriado in feriados:
        if feriado.get("date") == hoje:
            return feriado
    return None


def avisar_se_feriado():
    ano = date.today().year
    feriados = buscar_feriados(ano)
    feriado_hoje = verificar_feriado_hoje(feriados)
    if feriado_hoje:
        nome_feriado = feriado_hoje.get("name", "Feriado")
        print(f"\n  ATENCAO: Hoje e feriado ({nome_feriado})!")
        print("  Mesmo assim, nao esqueca dos seus remedios!\n")
