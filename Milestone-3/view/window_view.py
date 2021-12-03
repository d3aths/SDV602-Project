import PySimpleGUI as sg


class WindowView(object):
    views = {}
    current_view = None
    def __init__(self,title,layout,controls) -> None:    
        super().__init__()

        self.layout = None
        self.window = None
        self.title = title
        self.controls = None
        self.set_layout(layout)
        self.make_window()
        self.set_controls(controls)
        self.Hide()
        self.value = None
        

    def set_layout(self, layout):
        self.layout = layout
    
    def make_window(self):
        if not self.window is None:
            self.window.Close()
            self.window = None 
        self.window = sg.Window(
            self.title,
            self.layout,
            modal=False,
            location=(0, 0),
            element_justification="center",
            finalize=True
        )
        WindowView.views[self.title] = self
        

    def set_controls(self,dictOfControls):
        self.controls = dictOfControls
    
    def Hide(self):
        if not self.window is None:
            self.window.Hide()

    def Show(self):
        if not self.window is None:
            self.window.UnHide()
    
    def Close(self):
        if not self.window is None:
            self.window.Close()
            if self.title in WindowView.views.keys():
                WindowView.views.pop(self.title)
            self.window =None

    def CatchEvents(self):
        if (not self.window is None) and (not self.controls is None) :
            print("In catch events")
            WindowView.current_view =  self
            self.Show() 
            while True :
                if not self.window is None:
                    event, self.value = self.window.read()
                else:
                    break
                if event in (sg.WIN_CLOSED, 'Close','Cancel','Exit'): # quit if close/exit/cancel button or X
                    break
                if event in self.controls.keys():
                    print( f'Recognised {event}')
                    print(self.controls[event])
                    
                    if not self.controls[event] is None: 
                        catch = self.controls[event]()
                        print(catch)
                        if not catch is None:
                             catch() # <-- runs the specified event controller
                    else:
                        print("WARNING got a None event controller")
            self.Close() 


    


    

