from setuptools import setup
import re

REQUIREMENTS = ['requests']

def readme():
    with open('README.md') as f:
        return f.read()

def find_version(filename):
    """Reads the version number from a file."""
    version = ''
    with open(filename, 'r') as f:
        regex = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in f:
            match = regex.match(line)
            if match:
                version = match.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("googlesearch/__init__.py")


setup(  name='googlesearch',
        version=__version__,
        description='Python wrapper around Google Custom Search '
                    'JSON/Atom API. Supports proxies.',
        long_description=readme(),
        license='MIT',
        author='Irmak Sirer',
        author_email='irmak.sirer@gmail.com',
        url='https://github.com/frrmack/googlesearch',
        packages=[ 'googlesearch', ],
        zip_safe=False,
        classifiers=[ 'Development Status :: 4 - Beta',
                      'Intended Audience :: Developers',
                      'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
                      'License :: OSI Approved :: MIT License',
                      'Programming Language :: Python :: 2',
                      'Programming Language :: Python :: 2.6',
                      'Programming Language :: Python :: 2.7',
                  ],
        install_requires=REQUIREMENTS,
        keywords=["googlesearch", "google", 'search', 'web search']
    )

