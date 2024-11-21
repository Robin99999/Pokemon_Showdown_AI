# Pokemon_Showdown_AI
Project to create an AI pokemon showdown bot

#SET-UP

git clone --recurse-submodules <repository-url>

pip install poke-env

#To run showdown locally

git clone https://github.com/smogon/pokemon-showdown.git

cd pokemon-showdown

npm install

cp config/config-example.js config/config.js

node pokemon-showdown start --no-security

Uses poke-env to simulate the pokemon showdown game environment in python

