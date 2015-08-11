Open Data Services Dashboard
==============

Introduction
------------

The Open Data Services dashboard is a displays information about issues and milestones in our GitHub repository.

It is built off the codebase that runs the IATI Dashboard: http://dashboard.iatistandard.org

Technology Overview
^^^^^^^^^^^^^^^^^^^

The dashboard mostly in Python, with some helper Bash scripts.

Python scripts:

* ``make_html.py`` contains is a Flask application that makes use of Frozen Flask to generate some static HTML.

Bash helper scripts:

* The dashboard uses data from GitHub, which needs to be fetched using ``fetch_data.sh``.
* ``git.sh`` runs all the above commands, see Usage below.

Installation
^^^^^^^^^^^^

Requirements:

* Unix based setup (e.g. Linux, Mac OS X) with bash etc.
* wget and curl installed
* Python 3
* python-virtualenv (optional)
* Development files for libfreetype, libpng, libxml and libxslt e.g. ``libfreetype6-dev libpng-dev libxml2-dev libxslt-dev``.

  (alternatively, you may be able to install some of the python dependencies in 
  requirements.txt using your package manager)


To install:

.. code-block:: bash

    ## Get the code
    git clone 'repo here'
    cd 'directory'

    ## Set up a virtual environment (recommended)
    # Create a virtual environment
     virtualenv .ve --python=/usr/bin/python3
    # Activate the virtual environment
    # (you need to this every time you open a new terminal session)
    source .ve/bin/activate

    ## Install python dependencies
    ## Use pip as described below, or your distro's package manager to install
    ## the dependcies in requirements.txt
    # If you are running a less recent linux distro, you will need to install distribute
    easy_install -U distribute
    pip install -r requirements.txt

    # Create a configuration file which is used for GitHub credentials to make requests to the GitHub api
    cp config.py.example config.py # And provide the necessary values

Usage
^^^^^

.. code-block:: bash
    
    # Fetch data from github
    ./fetch_data.sh

    mkdir out
    python make_html.py

make_html.py will output a MissingURLGeneratorWarning. This is expected, as some of the URLs defined are for the live development server only (see below).

The full list of steps for our deployment can be found in ``git.sh``. (The name of this is now a misnomer as the output is no longer a git repository - previously a commit was pushed to GitHub pages.)

Development
^^^^^^^^^^^

For development, you can use the live Flask development server, instead of Frozen Flask.

.. code-block:: bash

    python make_html.py --live

Using the live development server is highly recommended, because it displays full bracktraces for 500 errors, whereas frozen flask does not.


License
^^^^^^^

::

    Copyright (C) 2013-2015 Ben Webb <bjwebb67@googlemail.com>
    Copyright (C) 2013-2014 David Carpenter <caprenter@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
