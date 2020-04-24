# activation script for the Python virtual environment
VENV=venv/bin/activate

SCRIPT=list-hxl-datasets.py

run: $(VENV)
	. $(VENV) && python $(SCRIPT) > hxl-datasets.csv

preview: $(VENV)
	. $(VENV) && python $(SCRIPT) | head -10

build-venv: $(VENV)

$(VENV): requirements.txt
	rm -rf venv && python3 -m venv venv && . $(VENV) && pip install -r requirements.txt


