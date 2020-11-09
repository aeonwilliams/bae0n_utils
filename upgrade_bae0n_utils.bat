@echo off
call python setup.py sdist bdist_wheel
call python -m twine upload dist/*