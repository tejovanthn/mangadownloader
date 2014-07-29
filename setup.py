try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'mangadownloader',
    'author': 'Tejovanth N',
    'url': 'https://github.com/tejovanthn/mangadownloader',
    'download_url': 'https://github.com/tejovanthn/mangadownloader',
    'author_email': 'tejovanthn@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mangadownloader'],
    'scripts': [],
    'name': 'mangadownloader'
}

setup(**config)
