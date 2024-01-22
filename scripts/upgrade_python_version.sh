#!/bin/bash
sudo yum install libffi-devel -y
sudo wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz  
sudo tar -zxvf Python-3.10.4.tgz
cd Python-3.10.4
sudo ./configure --enable-optimizations
sudo make altinstall
python3.10 -m pip install --upgrade awscli --user
sudo ln -sf /usr/local/bin/python3.10 /usr/bin/python3