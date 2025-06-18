# Cursor AI Prompts
## Here are the prompts we used in Cursor to build the project (* = comments)
## This is all achieved without writing a single line of code!!!
==========================================================================

*blank folder prepared and opened*

> Create a virtual environment for a python project

*Cursor offers these commands in turn*
python3 -m venv venv
source venv/bin/activate

*The project will use pymongo*

*Cursor offers this command*
pip3 install pymongo

> Now create a python script called ‘access-mongo.py’ to connect to a localhost installation of mongodb, using the database 'environmental' and the collection 'noise_mapping'.

*python access-mongo.py is created*

> Now adapt the code to list out all the mongo documents whose key 'Location/Agglomoration' values start with the letter 'M'

*python access-mongo.py is updated*

> Now adapt the code to add an initial function to load into the database collection 'noise_mapping' the data from the csv in the data folder called 'noise_mapping_round_3.csv'. Delete any data that already exists in the collection first. Use the csv library to load the data.

*python access-mongo.py is updated*

> Now add full comments and a descriptive header suitable for students to understand, plus a fully documented README file

*documentation is added*