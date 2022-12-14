#!/bin/bash

if [ ! -d ~/.cheat_code_folder ];  then
  mkdir ~/.cheat_code_folder
fi

git clone https://github.com/TulipeSoyeuse/cheat_code ~/.cheat_code_folder
pip install -r ~/.cheat_code_folder/script/requirement.txt

if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
  echo 'alias cheat="python ~/.cheat_code_folder/script/cheat_script.py"' >> ~/.aliases
else
  echo 'alias cheat="python ~/.cheat_code_folder/script/cheat_script_wsl.py"' >> ~/.aliases
fi
echo "I am ready to sheat"
echo "you can now run 'cheat' command on your terminal to win this code'n'drink ! gl hf"
