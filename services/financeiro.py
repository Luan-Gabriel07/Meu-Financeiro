from datetime import datetime
import uuid # permite gerar identificadores únicos automaticamente.

movimentacoes = []

def cadastrar_movimentacoes (movimentacoes):
    descricao = str(input("Nome da movimentação: ")).upper().strip()
    while descricao == "":
       descricao = str(input("Nome da movimentação: ")).upper().strip()
    
    tipo = str(input("Tipo (RECEITA/DESPESA): ")).upper()
    while tipo not in ('RECEITA', 'DESPESA'):
       tipo = str(input("Tipo (RECEITA/DESPESA): ")).upper()
    
    categoria = str(input("Classificação do lançamento: ")).upper().strip()
    while categoria == "":
        categoria = str(input("Classificação do lançamento: ")).upper().strip()

    data = str(input("Data (DD/MM/AAAA): "))
    while True:
        try:
            data = datetime.strptime(data, "%d/%m/%Y") #converte uma string em uma data
            break
        except ValueError:
            print ("Digite uma data válida!")
            data = str(input("Digite novamente a data (DD/MM/AAAA): "))

    while True:

        ''' try/except: impede que o programa seja encerrado quando o 
        usuário digitar algo que não seja número.
        '''

        try: # o Python tenta executar o código que está dentro dele.
            valor = float(input("Valor: R$"))
            if valor > 0: 
                break
            else: 
                print ("O valor precisa ser maior que zero!")
        except  ValueError: # se acontecer um erro do tipo especificado, o Python executa o código dentro do except.
            print ("Digite um número válido!")

    id_movimentacao = str(uuid.uuid4())
        
    movimentacao = {
        "id": id_movimentacao,
        "descricao": descricao,
        "tipo": tipo,
        "categoria": categoria,
        "data": data,
        "valor": valor
    }

    movimentacoes.append(movimentacao)

def calcular_saldo(movimentacoes):
    total_receita = 0
    total_despesa = 0
    for i in movimentacoes:
        if i['tipo'] == 'RECEITA':
            total_receita += i['valor']
        elif i['tipo'] == 'DESPESA':
            total_despesa += i['valor']
    saldo_disponivel = total_receita - total_despesa
    return saldo_disponivel,total_despesa,total_receita

def listar_movimentacoes(movimentacoes):
    print ("================== MOVIMENTAÇÕES ==================")
    for i in movimentacoes:
        print (f"ID: {i['id']}")
        print(f"Descrição: {i['descricao']}")
        print(f"Tipo: {i['tipo']}")
        print(f"Categoria: {i['categoria']}")
        print(f"Data: {i['data'].strftime('%d/%m/%Y')}") #transforma um objeto datetime em uma string formatada.
        print(f"Valor: {i['valor']:.2f}")
        print ("")

def remover_movimentacoes(movimentacoes):
    if movimentacoes == []:
        print ("Nenhuma movimentação cadastrada!")
    else:
        print ("================== MOVIMENTAÇÕES ==================")
        for i in movimentacoes:
            print (f"ID: {i['id']}")
            print(f"Descrição: {i['descricao']}")
            print(f"Tipo: {i['tipo']}")
            print(f"Categoria: {i['categoria']}")
            print(f"Data: {i['data'].strftime('%d/%m/%Y')}") 
            print ("")
        escolha_remover = str(input("Escolha qual movimentação deseja remover (ID): ")).strip()

        for indice, i in enumerate(movimentacoes):
            if escolha_remover == i['id']:
                print ("Movimentação REMOVIDA!")
                movimentacoes.pop(indice)
                break
        else:
            print  ("Movimentação não encontrada!")

def editar_movimentacoes(movimentacoes):
    if movimentacoes == []:
        print ("Nenhuma movimentação cadastrada!")
    else:
        print ("================== MOVIMENTAÇÕES ==================")
        for i in movimentacoes:
            print (f"ID: {i['id']}")
            print(f"Descrição: {i['descricao']}")
            print(f"Tipo: {i['tipo']}")
            print(f"Categoria: {i['categoria']}")
            print(f"Data: {i['data'].strftime('%d/%m/%Y')}") 
            print ("")
        escolher_edicao = str(input("Escolha qual movimentação deseja editar (ID): ")).strip()

        for indice, i in enumerate(movimentacoes):
            if escolher_edicao == i['id']:
                elemento_editado = str(input("Qual elemento você quer editar: ")).upper().strip()

                if elemento_editado == 'DESCRIÇÃO':
                    nova_descricao = str(input("Informe a nova DESCRIÇÃO: ")).upper().strip()
                    while nova_descricao == "":
                           nova_descricao = str(input("Informe a nova DESCRIÇÃO: ")).upper().strip()
                    i['descricao'] = nova_descricao
                    print ("Movimentação editada com sucesso!")

                elif elemento_editado == 'TIPO':
                    novo_tipo = str(input("Informe o novo TIPO: (RECEITA/DESPESA) ")).upper().strip()
                    while novo_tipo not in ('RECEITA', 'DESPESA'):
                        novo_tipo = str(input("Informe o novo TIPO: (RECEITA/DESPESA) ")).upper().strip()
                    i['tipo'] = novo_tipo
                    print ("Movimentação editada com sucesso!")

                elif elemento_editado == 'CATEGORIA':
                    nova_categoria = str(input("Informe a nova CATEGORIA: ")).upper().strip()
                    while nova_categoria == "":
                        nova_categoria = str(input("Informe a nova CATEGORIA: ")).upper().strip()
                    i['categoria'] = nova_categoria
                    print ("Movimentação editada com sucesso!")

                elif elemento_editado == 'DATA':
                    nova_data = str(input("Informe a nova data (DD/MM/AAAA): "))
                    while True:
                        try:
                            nova_data = datetime.strptime(nova_data, "%d/%m/%Y")
                            break
                        except ValueError:
                            print("Data inválida!")
                            nova_data = str(input("Informe a nova data novamente (DD/MM/AAAA): "))
                    i['data'] = nova_data
                    print ("Movimentação editada com sucesso!")

                elif elemento_editado == 'VALOR':
                    while True:
                        try:
                            novo_valor = float(input("Informe o novo VALOR: R$"))
                            if novo_valor > 0:
                                break
                            else:
                                print("O valor precisa ser maior que zero!")
                        except ValueError:
                            print ("Digite um número válido")
                    i['valor'] = novo_valor
                    print ("Movimentação editada com sucesso!")
                break

        else:
            print ("Movimentação NÃO ENCONTRADA!")


# TESTES DO SISTEMA

while True:
    print("\n========== MEU FINANCEIRO ==========")
    print("1 - Cadastrar movimentação")
    print("2 - Listar movimentações")
    print("3 - Editar movimentação")
    print("4 - Remover movimentação")
    print("5 - Calcular saldo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_movimentacoes(movimentacoes)

    elif opcao == '2':
        listar_movimentacoes(movimentacoes)

    elif opcao == '3':
        editar_movimentacoes(movimentacoes)

    elif opcao == '4':
        remover_movimentacoes(movimentacoes)

    elif opcao == '5':
        saldo, despesas, receitas = calcular_saldo(movimentacoes)
        print(f"\nReceitas: R$ {receitas:.2f}")
        print(f"Despesas: R$ {despesas:.2f}")
        print(f"Saldo disponível: R$ {saldo:.2f}")

    elif opcao == '0':
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")