
from os import environ
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='testhelper',
    packages=['testhelper'],
    version='0.4.0',
    description='A testing helper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Peter White',
    author_email='pwhite@delpwhite.org',
    url='https://github.com/erikdeirdre/test_helper',
    python_requires = '>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)