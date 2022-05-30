import unicodedata
import re 

def limpar_texto(texto):
    # Remover acentos
    result = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

    # Remover caracteres especiais
    lista = '-#?º°ª.:/;~^`[{]}\\|!$%"\'&*()=+,><\t\r\n…'
    for i in range(0, len(lista)):
        result = result.replace(lista[i], ' ')

    # Transformar em UPPER case
    result = result.upper().strip()

    return result