import pandas as pd
from utils import limpar_texto

def carregar_nomes():
    nomes = pd.read_csv("dados/nomes.csv")

    # Limpar first_name para busca
    nomes.first_name = nomes.first_name.apply(limpar_texto)

    return nomes

def obter_dados_por_nome(nomes, meu_nome):
    # Limpar meu_nome para busca
    meu_nome = limpar_texto(meu_nome)

    linha = nomes[nomes.first_name == meu_nome].iloc[0]
    
    return linha

def imprimir_saida(linha):
    texto_saida = f"""Nome: {linha.first_name}
Gênero: {linha.classification}
Probabilidade: {linha.ratio}
Nomes alternativos: {linha.alternative_names}"""
    print(texto_saida)