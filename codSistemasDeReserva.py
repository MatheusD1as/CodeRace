def menu():
    print('''
    1 - Reservar Mesa
    2 - Cancelar reserva
    3 - Ver Mesas disponíveis
    4 - Sair''')
    opcao = int(input("Digite a opção: "))

    return opcao

def reservar(lista1, lista2):
    acao = int(input("Digite a mesa para reservar: "))

    if acao not in lista1:
        print(f"Mesa {acao} já está reservada!")
    else: 
        for itens in lista1:
            if acao == itens:
                lista2.append(acao)
                lista1.remove(acao)
        print(f"Mesa {acao} reservada com sucesso!")
    
    return lista1, lista2

def cancelar(lista1, lista2):
    acao = int(input("Digite a mesa para cancelar a reserva: "))

    if acao not in lista2:
        print(f"A mesa {acao} não está reservada!")
    else:
        for itens in lista2:
            if acao == itens:
                lista1.append(acao)
                lista2.remove(acao)
        print(f"Mesa {acao} tirada da reserva com sucesso!")
    
    return lista1, lista2

def printar(lista1, lista2):
    print("Disponíveis:",lista1)
    print("Reservadas:",lista2)

def main():
    lista_mesas = [1,2,3,4,5]
    lista_reservadas = []

    opc = 0

    while opc != 4:
        opc = menu()

        if opc == 1:
            reservar(lista_mesas, lista_reservadas)
        elif opc == 2:
            cancelar(lista_mesas, lista_reservadas)
        elif opc == 3:
            printar(lista_mesas, lista_reservadas)
        elif opc == 4:
            print("Até mais!")
        else:
            print("Opção inválida!")

main()
