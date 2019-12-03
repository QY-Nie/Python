import os

python_files = os.popen('find . -name "*.py"')
files = python_files.readlines()

for py_file in files:
    py = py_file.strip()
    if py == './run.py':
        continue
    os.system('python '+py)
