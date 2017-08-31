from setuptools import find_packages, setup

with open('pybin/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'r') as f:
    readme = f.read()

requirements = ['click']

setup(
    name='pybin',
    version=version,
    description='',
    long_description=readme,
    author='Ofek Lev',
    author_email='ofekmeister@gmail.com',
    maintainer='Ofek Lev',
    maintainer_email='ofekmeister@gmail.com',
    url='https://github.com/ofek/pybin',
    download_url='https://github.com/ofek/pybin',
    license='MIT/Apache-2.0',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',    ],

    install_requires=requirements,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pybin = pybin.cli:pybin',
        ],
    },
)
