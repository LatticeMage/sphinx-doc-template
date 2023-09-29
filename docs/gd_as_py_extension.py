
def setup(app):
    app.connect('source-read', treat_gd_as_py)

def treat_gd_as_py(app, docname, source):
    # If the document name ends with .gd, Sphinx will treat it as a .py file
    if docname.endswith('.gd'):
        return [''.join(source)]
    return None
