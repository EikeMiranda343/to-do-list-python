tarefas = []
tarefas_concluidas = {}

def menu ():
    print('1. Adicionar tarefa')
    print('2. Concluir tarefa')
    print('3. Listar tarefas')
    print('4. Remover tarefa')
    print('5. Sair da aplicação')
    print()

def adicionar_tarefa ():
    tarefa = input('Qual tarefa você deseja adicionar? ')
    nova_tarefa = {"tarefa": tarefa, "concluida": False}
    tarefas.append(nova_tarefa)
    print('Tarefa adicionada com sucesso!')

def listar_tarefa ():
    if not tarefas:
        print('Você não adicionou nenhuma tarefa!')
    else:
        for i, tarefa in enumerate(tarefa, start = 1):
            print(tarefa[i])


adicionar_tarefa()
