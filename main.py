import PySimpleGUI as gui
import time as t
import keyboard as kb


def storage_layout():
    # this creates the layout of the window
    layout = [[gui.Text("PLEASE INPUT ALL MEASUREMENTS AS CM")],
              [gui.Text("Enter WIDTH of compartment: "), gui.InputText(key='width')],
              # the key is to make it easier to know what values i am retrieving later
              [gui.Text("Enter number of ROWS of compartment: "), gui.InputText(key='rows')],
              [gui.Button("Enter"), gui.Button("Cancel")]
              ]

    # this creates the actual window titled 'Physical space dimensions'
    window = gui.Window("Physical space dimensions", layout)
    return window

def attr_layout():
    layout = [[gui.Text("Enter Album/CD name"), gui.InputText(key="alb_name")],
                   [gui.Text("Enter artist name"), gui.InputText(key="artist_name")],
                   [gui.Button("Enter"), gui.Button("Cancel")]
                   ]
    attr_window = gui.Window("CD attributes", layout)
    return attr_window

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
    # this segment of code was put into a separate function

    while True:
        window = storage_layout()

        event, values = window.read()

        if event == gui.WIN_CLOSED or event == "Cancel":  # if user closes window or clicks cancel
            break

        if event == "Enter":
            try:  # condition to see if user input is a float
                flt_width = float(values["width"])
                flt_rows = float(values["rows"])

                storage_dict = {"width": flt_width, "rows": flt_rows}

                confirm_layout = [[gui.Text(f"You entered:")],
                                  [gui.Text(storage_dict)],
                                  [gui.Button("Confirm"), gui.Button("Cancel")]
                                  ]

                confirm_window = gui.Window("Confirm input ", confirm_layout)

                confirm_event, confirm_values = confirm_window.read()

                if confirm_event == gui.WIN_CLOSED or confirm_event == 'Cancel':
                    pass
                    confirm_window.close()

                if confirm_event == 'Confirm':
                    cd_round = storage_dict['width'] // 1
                    cd_num = cd_round * storage_dict['rows']
                    window.close()
                    confirm_window.close()
                    result = int(cd_num)
                    return result


                    break



            except ValueError as v_error: #if user does not input float this section of code is triggered
                error_layout = [[gui.Text(f"One of your inputs is not valid")],
                                [gui.Text(f"Error: {v_error}")],
                                [gui.Text(f"Please re-enter valid inputs")],
                                [gui.Button("Retry"), gui.Button("Cancel")]
                                ]

                error_window = gui.Window("Error Occurred...", error_layout)

                window.close()

                error_event, error_values = error_window.read()

                if error_event == gui.WIN_CLOSED or error_event == "Cancel":
                    break
                if error_event == "Retry":
                    error_window.close()
                    pass

            '''print("You entered ", values['width'])
            print("You entered ", values['height'])
            print("You entered ", values['depth'])'''

        window.close()


def cd_attributes(cd_num):
    attr_window = attr_layout()

    attr_event, attr_values = attr_window.read()


        if attr_event == gui.WIN_CLOSED or attr_event == "Cancel":
            attr_window.close()

        if attr_event == "Enter":
            try:
                str_album = str(attr_values["alb_name"])
                str_artist = str(attr_values["artist_name"])
                attr_window.close()
            except ValueError as v_error:
                error_layout = [[gui.Text(f"One of your inputs is not valid")],
                                [gui.Text(f"Error: {v_error}")],
                                [gui.Text(f"Please re-enter valid inputs")],
                                [gui.Button("Retry"), gui.Button("Cancel")]
                                ]

                error_window = gui.Window("Error Occurred...", error_layout)

                error_event, error_values = error_window.read()

                if error_event == gui.WIN_CLOSED or error_event == "Cancel":
                    print("window closed?")
                    error_window.close()


                if error_event == "Retry":
                    pass


cd_attributes(storage_input())

'''def pop_up():
    gui.popup("hello world")

pop_up()'''
