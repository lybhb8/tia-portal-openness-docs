# Configuration file for the Sphinx documentation builder.
#
# For the full list of built configurations, see the docs:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information ------------------------------------------------

project = 'TIA Portal Openness Documentation'
copyright = '2024, TIA Portal Openness Community'
author = 'TIA Portal Openness Community'

# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
    'myst_parser',
]

# Myst parser configuration
myst_enable_extensions = [
    'amsmath',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'linkify',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
]

# -- Options for HTML output -------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vocabulary_mode': 'first',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# -- Options for PDF output --------------------------------------------

latex_engine = 'xelatex'
latex_elements = {
    'preamble': r'''
\usepackage{ctex}
\setCJKmainfont{SimSun}
\setCJKsansfont{SimSun}
''',
}

# -- Options for intersphinx extension ---------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for localisation ------------------------------------------

language = 'zh_CN'
locale_dirs = ['locale/']
