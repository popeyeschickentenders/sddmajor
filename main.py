import PySimpleGUI as gui
import time as t
import keyboard as kb

def storage_layout():
    # this creates the layout of the window
    layout = [[gui.Text("PLEASE INPUT ALL MEASUREMENTS AS CM")],
              [gui.Text("Enter WIDTH of compartment: "), gui.InputText(key='width')],
              # the key is to make it easier to know what values i am retrieving later
              [gui.Text("Enter HEIGHT of compartment: "), gui.InputText(key='height')],
              [gui.Text("Enter DEPTH of compartment: "), gui.InputText(key='depth')],
              [gui.Button("Enter"), gui.Button("Cancel")]
              ]

    # this creates the actual window titled 'Physical space dimensions'
    window = gui.Window("Physical space dimensions", layout)
    return window

def storage_input():
    '''#this creates the layout of the window
    layout = [ [gui.Text("PLEASE INPUT ALL MEASUREMENTS AS CM")],
               [gui.Text("Enter WIDTH of compartment: "), gui.InputText(key='width')],
               [gui.Text ("Enter HEIGHT of compartment: "), gui.InputText(key='height')],
               [gui.Text("Enter DEPTH of compartment: "), gui.InputText(key='depth')],
               [gui.Button("Enter"), gui.Button("Cancel")]
    ]


    #this creates the actual window titled 'Physical space dimensions'
    window = gui.Window ("Physical space dimensions", layout)
'''
#this segment of code was put into a separate

    while True:
        window = storage_layout()

        event, values = window.read()
        flt_width = float(values["width"])
        flt_height = float(values["height"])
        flt_depth = float(values["depth"])

        if event == gui.WIN_CLOSED or event == "Cancel": # if user closes window or clicks cancel
            break

        if event == "Enter":
            try: #condition to see if user input is a float

                return {"width" : flt_width, "height" : flt_height, "depth" : flt_depth}
                break
            except ValueError as v_error:
                error_layout = [[gui.Text(f"One of your inputs is not valid")],
                                [gui.Text(f"Error: {v_error}")],
                                [gui.Text(f"Please re-enter valid inputs")]]

                error_window = gui.Window("Error Occured...", error_layout)
                window.close()
                error_window.read()

                t.sleep(4)
                error_window.close()
                pass


            '''print("You entered ", values['width'])
            print("You entered ", values['height'])
            print("You entered ", values['depth'])'''

    window.close()




gui.popup(storage_input())
'''def pop_up():
    gui.popup("hello world")

pop_up()'''
