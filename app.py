# app.py

import json
import os

ARQUIVO = "remedios.json"


def carregar_remedios():
    """Le os remedios salvos no arquivo JSON."""
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_remedios(remedios):
    """Salva a lista de remedios no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(remedios, f, ensure_ascii=False, indent=2)


def adicionar_remedio(nome, horario, dosagem):
    """Adiciona um novo remedio a lista."""
    remedios = carregar_remedios()
    remedio = {
        "nome": nome,
        "horario": horario,
        "dosagem": dosagem
    }
    remedios.append(remedio)
    salvar_remedios(remedios)
    print(f"\n Remedio '{nome}' adicionado para as {horario}!\n")


def listar_remedios():
    """Mostra todos os remedios cadastrados."""
    remedios = carregar_remedios()
    if not remedios:
        print("\n Nenhum remedio cadastrado ainda.\n")
        return
    print("\n Remedios cadastrados:")
    for i, r in enumerate(remedios, 1):
        print(f"  {i}. {r['nome']} - {r['dosagem']} - as {r['horario']}")
    print()


def remover_remedio(indice):
    """Remove um remedio pelo numero na lista."""
    remedios = carregar_remedios()
    if indice < 1 or indice > len(remedios):
        print("\n Numero invalido.\n")
        return
    removido = remedios.pop(indice - 1)
    salvar_remedios(remedios)
    print(f"\n '{removido['nome']}' removido com sucesso!\n")


def menu():
    """Loop principal do programa."""
    while True:
        print("=====================================")
        print("   Gerenciador de Remedios           ")
        print("=====================================")
        print("1 - Adicionar remedio")
        print("2 - Listar remedios")
        print("3 - Remover remedio")
        print("4 - Sair")
        print("=====================================")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            nome = input("Nome do remedio: ").strip()
            horario = input("Horario (ex: 08:00): ").strip()
            dosagem = input("Dosagem (ex: 1 comprimido): ").strip()
            adicionar_remedio(nome, horario, dosagem)

        elif opcao == "2":
            listar_remedios()

        elif opcao == "3":
            listar_remedios()
            try:
                indice = int(input("Numero do remedio a remover: "))
                remover_remedio(indice)
            except ValueError:
                print("\n Digite um numero valido.\n")

        elif opcao == "4":
            print("\nAte logo!\n")
            break

        else:
            print("\n Opcao invalida.\n")


if __name__ == "__main__":
    menu()
