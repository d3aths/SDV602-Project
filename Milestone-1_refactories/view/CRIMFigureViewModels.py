"""
Note these are not classes but figure generating functions. 
Thinking of them as FigureViewModels because they cross between view and model. A bit tenuous?
A CRIM_CSVModel is instantiated once - and its gSelections is used as a global.
In this way the CSV file is processed ONCE
"""
import matplotlib.pyplot as plt
from model.CRIMCSVModel import CRIM_CSVModel

gCSV_Model = CRIM_CSVModel('nz-convictions (copy).csv',
                           Select_Columns = {"years":0,"convictions_f":3,"convictions_m": 4,
                                             "euro": 8, "maori":9,"pacific":10,"asian": 11,"other": 12},
                           Transposed = True)
gSelections = gCSV_Model.select()


#reads the csv and makes the graph for the first window
def convictionsbysex():
    """
    
    """
    global gSelections

    years = gSelections["years"]
    convictions_f = gSelections["convictions_f"]
    convictions_m = gSelections["convictions_m"]

    plt.close('all')
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
    global gSelections

    years = gSelections["years"] 
    euro = gSelections["euro"]
    maori = gSelections["maori"]
    pacific = gSelections["pacific"]
    asian = gSelections["asian"]
    other = gSelections["other"]

    plt.close('all')
    plt.stackplot(years, euro, maori, other, pacific, asian)
    plt.title('NZ Conviction Data')
    
    return plt.gcf()

if __name__ == "__main__" :
    """
    Mainly testing
    """
    convictions_by_sex_figure = convictionsbysex()
    convictions_by_race_figure = convictionsbyrace()



