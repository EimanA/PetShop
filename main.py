"""
Developer: Eiman Ardakanian
Date: 2022-08-21
"""

from random import randint
import sqlite3
from colorama import Fore, Style
from abc import ABC


class Animal(ABC):
    """
    A parent (abstract) class to represent different animals in a pet store including cats and dogs

    Attributes
    ----------
    name : str
        name of the Animal
    name_list : list
        a List of all this animal's names including the current and past names
    age : int
        age of the Animal
    favorite_food : str
        favorite food of the Animal
    speak_counter : int
        the number of times this animal has spoken

    Methods
    -------
    getters and setters for most of the attributes:
        Gets or Sets the attribute.
        Note: Set name also appends this current name to the previously added list of names
    get_average_name_length()
        Gets average name length of all names that this animal ever have had
    speak(words)
        Prints the provided words and increases the speak_counter. Each 5 times that the animal speaks (each 5 call on
        a specific object of this class) will also increase the age of the object by 1
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes of the animal object

        :param name: a str representing the name of the animal
        """
        self.name = name
        self.name_list = [name]
        self.age = randint(5, 10)
        self.favorite_food = None
        self.speak_counter = 0

    def get_name(self):
        return self.name

    def get_names(self):
        return self.name_list

    def get_age(self):
        return self.age

    def get_favorite_food(self):
        return self.favorite_food

    def get_speak_count(self):
        return self.speak_counter

    def set_name(self, name):
        """
        Set the name of the animal and add this name to the list of all names that this animal has ever had
        :param name: a str representing the name of the animal
        """
        self.name = name
        self.name_list.append(name)

    def set_age(self, age):
        self.age = age

    def set_favorite_food(self, favorite_food):
        self.favorite_food = favorite_food

    def get_average_name_length(self):
        """
        Get the average length of the names that this animal has ever had
        """
        num_of_names = len(self.name_list)
        total_length = 0
        for name in self.name_list:
            total_length += len(name)
        return total_length / num_of_names

    def speak(self, words):
        """
        Speak(Print) the provided words.

        This method/function also increments the speak_counter attribute of the animal by one, and for each 5 speaks, it
        increases the age of the animal by one.

        :param words: a str representing the words that animal should say(the words that should be printed)
        """
        print(Fore.YELLOW + words)
        self.speak_counter += 1
        if self.speak_counter % 5 == 0:
            self.age += 1


class Cat(Animal):
    """
    A subclass of the Animal class

    Attributes
    ----------
    All animal attributes

    Methods
    -------
    speak :
        sends (calls/invokes) the same method of the parent class with the received argument/words or with the default
        value ("meow")
    """
    def __init__(self, name=""):
        super().__init__(name=name)

    def speak(self, words="meow"):
        super().speak(words)


class Dog(Animal):
    """
    A subclass of the Animal class

    Attributes
    ----------
    All animal attributes

    Methods
    -------
    speak :
        sends (calls/invokes) the same method of the parent class with the received argument/words or with the default
        value ("bark")
    """
    def __init__(self, name=""):
        super().__init__(name=name)

    def speak(self, words="bark"):
        super().speak(words)


class Data:
    """
    A class to represent a connection to the internal database

    Attributes
    ----------
    conn : object
        a connect object of the internal sqlite3 db
    cur : object
        a cursor object for the connection to the internal sqlite3 db

    Methods
    -------
    begin_tran():
        Creates a cursor object for the connection of the object of this class
    commit():
        Commits and closes the connection to the db
    rollback():
        Rollbacks the transaction to the db
    insert(table, obj):
        Inserts the object attributes into the specified table of our db by executing the required query on the cursor
        object

    """
    def __init__(self, database):
        """
        Constructs the connection to the internal sqlite db

        :param database: a str representing the database name
        """
        try:
            print(Fore.GREEN + f"\nConnecting to {database}")
            file_name = database + ".db"
            self.conn = sqlite3.connect(file_name)
        except sqlite3.Error as e:
            print(Fore.RED + f"Error happened during db connection: {e}")
            raise Exception("No db connection created due to an sqlite error")
        else:
            self.cur = None

    def begin_tran(self):
        """
        Creates a cursor and assigns it to the cur attribute of this object for the connection to the internal db
        """
        print("Beginning a transaction")
        try:
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error happened during commit: {e}")
            raise Exception("No cursor object created due to an sqlite error")

    def commit(self):
        """
        Commits the changes to the internal db and closes the connection
        """
        print(Fore.GREEN + "Committing transaction")
        try:
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error happened during commit: {e}")
            self.rollback()

    def rollback(self):
        """
        Rollbacks the last transaction made for the internal db
        """
        try:
            print("Rolling back transaction")
            self.conn.rollback()  # rollback code
        except Exception as e:
            print(f"Error happened during rollback: {e}")

    def insert(self, table, obj):
        """
        Inserts name, age, favorite_food, speak_counter attributes of the object into the provided table name
        :param table: a str representing the table name of the database
        :param obj: an object of the animal class
        """
        try:
            print(Style.RESET_ALL + f"Inserting {obj.get_name()} into table {table}")

            name = obj.get_name()
            age = obj.get_age()
            favorite_food = obj.get_favorite_food()
            speak_counter = obj.get_speak_count()

            self.cur.execute(f"INSERT INTO {table} (name, age, favorite_food, speak_counter) VALUES (?, ?, ?, ?)",
                             (name, age, favorite_food, speak_counter))

        except Exception as e:
            print(f"Error happened during insertion in db: {e}")
            raise Exception("No row created due to an sqlite error")

        else:
            inserted_row = self.cur.execute(f"SELECT * FROM {table} WHERE id = last_insert_rowid()").fetchone()
            print(inserted_row)


# This main function is not going to be called since the main method implementation for the next parts is written in
# the other file
def main():
    """
    Implement part 1 of the assignment

    Create a Cat class with a number of methods. Change the default name, and insert it into the database
    """

    cat = Cat()
    print(f"Name is currently {cat.get_name()}")

    cat.set_name("Garfield")
    print(f"Name has been changed to {cat.get_name()}")

    try:
        data = Data("database")
        data.begin_tran()
    except Exception as e:
        print(e)

    else:
        try:
            cat = Cat("Marie")
            data.insert("Cat", cat)

        except Exception as e:
            print(e)
        else:
            data.commit()


# main()
