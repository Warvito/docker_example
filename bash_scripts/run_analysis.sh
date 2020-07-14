#!/bin/sh
printf '%s\n' --------------------
echo PIP
printf '%s\n' --------------------
pip install -r /project/requirements.txt --user
echo SUCCESS

printf '%s\n' --------------------
echo PYTHON
printf '%s\n' --------------------
python3 /project/my_python_script.py