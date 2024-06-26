import json

# arquivo onde os contatos serão salvos
arquivo_contatos = 'contatos.json'

# Função para carregar os contatos de um arquivo JSON
def carregar_contatos():
    try:
        with open(arquivo_contatos, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Função para salvar os contatos em um arquivo JSON
def salvar_contatos():
    with open(arquivo_contatos, 'w') as file:
        json.dump(contatos, file, indent=4)

# Iniciando um dicionário vazio
contatos = carregar_contatos()

# Função para adicionar novos contatos
def adicionar_contato(nome, telefone, email):
    contatos[nome] = {'telefone': telefone, 'email': email}
    print(f'Contato {nome} adicionado com sucesso.')

# Função para remover um contato existente
def remover_contato(nome):
    if nome in contatos:
        del contatos[nome]
        print(f'Contato {nome} removido com sucesso.')
    else:
        print(f'Contato {nome} não encontrado.')

# Função para atualizar os detalhes de um contato
def atualizar_contato(nome, telefone=None, email=None):
    if nome in contatos:
        if telefone:
            contatos[nome]['telefone'] = telefone
        if email:
            contatos[nome]['email'] = email
        print(f'Contato {nome} atualizado com sucesso.')
    else:
        print(f'Contato {nome} não encontrado.')

# Função para buscar um contato pelo nome
def buscar_contato(nome):
    if nome in contatos:
        return contatos[nome]
    else:
        print(f'Contato {nome} não encontrado.')
        return None

# Função para exibir todos os contatos
def exibir_contatos():
    if contatos:
        print("\nLista de Contatos:")
        print("------------------")
        # Ordenar contatos alfabeticamente pelo nome
        contatos_ordenados = sorted(contatos.items())
        for nome, detalhes in contatos_ordenados:
            print(f'Nome: {nome}')
            print(f'Telefone: {detalhes["telefone"]}')
            print(f'Email: {detalhes["email"]}')
            print("------------------")
    else:
        print('Nenhum contato encontrado.')

# Função principal para interagir com o usuário
def menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("--------------")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Atualizar contato")
        print("4. Buscar contato")
        print("5. Exibir todos os contatos")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_contato(nome, telefone, email)
        elif escolha == '2':
            nome = input("Nome do contato a ser removido: ")
            remover_contato(nome)
        elif escolha == '3':
            nome = input("Nome do contato a ser atualizado: ")
            telefone = input("Novo Telefone (pressione enter para manter o atual): ")
            email = input("Novo Email (pressione enter para manter o atual): ")
            atualizar_contato(nome, telefone if telefone else None, email if email else None)
        elif escolha == '4':
            nome = input("Nome do contato a ser buscado: ")
            contato = buscar_contato(nome)
            if contato:
                print(f'Nome: {nome}, Telefone: {contato["telefone"]}, Email: {contato["email"]}')
        elif escolha == '5':
            exibir_contatos()
        elif escolha == '6':
            salvar_contatos()
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciando o programa
menu()