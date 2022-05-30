# Projeto Zero - Gênero

Script que recebe um __primeiro__ nome como argumento e retorna dados de gênero, a saber: gênero mais provável, probabilidade e nomes alternativos.

## Desenvolvimento

- Environment:

```
pip install virtualenv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Environment (Windows):

```
pip install virtualenv
virtualenv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Como Executar

- Script principal: `obter_genero.py`
- Argumentos:
  - __meu_nome__: Primeiro nome a buscar dados de gênero.
- Execução:
  - `python obter_genero.py --meu-nome Ricardo`
