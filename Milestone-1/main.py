from logging import disable
from tkinter import font
from PySimpleGUI.PySimpleGUI import InputText
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from numpy.core.numeric import binary_repr
import csv

# window colour theme
sg.theme('DarkGrey14')


#switches the rows around to be able to be read properly
def transpose(table_csv, skip_if_empty = True):
    transposed_tmp = []
    transposed = []
    transposed_tmp = list(zip(*table_csv))
    
    # change each row to a list
    for row_tuple in transposed_tmp:
        transposed += [list(row_tuple)]
    
    return transposed

#reads the csv and makes the graph for the first window
def convictionsbysex():
    """
    Plot more than one on a single graph
    Args 
          **kwargs lets you pass arguments into this function
    """
    years = []
    convictions_f = []
    convictions_m = []

    with open('nz-convictions (copy).csv') as f:
        reader = csv.reader(f, delimiter=',')
        transposed = transpose(reader)

        for row in transposed:
            years.append(int(row[0])),
            convictions_f.append(int(row[3])),
            convictions_m.append(int(row[4]))


    fig, ax = plt.subplots()

    ax.set(xlabel='Year',
        ylabel='Convictions by sex',
        title='New Zealand Conviction Data')

    ax.plot(years, convictions_f)
    ax.plot(years, convictions_f, "oy")
    ax.plot(years, convictions_m)
    ax.plot(years, convictions_m, "or")

    return plt.gcf()

#reads the csv and makes the graph for the second window
def convictionsbyrace():
    """
    Plot more than one on a single graph
    Args 
          **kwargs lets you pass arguments into this function
    """
    years = []
    euro = []
    maori = []
    pacific = []
    asian = []
    other = []

    with open('nz-convictions (copy).csv') as f:
        reader = csv.reader(f, delimiter=',')
        transposed = transpose(reader)

        for row in transposed:
            years.append(int(row[0])),
            euro.append(int(row[8])),
            maori.append(int(row[9])),
            pacific.append(int(row[10])),
            asian.append(int(row[11])),
            other.append(int(row[12])),

    plt.stackplot(years, euro, maori, other, pacific, asian)
    plt.title('NZ Conviction Data')
    
    return plt.gcf()

# code for graphs
fig1 = convictionsbyrace()

fig2 = plt.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig2.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# fig2 = convictionsbyrace()

fig3 = plt.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig3.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

matplotlib.use('TkAgg')
plt.ion()

#drawing the canvas + including toolbar for interactivity
def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)

class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

# Account login or register to show up first
layoutacc = [
    [sg.Text("Please select your option", border_width=1)],
    [sg.Button("Login", size=(30,2))],
    [sg.Button("Register", size=(30,2))]
]
accwindow = sg.Window(
    "Account Login",
    layoutacc,
    modal=True,
    location=(0, 0)
)

# Main window
layout = [
    [sg.Text("Graph 1")],
    [sg.Button('Show all', font="Helvetica 8", size=(3,1))],
    [sg.Canvas(key="-CANVAS1-", size=(400 * 2, 400))],
    [sg.Canvas(key='controls_cv1')],
    [sg.Text("Summary of data", size=(40, 5))],
    [sg.Button("Prev", size=(3,1), disabled=True), sg.Button("New +", button_type=2, font=('Fira 9'), size=(3,1)), sg.Button("Next", size=(3,1))],
    [sg.Multiline(size=(61, 10), font=('Fira 12'), key='MLINE_KEY', disabled=True)],
    [sg.Multiline(size=(40, 3), enter_submits=True, key='query', do_not_clear=False),
    sg.Button('Send', bind_return_key=True)],
    [sg.Button("Close")],
]

# Create the form and show it without the plot
window = sg.Window(
    "Main Window",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
    default_button_element_size=(8,2),
    use_default_focus=False
)
# Main window 2
layout2 = [
    [sg.Text("Graph 2")],
    [sg.Canvas(key="-CANVAS2-", size=(400 * 2, 400))],
    [sg.Canvas(key='controls_cv2')],
    [sg.Text("Summary of data", size=(40, 5))],
    [sg.Button("Prev", size=(3,1)), sg.Button("New +", button_type=2, font=('Fira 9'), size=(3,1)), sg.Button("Next", size=(3,1))],
    # [sg.Multiline(size=(61, 10), font=('Fira 12'), key='MLINE_KEY', disabled=True)],
    # [sg.Multiline(size=(40, 3), enter_submits=True, key='query2', do_not_clear=False),
    # sg.Button('Send', bind_return_key=True)],
    [sg.Button("Close")],
]

# Create the form and show it without the plot
window2 = sg.Window(
    "Window 2",
    layout2,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
    default_button_element_size=(8,2),
    use_default_focus=False
)
# Main window 3
layout3 = [
    [sg.Text("Graph 3")],
    [sg.Canvas(key="-CANVAS3-", size=(400 * 2, 400))],
    [sg.Canvas(key='controls_cv3')],
    [sg.Text("Summary of data", size=(40, 5))],
    [sg.Button("Prev", size=(3,1)), sg.Button("New +", button_type=2, font=('Fira 9'), size=(3,1)), sg.Button("Next", size=(3,1), disabled=True)],
    # [sg.Multiline(size=(61, 10), font=('Fira 12'), key='MLINE_KEY', disabled=True)],
    # [sg.Multiline(size=(40, 3), enter_submits=True, key='query3', do_not_clear=False),
    # sg.Button('Send', bind_return_key=True)],
    [sg.Button("Close")],
]

# Create the form and show it without the plot
window3 = sg.Window(
    "Window 3",
    layout3,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
    default_button_element_size=(8,2),
    use_default_focus=False
)

#deactivates all the other windows at runtime
window2_active=False
window3_active=False
loginwindow_active=False
regwindow_active=False
window.Hide()
window2.Hide()
window3.Hide()

#window definitions
def window1_open():
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'Close'):
        window.Close()
        accwindow.close()
        loginwindow.close()
    if event == 'Send':       #event for live chat
        query = value['query'].rstrip()
        print('Celeste: {}'.format(query))
    if event =='Show all':          #opens all windows
        window2.UnHide()
        draw_figure_w_toolbar(window2['-CANVAS2-'].TKCanvas, fig2, window2['controls_cv2'].TKCanvas)
        window3.UnHide()
        draw_figure_w_toolbar(window3['-CANVAS3-'].TKCanvas, fig3, window3['controls_cv3'].TKCanvas)
    if event == 'Next':       #opens window 2 if next is clicked
        window2_active=True
        window2.UnHide() #for if you are navigating next again after already coming from window 2
        # window.Hide()
        # window_active=False
        draw_figure_w_toolbar(window2['-CANVAS2-'].TKCanvas, fig2, window2['controls_cv2'].TKCanvas)
        window2_open()

def window2_open():
    event, value = window2.read()
    if event in (sg.WIN_CLOSED, 'Close'):
        window2.Close()
        # accwindow.close()
        # loginwindow.close()
    if event == 'Send':
        query2 = value['query2'].rstrip()
        print('Celeste: {}'.format(query2))
    if event == 'Prev':     #opens prev window
        # window.UnHide()
        # window2.Hide()
        window_active=True
        # window2_active=False
        window.read()
        window1_open()
    if event == 'Next':       #opens window 3 if next is clicked
        window3_active=True
        # window2_active=False
        window3.UnHide()
        # window2.Hide()
        draw_figure_w_toolbar(window3['-CANVAS3-'].TKCanvas, fig3, window3['controls_cv3'].TKCanvas)
        window3_open()

def window3_open():
    event, value = window3.read()
    if event in (sg.WIN_CLOSED, 'Close'):
        window3.Close()
        accwindow.close()
        loginwindow.close()
    if event == 'Send':
        query3 = value['query3'].rstrip()
        print('Celeste: {}'.format(query3))
    if event == 'Prev':     #opens prev window
        # window2.UnHide()
        # window3.Hide()
        window2_active=True
        # window3_active=False
        window2.read()
        window2_open()

#Workaround for outputs printing wrong place
print = lambda *args, **kwargs: window['MLINE_KEY'].print(*args, **kwargs)


# # Make the Output Element "read only"
# window.Element('_OUT_')._TKOut.output.bind("<Key>", lambda e: "break")

while True:     # The Event Loop
    event, value = accwindow.read()
    if event in (sg.WIN_CLOSED, 'Close'):            # quit if exit button or X
        break
    if event == 'Login':        #opens login window if login button is pressed
        loginwindow_active=True
        layoutlogin = [
            [sg.InputText("Username")],
            [sg.InputText("Password")],
            [sg.Button("Ok")], [sg.Button("Cancel")]]
        loginwindow = sg.Window("Login", layoutlogin, modal=True)

        while True:
            event, value = loginwindow.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Ok' or event == 'Cancel':      # placeholder of just closing the window, need to put login validation here
                loginwindow.close()
                accwindow.Hide()
                window.UnHide()
                draw_figure_w_toolbar(window['-CANVAS1-'].TKCanvas, fig1, window['controls_cv1'].TKCanvas)
                #opens the main window after logging in is accepted and starts drawing on defs                           
                window1_open()    

    if event == 'Register':         #opens register window if that button is pressed
        regwindow_active=True
        layoutreg = [
            [sg.InputText("Username")],
            [sg.InputText("Password")],
            [sg.Button('Ok')], [sg.Button('Cancel')]]
        regwindow = sg.Window("Register", layoutreg, modal=True)    
        
        while True:
            event, value = regwindow.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Ok' or event == 'Cancel':      # placeholder of just closing the window, need to put register capturing here
                regwindow.close()  
        regwindow.close()
accwindow.close()