movimentacoes = []

def cadastrar_movimentacoes ():
    descricao = str(input("Nome da movimentação: ")).upper().strip()
    while descricao == "":
       descricao = str(input("Nome da movimentação: ")).upper().strip()
    
    tipo = str(input("Tipo (RECEITA/DESPESA): ")).upper()
    while tipo not in ('RECEITA', 'DESPESA'):
       tipo = str(input("Tipo (RECEITA/DESPESA): ")).upper()
    
    categoria = str(input("Classificação do lançamento: ")).upper().strip()
    while categoria == "":
        categoria = str(input("Classificação do lançamento: ")).upper().strip()

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
        
    movimentacao = {
        "descricao": descricao,
        "tipo": tipo,
        "categoria": categoria,
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
        print(f"Descrição: {i['descricao']}")
        print(f"Tipo: {i['tipo']}")
        print(f"Categoria: {i['categoria']}")
        print(f"Valor: {i['valor']:.2f}")
        print ("")

def remover_movimentacoes(movimentacoes):
    if movimentacoes == []:
        print ("Nenhuma movimentação cadastrada!")
    else:
        print ("================== MOVIMENTAÇÕES ==================")
        for i in movimentacoes:
            print(f"Descrição: {i['descricao']}")
            print(f"Tipo: {i['tipo']}")
            print(f"Categoria: {i['categoria']}")
            print(f"Valor: {i['valor']:.2f}")
            print ("")
        escolha_remover = str(input("Escolha qual movimentação deseja remover: (DESCRIÇÃO)")).upper().strip()

        for indice, i in enumerate(movimentacoes):
            if escolha_remover == i['descricao']:
                print ("Movimentação encontrada!")
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
            print(f"Descrição: {i['descricao']}")
            print(f"Tipo: {i['tipo']}")
            print(f"Categoria: {i['categoria']}")
            print(f"Valor: {i['valor']:.2f}")
            print ("")
        escolher_edicao = str(input("Escolha qual movimentação deseja editar: (DESCRIÇÃO)")).upper().strip()

        for indice, i in enumerate(movimentacoes):
            if escolher_edicao == i['descricao']:
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

        else:
            print ("Movimentação NÃO ENCONTRADA!")
