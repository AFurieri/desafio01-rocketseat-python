def adicionar_contato(contatos, nome, telefone, email):
    """adiciona um contato a lista de contatos"""
    contato = {"nome": nome,
               "telefone": telefone,
               "email": email,
               "favorito": False
               }
    
    contatos.append(contato)

    print(f"contato de {nome} adicionado com sucesso")

    return


def visualizar_contatos(contatos):
    """printa a lista de contatos no terminal"""
    print("\nLista de contatos:\n")
    for i, contato in enumerate(contatos, start=1):
        favorito = "*" if contato["favorito"] else ""
        print(f"{i}. {contato['nome']} / {contato['telefone']} / {contato['email']} {favorito}")
    
    return


def editar_contato(contatos, indice, alterar):
    """permite editar o elemento do contato desejado (nome, telefone ou email)"""
    indice -= 1

    if alterar == "1":
        mudanca = input("digite o novo nome: ")
        contatos[indice]["nome"] = mudanca
        print("nome atualizado com sucesso")

    elif alterar =="2":
        mudanca = input("digite o novo numero: ")
        contatos[indice]["telefone"] = mudanca
        print("telefone atualizado com sucesso")

    elif alterar =="3":
        mudanca = input("digite o novo email: ")
        contatos[indice]["email"] = mudanca
        print("email atualizado com sucesso")

    else:
        print("alternativa inválida")
    
    return


def favoritar(contatos, indice):
    """torna o contato favorito"""
    indice -= 1
    contatos[indice]["favorito"] = True
    print(f"{contatos[indice]['nome']} foi marcado como favorito.")

    return

def desfavoritar (contatos, indice):
    """torna um contato favorito como não favorito"""
    indice -= 1
    contatos[indice]["favorito"] = False
    print(f"{contatos[indice]['nome']} foi desmarcado como favorito.")

    return


def favoritos (contatos):
    print("\nLista de contatos favoritos:\n")
    for i, contato in enumerate(contatos, start= 1):
        if contato["favorito"] == True:
            print(f"{i}. {contato['nome']} / {contato['telefone']} / {contato['email']}") 
    return


lista_contatos = []


while True:
    print("\nMenu da lista de contatos\n")
    print("1. adicionar contato ")
    print("2. visualizar lista de contatos")
    print("3. editar um contato")
    print("4. marcar/desmarcar um contato como favorito")
    print("5. ver lista de contatos favoritos")
    print("6. apagar um contato")
    print("7. sair")

    escolha = input("digite a sua escolha: ")
    print()

    if escolha == "1":
        nome = input("digite o nome do contato que voce deseja adicionar: ")
        telefone = input("digite o telefone do contato que voce deseja adicionar: ")
        email = input("digite o email do contato que voce deseja adicionar: ")
        adicionar_contato(lista_contatos, nome, telefone, email)
    
    elif escolha == "2": 
        visualizar_contatos(lista_contatos)

    elif escolha == "3":
        visualizar_contatos(lista_contatos)
        contato = int(input("digite o indice (numero que fica a frente) do contato que voce deseja atualizar: "))
        print("1. nome")
        print("2. telefone")
        print("3. email")
        alterar = input("digite o que voce deseja alterar no contato ")
        editar_contato(lista_contatos, contato, alterar)
    
    elif escolha == "4":
        visualizar_contatos(lista_contatos)
        indice = int(input("\ndigite o indice do contato (numero que fica a frente dele) que você deseja alterar o favoritismo: "))
        print("\n1. favoritar")
        print("2. desfavoritar")
        status = input("\ndigite o que você deseja fazer: ")

        if status == "1":
            favoritar(lista_contatos, indice)

        elif status == "2":
            desfavoritar(lista_contatos, indice)

        else:
            print("opção inválida!")

    elif escolha == "5":
        favoritos(lista_contatos)


            

    




