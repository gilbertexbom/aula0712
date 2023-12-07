# Interface de prompt de comando simples
import calc

while True:
    # Apresentação
    print('\n\t\t\t -- Calculadora -- \n')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Sair')

    # Ler a opção do usuário
    op = int(input('\nOpção: '))

    if op == 1:
        # Entradas
        num1 = int(input('Informe n1: '))
        num2 = int(input('Informe n2: '))

        # Processamento
        total = calc.soma(num1, num2)

        # Saída
        print('{} + {} = {}'.format(num1, num2, total))
    elif op == 2:
        # Entradas
        num1 = int(input('Informe n1: '))
        num2 = int(input('Informe n2: '))

        # Processamento
        total = calc.sub(num1, num2)

        # Saída
        print('{} - {} = {}'.format(num1, num2, total))
    elif op == 3:
        print('Forte abraço!')
        break
    else:
        print(f'\nOpção {op} incorreta!\n')