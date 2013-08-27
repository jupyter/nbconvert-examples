from IPython.nbconvert.preprocessors import *

class CheesePreprocessor(Preprocessor):
    """docstring for CheesePreprocessor"""

    def preprocess_cell(self, cell, resources, index):
        """
        Adds bold 'cheese' to the start of every markdown cell.
        """
        
        if 'source' in cell and cell.cell_type == "markdown":
            cell.source = '**cheese** ' + cell.source
        return cell, resources
