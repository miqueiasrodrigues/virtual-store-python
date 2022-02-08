from time import sleep
from prettytable import PrettyTable
import os

def menu_cabecalho(texto, tamanho):
    print(tamanho*'-')
    print(texto.center(tamanho))
    print(tamanho*'-')
     
def menu_listar(lista_menu):
    for i in range(len(lista_menu)):
        print(f'[{i+1}] {lista_menu[i]}')
        
def castrar_produto(produtos,categoria,categoria_nomes):
    novo_produto = {}
    categoria_produtos = {}
    mensagem = ''
    while True:
        codigo = str(input('Digite o CÓDIGO do produto:\t'))
        codigo = codigo.upper()
        if codigo not in produtos.keys():
            for i in range(len(categoria)):
                nome = str(input(f'Digite {categoria_nomes[i]} do produto:\t'))
                nome = nome.upper()
                categoria_produtos[categoria[i]] = nome
            
            novo_produto[codigo] = categoria_produtos
            produtos.update(novo_produto)
            mensagem = 'PRODUTO CADASTRADO COM SUCESSO!'
            break
        else:
            mensagem = 'ERRO! ESSE CÓDIGO JÁ ESTÁ CADASTRADO!'
            print(mensagem)
        mensagem = 'ERRO! PRODUTO NÃO CADASTRADO!'
    return produtos, print(mensagem)

def localizar_produto(produtos):
    produto_obtido = {}
    codigo = str(input('Digite o CÓDIGO do produto:\t'))
    codigo = codigo.upper()
    if codigo in produtos.keys():
        produto_obtido = {codigo:produtos[codigo]}
    return produto_obtido

def remover_produto(produtos):
    codigo = str(input('Digite o CÓDIGO do produto:\t'))
    codigo = codigo.upper()
    if codigo in produtos.keys():
        del produtos[codigo]
        return produtos, print('PRODUTO REMOVIDO COM SUCESSO!')
    else:
        return print('PRODUTO NÃO ENCONTRADO')

def alterar_produto(produtos,categoria,categoria_nomes):
    codigo = str(input('Digite o CÓDIGO do produto:\t'))
    codigo = codigo.upper()
    if codigo in produtos.keys():
        for i in range(len(categoria)):
            nome = str(input(f'Digite {categoria_nomes[i]} do produto:\t'))
            nome = nome.upper()
            produtos[codigo][categoria[i]] = nome    
    else:
        return print('PRODUTO NÃO ENCONTRADO') 
    return produtos

def perguntar_novamente(texto):
    while True:
        escolha = str(input(f'\nDeseja {texto} (S/N): '))
        escolha = escolha.upper()
        if escolha == 'S':
            return escolha
        elif escolha == ''  or escolha == 'N':
            print('OKAY, VOLTANDO PARA O MENU...')
            sleep(2)
            return 'N'

def mostrar_na_tela(produtos):
    categoria = ['CÓDIGO','NOME','MARCA','CATEGORIA','VALOR (R$)']
    x = PrettyTable()
    produtos_lista = []
    chaves_lista = []
    x.field_names = categoria

    chaves_lista = list(produtos.keys())
    contador = 0

    if produtos == {}:
        return print(x)
    else:
        for i in produtos.keys():
            for j in produtos[i]:
                produtos_lista.append(produtos[i][j])
            produtos_lista.insert(0,chaves_lista[contador])
            x.add_row(produtos_lista)
            produtos_lista = []
            contador += 1
        return print(x)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def soma_media(produtos):
    soma = 0
    print(f'O NÚMERO TOTAL DE PRODUTOS É: {len(produtos.keys())}')
    for i in produtos.keys():
        valor = (produtos[i]['valor']).replace(',', '.')
        soma = soma + float(valor)
    print(f'A SOMA DOS VALORES É : R${str(soma).replace(".", ",")}')
    if not produtos == {}:
        print(f'A MÉDIA DOS VALORES É: R${str(round(soma/len(produtos.keys()),2)).replace(".", ",")}')
    
    
