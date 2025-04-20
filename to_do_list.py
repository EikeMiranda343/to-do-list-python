tarefas = []

def menu():
    print('Menu - Escolha uma opção: ')
    print('1. Adicionar tarefa')
    print('2. Listar tarefas')
    print('3. Remover tarefa')
    print('4. Marcar tarefa como concluída')
    print('5. Sair')

def adicionar_tarefa():
    tarefa = input('Digite a tarefa: ')
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada com sucesso!')
    print()

def listar_tarefa():
    for i in range(0, len(tarefas)):
        print(f'{i + 1} - {tarefas[i]}')
    print()

def remover_tarefa():
    listar_tarefa()
    indice = int(input('Digite o número da tarefa que deseja remover: ')) - 1
    tarefa_removida = tarefas.pop(indice)
    print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
    print()

def concluir_tarefa():
    listar_tarefa()
    if tarefas:
        indice = int(input('Digite o número da tarefa que deseja concluir: ')) - 1
        print()
        if 0 <= indice <= len(tarefas):
            tarefas[indice] = tarefas[indice].replace(' - Concluída', '')
            tarefa_concluida = tarefas[indice] + ' - Concluída'
            tarefas[indice] = tarefa_concluida
            print(f'Tarefa "{tarefa_concluida}" marcada como concluída!')
            print()


def to_do_list():
    while True:
        menu()
        opcao = int(input('Escolha uma opção: '))
        print()
        if opcao == 1:
            adicionar_tarefa()
        elif opcao == 2:
            listar_tarefa()
        elif opcao == 3:
            remover_tarefa()
        elif opcao == 4:
            concluir_tarefa()
        else:
            print('Saindo...')
            break

to_do_list()