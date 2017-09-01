pybin
=====

.. image:: https://img.shields.io/pypi/v/pybin.svg?style=flat-square
    :target: https://pypi.org/project/pybin
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pybin.svg?style=flat-square
    :target: https://pypi.org/project/pybin
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/l/pybin.svg?style=flat-square
    :target: https://choosealicense.com/licenses
    :alt: License

-----

When you install a package via ``pip install --user ...``, any executables get
placed in special directory specifically for the intended user. Unfortunately,
this location is most likely not included in your user's PATH variable. So for
example if you did ``pip3 install --user hatch`` and then tried to learn more
about your new tool by doing ``hatch --help``, it would fail to be located.

pybin solves this problem by providing a small CLI, and corresponding API, to
locate your Python's user bin and optionally update the user PATH. It supports
all major operating systems and does not require elevated privileges!

    **Fear not, this only modifies the user PATH; the system PATH is never
    touched nor even looked at!**

.. contents:: ``Table of Contents``
    :backlinks: none

Installation
------------

pybin is distributed on `PyPI <https://pypi.org>`_ as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 2.6-2.7/3.3+ and PyPy.

.. code-block:: bash

    $ pip install pybin

License
-------

pybin is distributed under the terms of both

- `MIT License <https://choosealicense.com/licenses/mit>`_
- `Apache License, Version 2.0 <https://choosealicense.com/licenses/apache-2.0>`_

at your option.
