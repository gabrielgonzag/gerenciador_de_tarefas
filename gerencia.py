import os
 
dados = [] #dicionario aceitará apenas: ['nome', 'descrição', 'status'] por padrão o status será adicionado com FALSE.

def menu_principal():#menuzin estilizado apenas
     print('''
     _______  _______  _______  _______  _        _______ _________         
(  ____ \(  ____ \(  ____ )(  ____ \( (    /|(  ____ \\__   __/|\     /|
| (    \/| (    \/| (    )|| (    \/|  \  ( || (    \/   ) (   ( \   / )
| |      | (__    | (____)|| (__    |   \ | || |         | |    \ (_) / 
| | ____ |  __)   |     __)|  __)   | (\ \) || |         | |     ) _ (  
| | \_  )| (      | (\ (   | (      | | \   || |         | |    / ( ) \ 
| (___) || (____/\| ) \ \__| (____/\| )  \  || (____/\___) (___( /   \ )
(_______)(_______/|/   \__/(_______/|/    )_)(_______/\_______/|/     \|
                                                                        
''')

def voltar_menu():
    input('Digite uma tecla para retornar para o menu principal')
    main()

def opções():#print com as opções e umas viadagem de *
     print('********************************')
     print('1. Iniciar uma nova atividade\n')
     print('2. Exibir atividades existentes\n')
     print('3. Ativar ativiade\n')
     print('4. Excluir ativade\n')
     print('********************************')

def iniciar_atividade():
    os.system('cls')
    nome = input('Digite o nome da atividade ')
    descricao = input(f'Crie uma descrição para a atividade {nome} ')
    dados_atividade = {'nome': nome, 'descricao': descricao, 'status': False}
    dados.append(dados_atividade)
    print(f'Atividade {nome} registrada com sucesso!\n')
    voltar_menu()

def exibir_atividade():
    os.system('cls')
    print('\nLista de Atividades')
    for dado in dados:
        nome_atividade = dado['nome']
        descricao_atividade = dado['descricao']
        status_atividade = dado['status']
        status_atividade_str = "Ativo" if status_atividade else "A fazer"
        print (f'\n.{nome_atividade} | {descricao_atividade} | {status_atividade_str}')
        voltar_menu()

def excluir_atividade():

    os.system('cls')
    if len(dados) == 0:
        print('Nenhuma atividade para excluir.\n')
    else:
        nome_atividade = input('Digite o nome da atividade que deseja excluir: ')
        atividade_encontrada = False

        # Percorrer a lista de atividades para encontrar e remover pelo nome
        for dado in dados:
            if dado['nome'] == nome_atividade:  # Comparação de string diretamente
                dados.remove(dado)  # Remove o dicionário da lista
                print(f'A atividade "{nome_atividade}" foi excluída com sucesso!\n')
                atividade_encontrada = True
                break
        
        if not atividade_encontrada:
            print(f'A atividade "{nome_atividade}" não foi encontrada.\n')

    voltar_menu()

def escolher_opcao():
    try:
        escolha = int(input('DIGITE A OPÇÃO DESEJADA: '))
        if escolha == 1: iniciar_atividade()
        elif escolha == 2: exibir_atividade()
        elif escolha == 3: ativar_atividade()
        elif escolha == 4: excluir_atividade()      
        else: print('Opção Inválida')
            
    except ValueError:
        print('Entrada inválida')
        
def ativar_atividade():
    os.system('cls')

    print('\nLista de Atividades\n')
    print('***********************')
    for dado in dados:
        nome_atividade = dado['nome']
        descricao_atividade = dado['descricao']
        status_atividade = dado['status']
        status_atividade_str = "Ativo" if status_atividade else "A fazer"
        print (f'\n.{nome_atividade} | {descricao_atividade} | {status_atividade_str}')

    atividade_ativa = input('\nDigite o nome da atividade que deseja ativar\n')
    print('*********************')
    for dado in dados:
        if dado['nome'] == atividade_ativa:
            dado['status'] = True
            print(f'Atividade {atividade_ativa} registrada com sucesso!\n')
            break
    if not dado['status']: print(f'Atividade não existe!')
        
    voltar_menu()


def main():
     menu_principal()
     opções()
     escolher_opcao()

if __name__ == '__main__':
     main()
