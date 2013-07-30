from IPython.nbconvert.transformers import *

class CheeseTransformer(Transformer):
    """docstring for CheeseTransformer"""

    def transform_cell(self, cell, resources, index):
        """
        Adds bold 'cheese' to the start of every markdown cell.
        """
        
        if 'source' in cell and cell.cell_type == "markdown":
            cell.source = '**cheese** ' + cell.source
        return cell, resources
