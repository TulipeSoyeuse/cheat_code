#!/bin/bash

if [ ! -d ~/.cheat_code_folder ];  then
    mkdir ~/.cheat_code_folder
fi

curl -s  >
chmod u+x 
pip install -q requirement.txt

echo 'alias check="zsh ~/.cheat_code_folder/"' >> ~/.aliases
