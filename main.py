import json.decoder
import PySimpleGUI as gui
import time as t
import keyboard as kb
import json as js
import random

'''def  temp_num():
    return 3'''

def driver_num():
    random_int = random.randint(0,10)
    return random_int

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
    '''print("cd attr ran")'''
    attr_list = []
    for i in range(cd_num): #i only want it to run one less than the number because i need to add comma to make it a valid list, if it adds comma to last one it raises error

        attr_window = attr_layout()

        attr_event, attr_values = attr_window.read()

        if attr_event == gui.WIN_CLOSED or attr_event == "Cancel":
            attr_window.close()
            break

        if attr_event == "Enter":
            attr_list.append(attr_values)
            print(attr_list)
            attr_window.close()

        attr_window.close()

    with open("attr_file", "w") as f:
        f.write(json.dumps(attr_list))


def sort_artist(file_name):
    try:
        file_open = js.load(open(file_name))
        artist_list= []
        for i in file_open:
            #print(i)
            dict_value = i["artist_name"]
            #print(dict_value)
            artist_list.append((dict_value))

        artist_list.sort()
        print(artist_list)

        sorted_output(artist_list)

        with open("artist_file", "a") as f:
            f.write(json.dumps(artist_list))

    except json.decoder.JSONDecodeError:
        print("Invalid values in file")
        gui.popup("Error occurred... Please enter new values before sorting")

def sort_album(file_name):
    try:
        file_open = js.load(open(file_name))
        album_list = []
        for i in file_open:
            # print(i)
            dict_value = i["alb_name"]
            # print(dict_value)
            album_list.append((dict_value))
            print(album_list)

        album_list.sort()
        print(album_list)


        sorted_output(album_list)

        with open("album_file", "a") as f:
            f.write(json.dumps(album_list))

    except json.decoder.JSONDecodeError:
        print("Invalid values in file")
        gui.popup("Error occurred... Please enter new values before sorting")

def sorted_output(sorted_list):
    layout = [[gui.Text(sorted_list)],
              [gui.Button("Close")]]

    window = gui.Window("Sorted list", layout)

    event, values = window.read()

    if event == gui.WIN_CLOSED or event == "Close":
        window.close()

def search_artist():
    layout = [[gui.Text("Enter Artist"), gui.InputText(key="artist_input")],
              [gui.Button("Enter"), gui.Button("Cancel")]
              ]

    window = gui.Window("Artist Search", layout)

    event, values = window.read()

    if event == gui.WIN_CLOSED or event == "Close":
        window.close()

    if event == "Enter":
        file_open = js.load(open("attr_file"))
        print("file opened successfully")

        artist_input = values["artist_input"]
        for i in file_open:
            dict_value = i["artist_name"]

            if values["artist_input"] == dict_value:
                print(dict_value)
                print("result matches")

            sorted_open = js.load(open("artist_file"))

            for i in range(0, len(sorted_open)):
                if i > 0:
                    before_value = sorted_open[i - 1]
                elif i == 0:
                    before_value = ""

                if i < len(sorted_open):
                    next_value = sorted_open[i + 1]
                elif i == len(sorted_open):
                    next_value = ""

                if alb_input == sorted_open[i]:
                    print(f"{alb_input} is on the right of {before_value} and on the left of {next_value}")

def search_album():
    layout = [[gui.Text("Enter Album"), gui.InputText(key="alb_input")],
              [gui.Button("Enter"), gui.Button("Cancel")]
              ]

    window = gui.Window("Album Search", layout)

    event, values = window.read()

    alb_input = values["alb_input"]

    if event == gui.WIN_CLOSED or event == "Close":
        window.close()

    if event == "Enter":
        file_open = js.load(open("attr_file"))
        window.close()

        for i in file_open:
            dict_value = i["alb_name"]

            if alb_input == dict_value:
                print(dict_value)
                print("result matches")

        sorted_open = js.load(open("album_file"))

        for i in range(0,len(sorted_open)):
            if i > 0:
                before_value = sorted_open[i - 1]
            elif i == 0:
                before_value = ""

            if i < len(sorted_open):
                next_value = sorted_open[i + 1]
            elif i == len(sorted_open):
                next_value = ""

            if alb_input == sorted_open[i]:
                print(f"{alb_input} is on the right of {before_value} and on the left of {next_value}")

def run_option():
    layout = [[gui.Text("SORT, SEARCH OR INPUT?")],
              [gui.Button("SORT"), gui.Button("SEARCH"), gui.Button("INPUT MEASUREMENTS")],
              [gui.Button("CANCEL")]]

    window = gui.Window("CD SORTER", layout)

    event, values = window.read()

    if event == gui.WIN_CLOSED or event == "CANCEL":
        window.close()

    if event == "SORT":
        sort_layout = [[gui.Text("Sort by Album or Artist")],
                  [gui.Button("Album"), gui.Button("Artist")],
                  [gui.Button("CANCEL")]]

        sort_window = gui.Window("CD SORTER", sort_layout)
        sort_event, sort_values = sort_window.read()

        if sort_event == gui.WIN_CLOSED or event == "CANCEL":
            sort_window.close()

        if sort_event == "Album":
            try:
                sort_album("attr_file")

            except json.decoder.JSONDecodeError:
                gui.popup("Error occurred... Please enter new values before sorting")

        if sort_event == "Artist":
            try:
                sort_artist("attr_file")

            except json.decoder.JSONDecodeError:
                gui.popup("Error occurred... Please enter new values before sorting")

    if event == "SEARCH":
        search_layout = [[gui.Text("Search by Album or Artist")],
                       [gui.Button("Album"), gui.Button("Artist")],
                       [gui.Button("CANCEL")]]

        search_window = gui.Window("CD SORTER", search_layout)
        search_event, search_values = search_window.read()

        if search_event == gui.WIN_CLOSED or event == "CANCEL":
            search_window.close()

        if search_event == "Album":
            try:
                search_album()

            except json.decoder.JSONDecodeError:
                print("Invalid values in file")
                gui.popup("Error occurred... Please enter new values before sorting")

        if search_event == "Artist":
            try:
                search_artist()

            except json.decoder.JSONDecodeError:
                print("Invalid values in file")
                gui.popup("Error occurred... Please enter new values before sorting")

    if event == "INPUT MEASUREMENTS":
        cd_attributes(storage_input())
#cd_attributes(storage_input())
#sort_artist(f"attr_file")
#sort_album("attr_file")
run_option()
#cd_attributes(driver_num)
'''def pop_up():
    gui.popup("hello world")

pop_up()'''
