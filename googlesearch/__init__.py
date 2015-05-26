import os

__version__ = '0.7.0'
__license__ = 'MIT'
__author__ = 'Irmak Sirer'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

from .googlesearch import GoogleSearch

__all__ = [
        'GoogleSearch',
    ]

