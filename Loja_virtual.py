from Funcoes import *
from Armazenar_dados import *
from ast import literal_eval

texto_menu = 'LOJA VIRTUAL'
opcao_menu = ['LISTAR PRODUTOS', 'LOCALIZAR PRODUTO PELO CÓDIGO','CADASTRAR NOVO PRODUTO', 'ALTERAR PRODUTO', 'EXCLUIR PRODUTO', 'SAIR DO SISTEMA']
categoria_nomes = ['o NOME','a MARCA','a CATEGORIA', 'o VALOR']
categoria = ['nome','marca','categoria','valor']
escolha = 'N'
tamanho_espaco = 83

arq = 'DicionariodeProdutos.txt'

if arquivo_existe(arq) == False:
    criar_arquivo(arq)


produtos = ler_arquivo(arq)
produtos = dict(literal_eval(produtos))

while True:
    try:
        if escolha == 'N':
            menu_cabecalho(texto_menu,tamanho_espaco)
            menu_listar(opcao_menu)
            opcao_escolha = int(input('\nOPÇÃO: '))
            limpar_tela()

        if opcao_escolha == 1:
            menu_cabecalho(opcao_menu[0],tamanho_espaco)
            mostrar_na_tela(produtos)
            soma_media(produtos)
            input('\nAPERTE <ENTRE> PARA VOLTAR!')
            
        elif opcao_escolha == 2:
            menu_cabecalho(opcao_menu[1],tamanho_espaco)
            if produtos == {}:
                escolha = 'N'
                print('*AVISO, NÃO EXISTE NENHUM PRODUTO CADASTRADO!*')
                print('VOLTANDO PARA O MENU...')
                sleep(3)
            else:
                local = localizar_produto(produtos)
                if not local == {}:
                    mostrar_na_tela(local)
                else:
                    print('PRODUTO NÃO ENCONTRADO!')
                escolha = perguntar_novamente('LOCALIZAR UM OUTRO PRODUTO')

        elif opcao_escolha == 3:
            menu_cabecalho(opcao_menu[2],tamanho_espaco)
            castrar_produto(produtos,categoria,categoria_nomes)
            apagar(arq)
            guardar(arq, produtos)
            escolha = perguntar_novamente('CADASTRAR UM NOVO PRODUTO')
                
        elif opcao_escolha == 4:
            menu_cabecalho(opcao_menu[3],tamanho_espaco)
            if produtos == {}:
                escolha = 'N'
                print('*AVISO, NÃO EXISTE NENHUM PRODUTO CADASTRADO!*')
                print('VOLTANDO PARA O MENU...')
                sleep(3)
            else:
                mostrar_na_tela(produtos)
                alterar_produto(produtos,categoria,categoria_nomes)
                limpar_tela() 
                menu_cabecalho(opcao_menu[3],tamanho_espaco)
                mostrar_na_tela(produtos)
                escolha = perguntar_novamente('ALTERAR UM OUTRO PRODUTO')
                
        elif opcao_escolha == 5:
            menu_cabecalho(opcao_menu[4],tamanho_espaco)
            if produtos == {}:
                escolha = 'N'
                print('*NÃO EXISTE NENHUM PRODUTO CADASTRADO!*')
                print('VOLTANDO PARA O MENU...')
                sleep(3)
            else:
                mostrar_na_tela(produtos)
                remover_produto(produtos)
                apagar(arq)
                guardar(arq, produtos)
                limpar_tela()  
                menu_cabecalho(opcao_menu[4],tamanho_espaco)
                mostrar_na_tela(produtos)
                escolha = perguntar_novamente('REMOVE UM OUTRO PRODUTO')
           
        elif opcao_escolha == 6:
            menu_cabecalho(texto_menu,tamanho_espaco)
            print(f'SAINDO DA {texto_menu}...')
            apagar(arq)
            guardar(arq, produtos)
            sleep(2)
            break
        else: 
            print('ERRO! Digite uma opção válida!')
        limpar_tela()          
    except:
        print('ERRO! Digite uma opção válida!')
    
    
