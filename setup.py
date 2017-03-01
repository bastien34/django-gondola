import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-gondola',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPL3',
    description='A simple Django app to present categories of things.',
    long_description=README,
    url='https://www.example.com/',
    author='Bastien Roques',
    author_email='bastien@palaceweb.fr',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='tool to build nice grid layout',
    install_requires=['Django>=1.10',
                      'Pillow>=4.0',
                      'django-tables2>=1.4'],
)
