==============================
MyMo Interview Home Assignment
==============================

The purpose of this project is to demonstrate my knowledge in Python in general and in Django specifically.

The project crawls reddit and extracts submissions from subreddits selected by users.
Users then can create search phrases to count the number of occurrences of such phrases in all or some subreddits.

-------------------------
Installation Instructions
-------------------------

This project uses pipenv_ to manage dependencies.

You can install pipenv using pip:

.. code:: bash

  $ pip install pipenv

Then the project's dependencies can be installed using:

.. code:: bash

  $ pipenv install --dev


pipenv already creates a virtual environment for you which you can use by typing:

.. code:: bash

  $ pipenv shell

For more information about pipenv refer to its documentation_.


After all the dependencies have been installed you can use invoke_ to run the project, the tests and other tasks.

To view the list of tasks type:

.. code:: bash

  $ inv --list

-------------
Configuration
-------------

According to 12factor_ `configuration should be stored in environment variables <https://12factor.net/config>`_.
The configuration is stored in .env files which have the following format:

ENV_VAR=VALUE

ENV_VAR2=ANOTHER_VALUE

There are two different .env files. One for development called .env and another one for production called .env.prod.

This repository contains an example of such .env file called .env.example with the relevant database & message broker URIs set already for production.

-----------------
Running the tests
-----------------

To run the tests you need to run postgresql first somehow and set the URI in the .env file.

Then you can run the tests by typing:

.. code:: bash

  $ inv test


.. _pipenv: https://github.com/pypa/pipenv
.. _documentation: https://docs.pipenv.org/
.. _invoke: http://www.pyinvoke.org/
.. _12factor: https://12factor.net/
