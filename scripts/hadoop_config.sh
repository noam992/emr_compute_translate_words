#!/bin/bash
echo 'Exist directory: '
pwd
python3 -m pip install requests
python3 -m pip install urllib3==1.26.6

export PATH="/usr/local/bin:$PATH"
source ~/.bash_profile
echo 'Print PATH: ' $PATH