# 💊 Gerenciador de Horários de Remediações
🌐 **Deploy:** https://github.com/matheusperfeito-design/Gerenciador-de-horarios-de-remedios

Aplicação de linha de comando (CLI) desenvolvida em Python para auxiliar no controle de remédios e horários, especialmente útil para idosos ou cuidadores que precisam organizar múltiplos medicamentos.

## 🎯 Problema que resolve

Muitas pessoas, especialmente idosos, têm dificuldade em lembrar quais remédios tomar, em qual horário e em qual dosagem. Essa aplicação permite cadastrar, listar e remover remédios de forma simples, salvando tudo em um arquivo local.

## 👥 Quem é beneficiado

- Idosos que tomam múltiplos medicamentos
- Cuidadores e familiares responsáveis por rotinas de medicação

## 🚀 Como usar

### Pré-requisitos

- Python 3.11 ou superior instalado

### Instalação

```bash
# Clone o repositório
git clone https://github.com/matheusperfeito-design/Gerenciador-de-horarios-de-remediacoes.git

# Entre na pasta
cd Gerenciador-de-horarios-de-remediacoes

# Instale as dependências
pip install -r requirements.txt
```

### Executar o programa

```bash
python app.py
```

### Menu do programa

```
=====================================
   Gerenciador de Remedios
=====================================
1 - Adicionar remedio
2 - Listar remedios
3 - Remover remedio
4 - Sair
=====================================
```

## 🧪 Testes

```bash
pytest test_app.py -v
```

## 🔍 Linting

```bash
flake8 app.py test_app.py --max-line-length=100
```

## 📁 Estrutura do projeto

```
Gerenciador-de-horarios-de-remediacoes/
├── app.py              # Programa principal
├── test_app.py         # Testes automatizados
├── requirements.txt    # Dependências
├── README.md           # Este arquivo
└── .github/
    └── workflows/
        └── ci.yml      # CI com GitHub Actions
```

## 🗃️ Armazenamento

Os dados são salvos localmente em um arquivo `remedios.json`, criado automaticamente na primeira execução.

## 📌 Versionamento

Este projeto segue o padrão de [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## 👤 Autor

**matheusperfeito-design**
