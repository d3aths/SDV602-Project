from logging import disable
from tkinter import font
from tkinter import messagebox
from PySimpleGUI.PySimpleGUI import InputText
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from numpy.core.numeric import binary_repr
import csv
from view.CRIMFigureViewModels import convictionsbysex,convictionsbyrace
from view.window_view import WindowView

# Kept these --- 
matplotlib.use('TkAgg')
plt.ioff() # << WATCH OUT IF THIS IS pli.ion() - you are interactive mode that means you gt an plot immedaitely
# window colour theme
sg.theme('DarkGrey14')

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

# These are your Windows - each "do" creates a WindowView

# -------
def do_DES_1():
    def show_all():
        # code for graphs
        fig1 = convictionsbysex()
        window = WindowView.views['DES_1'].window
        draw_figure_w_toolbar(window['-CANVAS1-'].TKCanvas, fig1, window['controls_cv1'].TKCanvas)
    
          
    def make_des():   
        if not 'DES_1' in WindowView.views.keys():
            WindowView.views['DES_1'] = WindowView('DES_1',
            [
                [sg.Text("Graph 1")],
                [sg.Button('Display graph', font="Helvetica 8", size=(3,1))],
                [sg.Canvas(key="-CANVAS1-", size=(400 * 2, 400))],
                [sg.Canvas(key='controls_cv1')],
                [sg.Text("Summary of data", size=(40, 5))],
                [sg.Button("Prev", size=(3,1), disabled=True), sg.Button("New +", button_type=2, font=('Fira 9'), size=(3,1)), sg.Button("Next", size=(3,1))],
                [sg.Multiline(size=(61, 10), font=('Fira 12'), key='MLINE_KEY', disabled=True)],
                [sg.Multiline(size=(40, 3), enter_submits=True, key='query', do_not_clear=False),
                sg.Button('Send', bind_return_key=True)],
                [sg.Button("Close")],
            ],

            {'Prev':do_DES_2,'New':None,'Next':do_DES_2,'Send':send_chat,'Display graph':show_all}
            )
        return WindowView.views['DES_1'].CatchEvents
            
            
    return make_des() if not 'DES_1' in WindowView.views.keys() else WindowView.views['DES_1'].CatchEvents
    
# -------
def do_DES_2():
    def show_all():
         # code for graphs
        fig = convictionsbyrace()
        window = WindowView.views['DES_2'].window
        draw_figure_w_toolbar(window['-CANVAS1-'].TKCanvas, fig, window['controls_cv1'].TKCanvas)
    

    def make_des():    
        if not 'DES_2' in WindowView.views.keys():
            WindowView.views['DES_2'] = WindowView('DES_2',
            [
                [sg.Text("Graph 2")],
                [sg.Button('Display graph', font="Helvetica 8", size=(3,1))],
                [sg.Canvas(key="-CANVAS1-", size=(400 * 2, 400))],
                [sg.Canvas(key='controls_cv1')],
                [sg.Text("Summary of data", size=(40, 5))],
                [sg.Button("Prev", size=(3,1), disabled=True), sg.Button("New +", button_type=2, font=('Fira 9'), size=(3,1)), sg.Button("Next", size=(3,1))],
                [sg.Multiline(size=(61, 10), font=('Fira 12'), key='MLINE_KEY', disabled=True)],
                [sg.Multiline(size=(40, 3), enter_submits=True, key='query', do_not_clear=False),
                sg.Button('Send', bind_return_key=True)],
                [sg.Button("Close")],
            ],

            {'Prev':do_DES_1,'New':None,'Next':do_DES_1,'Send':send_chat,'Display graph':show_all}
            )
        return WindowView.views['DES_2'].CatchEvents
    
    return make_des() if not 'DES_2' in WindowView.views.keys() else WindowView.views['DES_2'].CatchEvents

def send_chat():
    query = ['query'].rstrip()
    print('Celeste: {}'.format(query))

# -------
def do_login():
    def check_login():
        if not WindowView.views['Login'].value is None:  

            # Work with a UserManager object
            from model.user_manager import UserManager
            a_user_manager = UserManager()

            user_name = ['User']
            password = ['Password']
            print(f"Got User = {user_name} , Password = {password} - just testing")

            login_result = a_user_manager.login(user_name,password)
            print(f"Got login result: {login_result}")

            print(f"Got User Name: {WindowView.views['Login'].value['Username']}")
            print(f"Got Password: {WindowView.views['Login'].value['Password']}")
            
            if login_result == 'Login Success':
             return do_DES_1()
            else:
                messagebox.showinfo("Error", "Invalid user/pass combination")
                #return None
        else:
            return None

    def make_login():
        if not 'Login' in WindowView.views.keys():
            WindowView.views['Login'] = WindowView('Login', [
                        [sg.InputText("Username", key="Username")],
                        [sg.InputText("Password", key="Password", password_char='*')],
                        [sg.Button("Ok")], [sg.Button("Cancel")]],
                        {"Ok":check_login,"Cancel":None }
                
                        )
        return WindowView.views['Login'].CatchEvents
    
    return make_login() if not 'Login' in WindowView.views.keys() else  WindowView.views['Login'].CatchEvents               

# -------
def do_register():
    def register():
        # Work with a UserManager object
        
        from model.user_manager import UserManager
        a_user_manager = UserManager()

        user_name = ['User']
        password = ['Password']
        print(f"Got User = {user_name} , Password = {password}")

        register_result = a_user_manager.register(user_name,password)
        print(f"REGISTER RESULT {register_result}")
    def make_register():
        if not 'Register' in WindowView.views.keys():
            WindowView.views['Register'] = WindowView('Register', [
                    [sg.InputText("Username")],
                    [sg.InputText("Password", password_char='*')],
                    [sg.Button("Ok")], [sg.Button("Cancel")]],
                    {"Ok": register}
                    )
        return WindowView.views['Register'].CatchEvents

    return make_register() if not 'Register' in WindowView.views.keys() else WindowView.views['Register'].CatchEvents  
# -------
# This is your start up window
def do_accWindow():
    def make_acc():
        if not 'Account Login' in WindowView.views.keys():
            WindowView.views['Account Login'] = WindowView('Account Login', 
                                [
                                    [sg.Text("Please select your option", border_width=1)],
                                    [sg.Button("Login", size=(30,2))],
                                    [sg.Button("Register", size=(30,2))]
                                ],
                                {'Login':do_login,
                                'Register':do_register}
            )
        return WindowView.views['Account Login'].CatchEvents

    return make_acc() if not 'Account Login' in WindowView.views.keys() else WindowView.views['Account Login'].CatchEvents
# -------
acc_handle_events = do_accWindow()
print("before acc_handle_events ")
acc_handle_events()
