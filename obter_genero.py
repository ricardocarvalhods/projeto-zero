import argparse
import nomes

# Para execucao via outro modulo
def main(args):
    df_nomes = nomes.carregar_nomes()

    meu_nome = args.meu_nome
    linha = nomes.obter_dados_por_nome(df_nomes, meu_nome)

    nomes.imprimir_saida(linha)

# Para execucao direta via linha de comando
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--meu-nome', type=str, help="Nome a buscar dados de genero.")

    arguments, _ = parser.parse_known_args()

    main(arguments)
