import csv


class CRIM_CSVModel(object):
    """
    A CSV Model for CRIM files - Selects columns
    """
    def transpose(self,table_csv):
        transposed_tmp = []
        transposed = []

        # transpose
        transposed_tmp = list(zip(*table_csv))
        
        # change each row to a list
        for row_tuple in transposed_tmp:
            transposed += [list(row_tuple)]
        
        return transposed

    def __init__(self,Source_File = None, Select_Columns = None, Transposed = False) -> None:
        """
        Constructor
        ===========
        Source_File is a csv file
        Filter_Columns is a Dictionary of Names with column locations
        Transposed is true when headings are in Column 0 , and Values are listed by Row
        """
        self.source_file = Source_File
        self.select_columns = Select_Columns
        self.transposed = Transposed
        self.rows = None

        # Load data
        if not (self.source_file is None):
            with open(self.source_file) as f:
                the_list = []
                reader = csv.reader(f, delimiter=',')
                if self.transposed :
                    the_list = self.transpose(reader)
                else: 
                    the_list = [item for item in reader]
                self.rows = the_list
        
    def setFilename(self, Source_File):
        """
        Set the CSV file name
        """
        self.source_file = Source_File 

    def setSelectColumns(self, select_columns):
        """
        Set the columns to select as a dictionary of Name:Row_Columns pairs
        """
        self.select_columns = select_columns

    def select(self):
        result = {}
        if not(self.source_file is None) and not(self.select_columns is None) and not(self.rows is None):
            for row in self.rows:
                for key,value in self.select_columns.items() :
                    if not (key in result) :
                        result[key] = []
                    result[key].append(int(row[value]))
            return result
        else:
            print("model_csv: needs a csv file before it can select ")
            return None




if __name__ == "__main__":
    """
    Mainly tests

    """
    a_model = CRIM_CSVModel('nz-convictions (copy).csv',
                        Select_Columns = {"years":0,"convictions_f":3,"convictions_m": 4,
                                        "euro": 8, "maori":9,"pacific":10,"asian": 11,"other": 12},
                        Transposed = True)
    selections = a_model.select()
    print(selections)