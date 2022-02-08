def arquivo_existe(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except:
        return False

def criar_arquivo(arq):
    a = open(arq, 'wt+')
    a.write(f'{{}}')
    a.close()

def ler_arquivo(arq):
    a = open(arq, 'rt')
    conteudo = a.read()
    a.close()
    return conteudo

def guardar(arq, produtos):
    a = open(arq, 'at')
    a.write(f'{produtos}')
    a.close()

def apagar(arq):
    open(arq, 'w').close()
