#!/bin/bash
cd ~
mkdir scripts

#### paste .sh file
chmod +x scripts/init_structure_folder.sh
ls -l scripts/init_structure_folder.sh

cd ~
mkdir etl

cd etl
mkdir bronze
mkdir silver
mkdir gold

#### upgrade python version scripts\upgrade_python_version.sh ####
export PYTHONPATH="/usr/local/lib/python3.10/site-packages:$PYTHONPATH"
echo $PYTHONPATH

cd ~
python3 -m venv env
source env/bin/activate

#### paste requirements.txt file
cd ~
pip install -r requirements.txt

#### paste etl/bronze/stg_appl_stock.py file

