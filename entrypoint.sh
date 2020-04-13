#!/bin/bash

# remove old files
rm -f output.txt index.html output.csv

# run python script for brasilian stocks and save output in file
python3 fundamentus.py > output.txt

# run the controller
python3 controller.py