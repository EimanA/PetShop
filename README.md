# Granify Assignment - Pet Shop app

Pet Shop is an OO design and implementation of a pet shop by EIMAN ARDAKANIAN with different kinds of animals (e.g. Cats, Dogs) who have name, age, and a favorite food, as well as a number of methods to get and set their attributes, store their probable previous names, or train them to speak a set of words.
This Pet Shop app also has an internal database connected to it in order to interact with it for different CRUD operations.

## Setting up the Environment and Instruction to run the app

For the ease of the reviewer, except for some core libraries and a sqlite3 db, there is no other packages or environment import/installation necessary for running this application.

To view the result of the application in a neat format, it would be better to run the main() function of this app from an IDE like Pycharm.
Otherwise, the main() function of the petShop.py file will also run the program, but it may not generate the colorful texts correctly in some environments.

## Tech Stack

Python, and SQLite

## Project Structure

All the files listed below were left in the root directory of the project to follow the instruction.

### database.db
The sqlite3 internal db

### homework.py
The first part of the instruction for homework.sql. This python file, which will be executed after running the main() function from the petShop.py, is responsible for creating the internal database and creation of its 2 tables (cats and dogs).

### main.py
The model design and implementation of the Animal class and its 2 children classes Cats and Dogs, as well as the Data class representing the interactions with the internal database.

### petShop.py
The main function/driver of the project responsible for running 2 demo methods (save_test and save_pet_shop), as well as a wrapper function to print colorful timestamps while running the project.

### schema.sql
The second part of the instruction for homework.sql which contains the sql commands to create 2 tables for cats and dogs.

### test_main.py
Unit tests. This file contains a number of unit tests including the ones that were asked for in the instruction as well as some other ones like checking the CRUD interactions with the database.


## Considerations

1. I assumed the Cat and Dog class need a parent/abstract class due to their similarities. An animal class were used for this purpose, which contains almost all the attributes and methods except for speak() method implementation due to the difference in the default value.
2. A real but lightweight sqlite db was used for a fuller implementation of this assignment. However, from CRUD operations, only the Create and Read were implemented as the other 2 were not related to the tasks that were asked for in the instruction.
3. This database will be made from scratch each time we run the program. However, by commenting out this line of the code in the main() function of the petShop.py file -> homework.init_db(), the previous executions of the app will remain in the db.
