from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version = '0.1',
    package = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'EDSA python package example',
    long_description=open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/Gav54/mypackage',
    author = 'Gavin Ogira',
    author_email = 'gavogira@gmail.com'
)