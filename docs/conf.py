
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'MY_ALGO'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.viewcode']
source_suffix = '.rst'
master_doc = 'index'
html_theme = 'alabaster'
# html_static_path = ['_static']
