
import sys


contatos = {}

def menu():
    print("\n--- Agenda de Contatos ---")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar como favorito")
    print("5. Ver contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    favorito = input("Favorito (s/n): ").lower() == 's'
    contatos[nome] = {'telefone': telefone, 'email': email, 'favorito': favorito}
    print(f"Contato {nome} adicionado com sucesso!")

def visualizar_contatos():
    if contatos:
        for nome, dados in contatos.items():
            favorito = "Sim" if dados['favorito'] else "Não"
            print(f"\nNome: {nome}")
            print(f"Telefone: {dados['telefone']}")
            print(f"Email: {dados['email']}")
            print(f"Favorito: {favorito}")
    else:
        print("Nenhum contato encontrado.")

def editar_contato():
    nome = input("Nome do contato a ser editado: ")
    if nome in contatos:
        telefone = input(f"Novo Telefone (atual: {contatos[nome]['telefone']}): ")
        email = input(f"Novo Email (atual: {contatos[nome]['email']}): ")
        favorito = input(f"Favorito (s/n, atual: {'s' if contatos[nome]['favorito'] else 'n'}): ").lower() == 's'
        contatos[nome] = {'telefone': telefone, 'email': email, 'favorito': favorito}
        print(f"Contato {nome} editado com sucesso!")
    else:
        print("Contato não encontrado.")

def marcar_desmarcar_favorito():
    nome = input("Nome do contato para marcar/desmarcar como favorito: ")
    if nome in contatos:
        contatos[nome]['favorito'] = not contatos[nome]['favorito']
        estado = "favorito" if contatos[nome]['favorito'] else "não favorito"
        print(f"Contato {nome} agora está marcado como {estado}.")
    else:
        print("Contato não encontrado.")

def ver_favoritos():
    favoritos = {nome: dados for nome, dados in contatos.items() if dados['favorito']}
    if favoritos:
        for nome, dados in favoritos.items():
            print(f"\nNome: {nome}")
            print(f"Telefone: {dados['telefone']}")
            print(f"Email: {dados['email']}")
    else:
        print("Nenhum contato favorito encontrado.")

def apagar_contato():
    nome = input("Nome do contato a ser apagado: ")
    if nome in contatos:
        del contatos[nome]
        print(f"Contato {nome} apagado com sucesso!")
    else:
        print("Contato não encontrado.")

def main():
    while True:
        escolha = menu()
        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            visualizar_contatos()
        elif escolha == '3':
            editar_contato()
        elif escolha == '4':
            marcar_desmarcar_favorito()
        elif escolha == '5':
            ver_favoritos()
        elif escolha == '6':
            apagar_contato()
        elif escolha == '7':
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
