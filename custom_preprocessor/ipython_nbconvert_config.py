c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['*.ipynb']
c.Exporter.preprocessors = ['cheese_preprocessor.CheesePreprocessor']