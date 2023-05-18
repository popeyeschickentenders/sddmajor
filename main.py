import PySimpleGUI as gui

def storage_space():

    #this is the layout for the window
    layout = [ [gui.Text("PLEASE INPUT ALL MEASUREMENTS AS CM")],
               [gui.Text("Enter text:"), gui.InputText()],
               [sg.Button('Enter'), sg.Button('Cancel')]
    ]


#this creates the window
    window = gui.Window ("Physical space dimensions", layout)

    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
    print('You entered ', values[0])

window.close()

storage_space()