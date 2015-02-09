"""Viewing scales metrics from Pyramid"""
from setuptools import setup, find_packages
import glob
import os.path


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)


setup(
    name='pyramid_scales',
    version='1.2.dev0',

    install_requires=[
        'scales',
        'setuptools',
    ],

    extras_require={
        'test': [
            'pyramid',
            'pytest',
            'webtest',
        ],
    },

    author='Wolfgang Schnerring <wosc@wosc.de>',
    author_email='wosc@wosc.de',
    license='BSD',
    url='https://github.com/wosc/pyramid_scales',

    keywords='',
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.txt',
        'HACKING.txt',
        'CHANGES.txt',
    )),

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    data_files=[('', glob.glob(project_path('*.txt')))],
    zip_safe=False,
)
