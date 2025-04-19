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
    print()
    indice = input('Digite o número da tarefa que deseja remover: ')
    tarefa_removida = tarefas.pop(int(indice) - 1)
    print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
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
            listar_tarefa()
        else:
            print('Saindo...')
            break

to_do_list()