# Automação de Preenchimento de Formulário com Python + Selenium

Este projeto automatiza o preenchimento de um formulário do Google Forms utilizando a biblioteca Selenium em Python. Os dados dos participantes são fornecidos por meio de uma lista de dicionários no código ou podem ser adaptados para leitura a partir de um arquivo `.xlsx`.

---

## Funcionalidades

- Acessa um link do Google Forms
- Preenche automaticamente os campos:
  - Nome
  - E-mail
  - Telefone
  - Idade
  - Sexo
- Envia o formulário para cada pessoa da lista

---

## Tecnologias Utilizadas

- Python
- Selenium
- Pandas (opcional, para leitura de Excel)
- Google Chrome + ChromeDriver

---

## Estrutura do Projeto
├── scr/

│ ├── automacao_python_lista.py # Automação via lista de dicionários no código

│ └── automacao_python_arquivo.py # Automação via planilha Excel

├── .gitignore

├── README.md


└── requirements.txt

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Execute o script Python:
```bash
python automacao_python_lista.py
OU
automacao_python_arquivo.py
```