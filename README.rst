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
placed in a special directory specifically for the intended user. Unfortunately,
this location is most likely not included in your user's PATH variable. So for
example if you did ``pip3 install --user hatch`` and then tried to learn more
about your new tool by doing ``hatch --help``, it would fail to be located.
See: `<https://github.com/pypa/pip/issues/3813>`_

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

You may need ``sudo``. **Do not use ``--user``!**

Commands
--------

Only 2!

pybin
^^^^^

.. code-block:: bash

    $ pybin -h
    Usage: pybin [OPTIONS] COMMAND [ARGS]...

      Shows the location of the bin directory and whether or not it is in the
      user PATH.

    Options:
      -p, --pypath TEXT  An absolute path to a Python executable.
      --version          Show the version and exit.
      -h, --help         Show this message and exit.

    Commands:
      put  Updates the user PATH

pybin put
^^^^^^^^^

.. code-block:: bash

    $ pybin put -h
    Usage: pybin put [OPTIONS]

      Updates the user PATH. The shell must be restarted for the update to take
      effect.

    Options:
      -p, --pypath TEXT  An absolute path to a Python executable.
      -f, --force        Update PATH even if it appears to be correct.
      -h, --help         Show this message and exit.

API
---

.. code-block:: python

    >>> from pybin import in_path, locate, put_in_path
    >>> in_path()
    False
    >>> locate()
    'C:\\Users\\Ofek\\AppData\\Roaming\\Python\\Python36\\Scripts'
    >>> success = put_in_path()

Manual modification
-------------------

Use the location pybin shows in concert with this very comprehensive document
Java provides: `<https://www.java.com/en/download/help/path.xml>`_

License
-------

pybin is distributed under the terms of both

- `MIT License <https://choosealicense.com/licenses/mit>`_
- `Apache License, Version 2.0 <https://choosealicense.com/licenses/apache-2.0>`_

at your option.
