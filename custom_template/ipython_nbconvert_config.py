c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['*.ipynb']
c.NbConvertApp.export_format = 'html'
c.Exporter.template_file = 'md_cell_list'