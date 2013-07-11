c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['*.ipynb']
c.NbConvertApp.export_format = 'sphinx_howto'

#Include dependency files
c.WriterBase.files = ['cats/mycat.jpg', 
                      'cats/yourcat.jpg']