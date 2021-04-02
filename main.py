from usuario import Usuario #Criando uma pessoa e instanciando na main por meio de orientação a objeto

continuar = 1
lista_usuarios = []

while continuar != 0:
    try:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))
        sobrenome = input("Digite o seu sobrenome: ")
        usuario = Usuario(nome, idade, sobrenome)
        lista_usuarios.append(usuario) #metodo "append" insere os usuarios em uma lista

        if usuario.idade == 99:
            break
        if usuario.idade == 98:
            continue

        print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")

        if usuario.idade <= 17:
            print(f"{usuario.nome} é adolescente")
        elif usuario.idade >= 18 and usuario.idade <= 50:
            print(f"{usuario.nome} é adulto")
        else:
            print(f"{usuario.nome} é idoso")
        continuar = int(input("Deseja continuar cadastrando? 0 - Sair 1 - Continuar "))
    except ValueError: #cria uma execeção caso o usuário digite letras na idade ou nas opções de continuar
        print("você deve informa um número válido para idade")
else:
    print("Lista de usuarios cadastrados: ")

    for x in lista_usuarios: #atraves do for conseguimos ter acesso a lista de todos os usuários cadastrados
        print(f"Nome completo: {x.nome} {x.sobrenome} - idade {x.idade}")

    print("Fim O loop")







