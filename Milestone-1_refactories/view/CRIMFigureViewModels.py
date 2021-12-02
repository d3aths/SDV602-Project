'''''''''
Note these are not classes but figure generating functions. 
Thinking of them as FigureViewModels because they cross between view and model. A bit tenuous?
A CRIM_CSVModel is instantiated once - and its gSelections is used as a global.
In this way the CSV file is processed ONCE
'''
from threading import ThreadError
import matplotlib.pyplot as plt
from model.CRIMCSVModel import CRIM_CSVModel

class DataSource():
    ds = None

def getdata():
    global gSelections
    gCSV_Model = CRIM_CSVModel(DataSource.ds,
                            Select_Columns = {'years':0,'convictions_f':3,'convictions_m':4,
                                                'euro':8, 'maori':9,'pacific':10,'asian':11,'other':12,
                                                'under19':15, '20-24':16, '25-29':17, '30-34':18, '35-39':19, '40-44':20, '45-49':21, '50-54':22, '55-59':23, '60-64':24, '65+':25},
                            Transposed = True)
    gSelections = gCSV_Model.select()


#reads the csv and makes the graph for the first window
def convictionsbysex():
    '''''''''
    
    '''
    global gSelections

    years = gSelections['years']
    convictions_f = gSelections['convictions_f']
    convictions_m = gSelections['convictions_m']

    plt.close('all')
    fig, ax = plt.subplots()

    ax.set(xlabel='Year',
        ylabel='Convictions by sex',
        title='New Zealand Conviction Data')

    ax.plot(years, convictions_f)
    ax.plot(years, convictions_f, 'oy', label="Women")
    ax.plot(years, convictions_m)
    ax.plot(years, convictions_m, 'or', label="Men")
    ax.legend()

    return plt.gcf()

#reads the csv and makes the graph for the second window
def convictionsbyrace():
    '''''''''
    Plot more than one on a single graph
    Args 
          **kwargs lets you pass arguments into this function
    '''
    global gSelections

    years = gSelections['years'] 
    euro = gSelections['euro']
    maori = gSelections['maori']
    pacific = gSelections['pacific']
    asian = gSelections['asian']
    other = gSelections['other']

    plt.close('all')
    plt.stackplot(years, euro, maori, other, pacific, asian)
    plt.title('NZ convictions by race')
    plt.legend()
    
    return plt.gcf()

def convictionsbyage():
    '''''''''
    had originally tried to do a pie chart here until troubles made me realize it cannot condense the data from all years into some total value
    so i was trying to ask it to show all years data in one single pie chart = impossible
    going with bar chart instead
    '''

    # ages = [gSelections['under19'], gSelections['20-24'], gSelections['25-29'], gSelections['30-34'], gSelections['35-39'], gSelections['40-44'], gSelections['45-49'], gSelections['50-54'], gSelections['55-59'], gSelections['60-64'], gSelections['65+']]

    years = gSelections['years']
    one = gSelections['under19']
    two = gSelections['20-24']
    three = gSelections['25-29']
    four = gSelections['30-34']
    five = gSelections['35-39']
    six = gSelections['40-44']
    seven = gSelections['45-49']
    eight = gSelections['50-54']
    nine = gSelections['55-59']
    ten = gSelections['60-64']
    eleven = gSelections['65+']
    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()
    ax.bar(years, one, width, bottom=two, label='Under 19')
    ax.bar(years, two, width, bottom=three, label='20-24')
    ax.bar(years, three, width, bottom=four, label='25-29')
    ax.bar(years, four, width, bottom=five, label='30-34')
    ax.bar(years, five, width, bottom=six, label='35-39')
    ax.bar(years, six, width, bottom=seven, label='40-44')
    ax.bar(years, seven, width, bottom=eight, label='45-49')
    ax.bar(years, eight, width, bottom=nine, label='50-54')
    ax.bar(years, nine, width, bottom=ten, label='55-59')
    ax.bar(years, ten, width, bottom=eleven, label='60-64')
    ax.bar(years, eleven, width, label='65 +')

    ax.set_ylabel('Ages')
    ax.set_title('NZ Convictions by Age')
    ax.legend()
     
    return plt.gcf()

if __name__ == '__main__' :
    '''''''''
    Mainly testing
    '''
    convictions_by_sex_figure = convictionsbysex()
    convictions_by_race_figure = convictionsbyrace()
    convictions_by_age_figure = convictionsbyage()



