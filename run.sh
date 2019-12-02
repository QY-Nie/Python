#!/bin/sh

PYTHON_FILES=$(ls *.py)

echo "Nie: Run all the python files!"

for file in $PYTHON_FILES
do
    python $file
done
