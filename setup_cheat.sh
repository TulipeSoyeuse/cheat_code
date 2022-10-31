#!/bin/bash

if [ ! -d ~/.cheat_code_folder ];  then
    mkdir ~/.cheat_code_folder
fi

curl -s https://github.com/TulipeSoyeuse/cheat_code/blob/main/setup_cheat.sh
chmod u+x cheat_CLI.sh
pip install -q ~/.cheat_code_folder/script/requirement.txt
echo "I am ready to sheat"
echo 'alias cheat="python ~/.cheat_code_folder/script/cheat_script"' >> ~/.aliases
echo "you can now runn 'cheat' command on your terminal to win this code'n'drink ! gl hf"
