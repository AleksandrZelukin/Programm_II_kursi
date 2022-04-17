import PySimpleGUI as sg

class logs:
    layot = [[sg.T('Produkts')],[sg.I(key='-IN-')],
             [sg.T('Ievadits')],[sg.T(key='-OUT-')],
             [sg.B('Read'),sg.B('Write'),sg.Exit()]]

    window = sg.Window('Virsraksts', layot)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Write':
            window['-OUT-'],update(values['-IN-'])

    window.close()
                                   
