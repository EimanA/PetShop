import sqlite3
from os import path


def db_path_finder():
    """

    :return: two strings representing the database and schema full paths
    """
    directory = path.dirname(path.abspath(__file__))
    schema_path = path.join(directory, 'schema.sql')
    db_path = path.join(directory, 'database.db')
    return db_path, schema_path


def init_db():
    """
    Create the database and its tables from the schema
    """
    sql_db_path, sql_schema_path = db_path_finder()
    if sql_db_path and sql_schema_path:
        try:
            connection = sqlite3.connect(sql_db_path)
        except sqlite3.Error as e:
            raise Exception("No db connection created due to an sqlite error")
        else:
            try:
                with open(sql_schema_path) as f:
                    connection.executescript(f.read())
            except (Exception, sqlite3.Error) as e:
                print(e)
            else:
                connection.commit()
                connection.close()
