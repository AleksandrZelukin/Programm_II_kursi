import PySimpleGUI as sg

class logs:
    layot = [[sg.T('Datoru komponenti:')],
             [sg.I('RAM')],
             [sg.I('HDD',key='-IN-')],
             [sg.I('Video karte',key='-IN-')],
             [sg.I('Procesors CPU',key='-IN-')], 
             [sg.I('Sistemplāte',key='-IN-')],
             [sg.I('Barošanas bloks',key='-IN-')],
             [sg.I('Korpus',key='-IN-')],
             [sg.T(key='-OUT-')],
             [sg.B('Read'),sg.B('Write'),sg.Exit()]]
            

    window = sg.Window('SIA“Personālais dators”', layot)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Write':
            window['-OUT-'],update(values['-IN-'])

    window.close()
