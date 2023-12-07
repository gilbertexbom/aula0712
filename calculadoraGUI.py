# Interface gráfica

import PySimpleGUI as psg

import calc

frame_layou = [
    [psg.Radio('Soma', 'RADIO1', key='soma', default=True)],
    [psg.Radio('Subtração', 'RADIO1', key='sub')]
]

layout = [
    [psg.Text('Informe N1: '), psg.InputText('', key='num1'), psg.Frame('Opções: ', frame_layou)],
    [psg.Text('Informe N2: '), psg.InputText('', key='num2')],
    [psg.Text('', key='total')],
    [psg.Button('Calcular'), psg.Button('Limpar')],
]

janela = psg.Window('Calculadora do Tio', layout)

while True:
    evento, valor = janela.read()

    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['num1'].update('')
        janela['num2'].update('')
        janela['total'].update('')
        janela['num1'].set_focus()
        janela['soma'].update(True)
    else:
        # Entradas
        v1 = int(valor['num1'])
        v2 = int(valor['num2'])

        # Processamento
        if valor['soma']:
            total = calc.soma(v1, v2)
        else:
            total = calc.sub(v1, v2)

        # Saída
        janela['total'].update('{}'.format(total))
