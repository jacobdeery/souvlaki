from os import path

from setuptools import setup, find_packages

from topside import release_info

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='souvlaki',
    version='0.1.0',
    description='A simple memorable name generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jacobdeery/souvlaki',
    author='Jacob Deery',
    author_email='jacob.deery@gmail.com',
    license='MIT',
    packages=find_packages(),
)
