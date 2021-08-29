from logging import disable
from tkinter import font
from PySimpleGUI.PySimpleGUI import InputText
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot
from numpy.core.numeric import binary_repr

# window colour theme
sg.theme('DarkGrey14')


# code for graphs
fig = matplotlib.pyplot.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

fig2 = matplotlib.pyplot.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig2.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

fig3 = matplotlib.pyplot.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig3.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

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
    modal=True,
    location=(0, 0)
)

# Main window
layout = [
    [sg.Text("Graph 1")],
    [sg.Canvas(key="-CANVAS-")],
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
    [sg.Canvas(key="-CANVAS2-")],
    [sg.Text("Summary of data", size=(40, 5))],
    [sg.Button("Prev", size=(3,1)), sg.Button("New +", button_type=2, font=('Fira 9'), size=(3,1)), sg.Button("Next", size=(3,1))],
    [sg.Multiline(size=(61, 10), font=('Fira 12'), key='MLINE_KEY', disabled=True)],
    [sg.Multiline(size=(40, 3), enter_submits=True, key='query2', do_not_clear=False),
    sg.Button('Send', bind_return_key=True)],
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
    [sg.Canvas(key="-CANVAS3-")],
    [sg.Text("Summary of data", size=(40, 5))],
    [sg.Button("Prev", size=(3,1)), sg.Button("New +", button_type=2, font=('Fira 9'), size=(3,1)), sg.Button("Next", size=(3,1), disabled=True)],
    [sg.Multiline(size=(61, 10), font=('Fira 12'), key='MLINE_KEY', disabled=True)],
    [sg.Multiline(size=(40, 3), enter_submits=True, key='query3', do_not_clear=False),
    sg.Button('Send', bind_return_key=True)],
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

#Workaround for outputs printing wrong place
print = lambda *args, **kwargs: window['MLINE_KEY'].print(*args, **kwargs)

# Add the plot to the windows
draw_figure(window["-CANVAS-"].TKCanvas, fig)

# # Make the Output Element "read only"
# window.Element('_OUT_')._TKOut.output.bind("<Key>", lambda e: "break")

while True:     # The Event Loop
    event, value = accwindow.read()
    if event in (sg.WIN_CLOSED, 'Close'):            # quit if exit button or X
        break
    if event == 'Login':        #opoens login window if login button is pressed
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
                while True:             #opens the main window after logging in is accepted
                    event, value = window.read()
                    if event in (sg.WIN_CLOSED, 'Close'):
                        break
                    if event == 'Send':       #event for live chat
                        query = value['query'].rstrip()
                        print('Celeste: {}'.format(query))
                    if event == 'Next':       #opens window 2 if next is clicked
                        window2_active=True
                        window2.UnHide() #for if you are navigating next again after already coming from window 2
                        window.Hide()
                        window_active=False
                        draw_figure(window2["-CANVAS2-"].TKCanvas, fig2)
                        print = lambda *args, **kwargs: window2['MLINE_KEY'].print(*args, **kwargs)
                        while True:
                            event, value = window2.read()
                            if event in (sg.WIN_CLOSED, 'Close'):
                                break
                            if event == 'Send':
                                query2 = value['query2'].rstrip()
                                print('Celeste: {}'.format(query2))
                            if event == 'Prev':     #opens prev window
                                window.UnHide()
                                window2.Hide()
                                window_active=True
                                window2_active=False
                                window.read()
                            if event == 'Next':       #opens window 3 if next is clicked
                                window3_active=True
                                window2_active=False
                                window3.UnHide()
                                window2.Hide()
                                draw_figure(window3["-CANVAS3-"].TKCanvas, fig3)
                                print = lambda *args, **kwargs: window3['MLINE_KEY'].print(*args, **kwargs)
                                while True:
                                    event, value = window3.read()
                                    if event in (sg.WIN_CLOSED, 'Close'):
                                        break
                                    if event == 'Send':
                                        query3 = value['query3'].rstrip()
                                        print('Celeste: {}'.format(query3))
                                    if event == 'Prev':     #opens prev window
                                        window2.UnHide()
                                        window3.Hide()
                                        window2_active=True
                                        window3_active=False
                                        window2.read()
                                window3.close()
                                accwindow.close()
                        window2.close()          
                        accwindow.close()                         
                window.close()
                accwindow.close()
        loginwindow.close()
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