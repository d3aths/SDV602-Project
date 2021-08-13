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

# Define the window layout
layout = [
    [sg.Text("Graph 1")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Text("Summary of data", size=(40, 5))],
    [sg.Button("Prev", size=(3,1)), sg.Button("Next", size=(3,1))],
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

# Add the plot to the window
draw_figure(window["-CANVAS-"].TKCanvas, fig)

#Live chat event

while True:     # The Event Loop
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'Close'):            # quit if exit button or X
        break
    if event == 'Send':
        query = value['query'].rstrip()
        # EXECUTE YOUR COMMAND HERE
        print('Celeste: {}'.format(query), flush=True)

window.close()