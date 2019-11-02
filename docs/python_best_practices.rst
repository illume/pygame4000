python best practices
=====================

Every project is somewhat different. Every reason to code is different.

Therefore best practices should be different. You won't do things the same way hacking up a weekend game for fun as you would grinding away in a cubicle implementing an aircraft safety system.


There's a lot of information out there about python.
Lots of tools to choose between.

This guide aims to point you in the right direction on a few topics.


Testing
-------

Use pytest because

- No boilerplate
- Failure reports
- Scalability
- Fixtures
- Mocking/Monkeypatching
- Mature with great plugins


Integration tests
~~~~~~~~~~~~~~~~~

Separate integration (functional) tests from unit tests.

Unit tests should be quick to run, and integration tests should
test the integration with external APIs or systems.


Code coverage
~~~~~~~~~~~~~

Use code coverage reporting to make sure code is at least tested.
Track and enforce a minimum standard in CI.


Documentation
-------------

It's fine, and good to write just a README.md file.

It's more important that you have:

- what it is, what it does, who you are, and why?
- examples of how to use it
- how to learn it, and how to use it to do certain tasks
- detailed reference


Write documentation with
`Sphinx
<http://www.sphinx-doc.org/en/stable/index.html>`_ and RestructuredText.

You can write narative style documentation, and also generate API documentation.
If you want to do something more than a basic README.md in your repo, then this is the way to go.

Type documentation
~~~~~~~~~~~~~~~~~~

First, remember that type hints are not needed for python and for all types of projects.
But they can be useful.


Document types with the typing module, rather than specify them in docstrings.
Because then the types can be checked with a tool called mypy in CI and in some code editors.

From sphinx-autodoc-typehints `sphinx-autodoc-typehints
<https://github.com/agronholm/sphinx-autodoc-typehints>`_ ...

.. code-block:: python

	from typing import Union

	def format_unit(value: Union[float, int], unit: str) -> str:
	    """ Formats the given value as a human readable string
	        using the given units.

	    :param value: a numeric value
	    :param unit: the unit for the value (kg, m, etc.)
	    """
	    return '{} {}'.format(value, unit)


There is an `example of how to document your python functions
<https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html>`_



Literate programming
--------------------

Experiments and live documentation can be done with
`jupyter notebooks
<http://jupyter.org/>`_

This is a great tool for experiments, notebooks, and live documentation, and visualizations.


Code quality and formatting
---------------------------

Use `pylint
<https://www.pylint.org/>`_
for linting, and `black
<https://github.com/ambv/black>`_
for code formatting.

Especially for developers new to python, pylint gives a lot of
good advice on how to improve your code.

It can catch many simple errors before they get checked into
source control or go into production.

A code formatter like `black
<https://github.com/ambv/black>`_
is useful in large teams so as to avoid having to talk about code formatting.


Package your code
-----------------

The `python packaging guide
<https://packaging.python.org/tutorials/packaging-projects/>`_
explains how to package python code.

- share your code with others
- a file structure all tools expect


Manage dependencies
-------------------

with `poetry
<https://poetry.eustace.io/>`_.
Because poetry is safe, easy, and addresses the whole workflow.


The `pip
<https://pip.pypa.io/en/stable/>`_ tool is still good to learn. However it has a few dangerous edges if you are a newbie. It also does not address the whole workflow of using and publishing packages.

Work inside a virtual environment to keep projects separated.
Because each project may require different dependencies installing them system wide will not work.



A private python index
----------------------

This is only needed if you want to keep some of your code private.

Private Python packages can be stored in a private python index.
`devpi
<https://devpi.net/docs/devpi/devpi/stable/%2Bd/index.html>`_

Devipi is also useful because it can act as a local mirror and cache.
This can make deploys quicker and more reliable.

You can also use github, or another private git code repository and use these for packages.
