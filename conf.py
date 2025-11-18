# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MarginX'
copyright = '2025, Sho Matsuoka'
author = 'Sho Matsuoka'
#release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# -- General configuration ---------------------------------------------------

# 拡張機能を追加します。
extensions = [
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------

# テーマを'sphinx_rtd_theme'に変更します。
html_theme = 'sphinx_rtd_theme'

# 静的ファイル（画像など）のパス
html_static_path = ['_static']

# sphinx_rtd_theme用のロゴ設定
# _staticディレクトリからの相対パスで指定します。
html_logo = '_static/image/yamanashi.png'

# (任意) sphinx_rtd_themeのオプション設定
html_theme_options = {
     'logo_only': False,
#     'display_version': True,
#     'prev_next_buttons_location': 'bottom',
#     'style_external_links': False,
#     'vcs_pageview_mode': '',
     'style_nav_header_background': '#2980B9'
#     # Toc options
#     'collapse_navigation': True,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
#     'includehidden': True,
#     'titles_only': False
 }
