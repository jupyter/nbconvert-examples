c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['*.ipynb']
c.NbConvertApp.export_format = 'latex'
c.Exporter.template_file = 'sphinx_article'
c.Exporter.preprocessors = ['sphinx_preprocessor.SphinxPreprocessor']
c.NbConvertApp.postprocessor_class = 'PDF'