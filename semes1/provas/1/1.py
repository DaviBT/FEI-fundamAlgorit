class Prod:
    codigo = 0
    especificacao = ""
    prec = 0

prod1 = Prod()
prod1.codigo = 1
prod1.especificacao = 'cachorro quente'
prod1.preco = 6

prod2 = Prod()
prod2.codigo = 2
prod2.especificacao = 'x-salada'
prod2.preco = 6.5

prod3 = Prod()
prod3.codigo = 3
prod3.especificacao = 'x-bacon'
prod3.preco = 5

prod4 = Prod()
prod4.codigo = 4
prod4.especificacao = 'torrada'
prod4.preco = 3

prod5 = Prod()
prod5.codigo = 5
prod5.especificacao = 'refrigerante'
prod5.preco = 2


codigo = int(input('Digite o código do produto:'))
qnt = int(input('Digite a quantidade do produto:'))

if codigo == 1:
    total = prod1.preco * qnt
    print(f'Total: R$ {total:.2f}')
if codigo == 2:
    total = prod2.preco * qnt
    print(f'Total: R$ {total:.2f}')
if codigo == 3:
    total = prod3.preco * qnt
    print(f'Total: R$ {total:.2f}')
if codigo == 4:
    total = prod4.preco * qnt
    print(f'Total: R$ {total:.2f}')
if codigo == 5:
    total = prod5.preco * qnt
    print(f'Total: R$ {total:.2f}')


