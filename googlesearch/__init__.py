import os

__version__ = '0.7.0'
__license__ = 'MIT'
__author__ = 'Irmak Sirer'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

from .search import GoogleSearch

__all__ = [
    'settings',
    'exceptions',
    'GoogleSearch',
]



