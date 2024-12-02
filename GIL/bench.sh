#!/bin/bash

# create no-GIL Python env
conda create -n 313-noGIL \
    python=3.13 python-freethreading \
    -c conda-forge/label/python_rc \
    -c conda-forge

conda activate 313-noGIL
PYTHON_GIL=0 python bench.py
PYTHON_GIL=1 python bench.py

conda activate 313
python bench.py
