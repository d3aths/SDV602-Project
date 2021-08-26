from tkinter import font
from PySimpleGUI.PySimpleGUI import InputText
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot
from numpy.core.numeric import binary_repr

sg.theme('DarkGrey14')

fig = matplotlib.pyplot.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

matplotlib.use('TkAgg')
matplotlib.pyplot.ion()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# Account login or register to show up first
layoutacc = [
    [sg.Text("Please select your option", border_width=1)],
    [sg.Button("Login", size=(30,2))],
    [sg.Button("Register", size=(30,2))]
]
accwindow = sg.Window(
    "Account Login",
    layoutacc,
    modal=True
)

# Main window
layout = [
    [sg.Text("Graph 1")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Text("Summary of data", size=(40, 5))],
    [sg.Button("Prev", size=(3,1)), sg.Button("New +", button_type=2, font=('Fira 9'), size=(3,1)), sg.Button("Next", size=(3,1))],
    [sg.Output(size=(61, 10), font=('Fira 12'))],
    [sg.Multiline(size=(40, 3), enter_submits=True, key='query', do_not_clear=False),
    sg.Button('Send', bind_return_key=True)],
    [sg.Button("Close")],
]

# Create the form and show it without the plot
window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
    default_button_element_size=(8,2),
    use_default_focus=False
)
window_active=False
loginwindow_active=False
regwindow_active=False

# Add the plot to the window
draw_figure(window["-CANVAS-"].TKCanvas, fig)

#Live chat event

while True:     # The Event Loop
    event, value = accwindow.read()
    if event in (sg.WIN_CLOSED, 'Close'):            # quit if exit button or X
        break
    if event == 'Login':
        loginwindow_active=True
        layoutlogin = [
            [sg.InputText("Username")],
            [sg.InputText("Password")],
            [sg.Button("Ok")], [sg.Button("Cancel")]]
        loginwindow = sg.Window("Login", layoutlogin, modal=True)
        while True:
            ev1, vals1 = loginwindow.read()
            if ev1 == sg.WIN_CLOSED:
                break
            if ev1 == 'Ok' or ev1 == 'Cancel':      # placeholder of just closing the window, need to put login validation here
                loginwindow.close()
                accwindow.Hide()
                window_active=True
                while True:
                    ev2, vals2 = window.read()
                    if ev2 in (sg.WIN_CLOSED, 'Close'):
                        break
                    if ev2 == 'Send':
                        query = vals2['query'].rstrip()
                        print('Celeste: {}'.format(query), flush=True)
                window.close()
                accwindow.close()
        loginwindow.close()
    if event == 'Register':
        regwindow_active=True
        layoutreg = [
            [sg.InputText("Username")],
            [sg.InputText("Password")],
            [sg.Button('Ok')], [sg.Button('Cancel')]]
        regwindow = sg.Window("Register", layoutreg, modal=True)    
        while True:
            ev3, vals3 = regwindow.read()
            if ev3 == sg.WIN_CLOSED:
                break
            if ev3 == 'Ok' or ev3 == 'Cancel':      # placeholder of just closing the window, need to put register capturing here
                regwindow.close()  
        regwindow.close()

accwindow.close()