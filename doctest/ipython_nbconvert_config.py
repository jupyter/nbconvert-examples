"""
DocTest format is the best plaintext format for IPython output in emails etc'.
"""

c = get_config()

#Export all the notebooks in the current directory to the doctest format.
c.NbConvertApp.notebooks = ['*.ipynb']
c.NbConvertApp.export_format = 'python'
c.Exporter.filters = {'prepend_prompt': 'prepend_prompt.prepend_prompt'}
c.Exporter.template_file = 'doctest'
