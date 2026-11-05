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


cadastrar_movimentacoes()
print ('-'*30)
cadastrar_movimentacoes()
print ('-'*30)
cadastrar_movimentacoes()
print ('-'*30)

saldo_disponivel,total_despesa, total_receita = calcular_saldo(movimentacoes)

print (f"Receitas: R${total_receita:.2f}")
print (f"Despesas: R${total_despesa:.2f}")
print (f"Saldo diponível: R${saldo_disponivel:.2f}")

listar_movimentacoes(movimentacoes)