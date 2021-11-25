import PySimpleGUI as sg

cities = ('Sofia', 'Plovdiv', 'Varna')
products = ('banana', 'water', 'juice', 'sweets', 'peanuts')

sg.theme('BluePurple')
layout = [
    [sg.Text('Quantity:'),
     sg.InputText('0', key='quantity', size=(15, 1)),
     sg.Combo(products, readonly=True, default_value='water', key='products'),
     sg.Combo(cities, readonly=True, default_value='Sofia', key='cities'),
     ],
    [sg.Text('Price:', size=(9, 1)),
     sg.Text('0', key='output', size=(25, 1)),
     sg.Submit('Calculate')]
]

window = sg.Window('Shop Example', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Calculate':
        price = 0
        if values['cities'] == 'Sofia':
            if values['products'] == 'banana':
                price = 3.1
            elif values['products'] == 'water':
                price = 0.8
            elif values['products'] == 'juice':
                price = 1.2
            elif values['products'] == 'sweets':
                price = 1.45
            else:
                price = 1.6
        elif values['cities'] == 'Plovdiv':
            if values['products'] == 'banana':
                price = 3
            elif values['products'] == 'water':
                price = 0.7
            elif values['products'] == 'juice':
                price = 1.15
            elif values['products'] == 'sweets':
                price = 1.3
            else:
                price = 1.5
        else:
            if values['products'] == 'banana':
                price = 3.15
            elif values['products'] == 'water':
                price = 0.7
            elif values['products'] == 'juice':
                price = 1.1
            elif values['products'] == 'sweets':
                price = 1.35
            else:
                price = 1.55
        all = round(price*float(values['quantity']), 2)
        window['output'].update(str(all)+' BGN')
window.close()
