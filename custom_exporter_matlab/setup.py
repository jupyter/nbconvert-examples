from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='matlab_nbconvert',
    version='0.2',
    description='An exporter for matlab-based jupyter notebooks',
    long_description=readme,
    url='https://github.com/janfreyberg/matlab_nbconvert',
    download_url='https://github.com/janfreyberg/matlab_nbconvert/tarball/0.2',
    # Author details
    author='Jan Freyberg',
    author_email='jan.freyberg@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Code Generators',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Only the following because these work w/ matlab kernel
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=['matlab', 'jupyter', 'notebook', 'nbconvert'],
    packages=['matlab_nbconvert'],
    install_requires=['nbconvert'],
    # Include the template file
    package_data={
        '': ['templates/*.tpl']
    },
    # Specify entry point to let nbconvert use this
    entry_points={
        'nbconvert.exporters': [
            'matlab = matlab_nbconvert:MatlabExporter'
        ],
    },
)
