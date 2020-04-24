list-hxl-datasets
=================

Generate a raw list of HXL-hashtagged datasets on HDX, disaggregated
by data provider, source, country, presence of subnational data, the
number of resource, and the start/end years.

# Prerequisites

* Python3
* Python3 venv module
* A Unix-like system

# Usage

Single command to build a virtual environment, activate it, and
generate the results in a file "hxl-datasets.csv":

  $ make run

Manual steps, in case you don't have make(1):

  $ python3 -m venv venv
  $ . venv/bin/activate
  (venv)$ pip install -r requirements.txt
  (venv)$ python3 list-hxl-datasets.py > hxl-datasets.csv
  (venv)$ deactivate

# License

This code is in the Public Domain and comes with NO WARRANTY. See UNLICENSE.md for details.

# Author

Written by David Megginson, 2020-04-24
