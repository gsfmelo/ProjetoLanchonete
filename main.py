print('Seja bem-vindo à lanchonete de Geovanna Melo! RU: 4466904\n') # Apresentação da lanchonete
print("*--------------- CARDÁPIO -----------------*") # Cardápio da lanchonete
print('Código |        Descrição      | Valor(R$)')
print('  100  |    Cachorro-quente    |    9,00')
print('  101  | Cachorro-quente duplo |   11,00')
print('  102  |        X-Egg          |   12,00')
print('  103  |       X-Salada        |   13,00')
print('  104  |       X-Bacon         |   14,00')
print('  105  |       X-Tudo          |   17,00')
print('  200  |   Refrigerante Lata   |    5,00')
print('  201  |      Chá Gelado       |    4,00')
print('*------------------------------------------*\n')

subtotal = 0 # Atribui 0 ao início

while True:
    codigo = input('Digite o código do lanche desejado (100/101/102/103/104/105/200/201): ') # Pede para o cliente digitar o código que deseja.
    if codigo != '100' and codigo != '101' and codigo != '101' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201':
        print('Opção inválida.') # Loop de código escolhido
        continue
    if codigo == '100':
        print('Você escolheu um Cachorro-quente no valor de R$ 9,00')
        subtotal += 9
    if codigo == '101':
        print('Você escolheu um Cachorro-quente Duplo no valor de R$ 11,00')
        subtotal += 11
    elif codigo == '102':
        print('Você escolheu um X-Egg no valor de R$ 12,00')
        subtotal += 12
    elif codigo == '103':
        print('Você escolheu um X-Salada no valor de R$ 13,00')
        subtotal += 13
    elif codigo == '104':
        print('Você escolheu um X-Bacon no valor de R$ 14,00')
        subtotal += 14
    elif codigo == '105':
        print('Você escolheu um X-Tudo no valor de R$ 17,00')
        subtotal += 17
    elif codigo == '200':
        print('Você escolheu um Refrigerante Lata no valor de R$ 5,00')
        subtotal += 5
    elif codigo == '201':
        print('Você escolheu um Chá Gelado no valor de R$ 4,00')
        subtotal += 4

    mais_pedidos = input('Deseja fazer mais algum pedido?(S/N): ') # Pergunta se o cliente desejar fazer outro pedido.
    mais_pedidos = mais_pedidos.upper() # Conta o pedido mesmo se o cliente digitar S ou N maiúsculos ou minúsculos
    if mais_pedidos == 'S': # Volta ao início do loop para o cliente fazer outro pedido
        continue
    else:
        mais_pedidos == 'N' # Encerra o pedido, o programa e mostra o valor total
        print('O valor total é: R${:.2f}'.format(subtotal))
        break



