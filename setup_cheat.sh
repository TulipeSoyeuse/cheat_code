#!/bin/bash

if [ ! -d ~/.cheat_code_folder ];  then
  mkdir ~/.cheat_code_folder
fi

if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then

  git clone https://github.com/TulipeSoyeuse/cheat_code ~/.cheat_code_folder
  pip install -r ~/.cheat_code_folder/script/requirement.txt
  echo "I am ready to sheat"
  echo 'alias cheat="python ~/.cheat_code_folder/script/cheat_script.py"' >> ~/.aliases
  echo "you can now run 'cheat' command on your terminal to win this code'n'drink ! gl hf"

else
echo "work in progress"
fi
