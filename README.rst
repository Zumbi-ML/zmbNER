========
Overview
========

A Named Entity Recognition project, used by the Zumbii Engine

* Free software: BSD 2-Clause License

Installation
============

::

    pip install zmbner

You can also install the in-development version with::

    pip install git+ssh://git@https://github.com/Zumbi-ML/zmbNER/j3ffsilva/zmbNER.git@main

Documentation
=============


https://zmbNER.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
