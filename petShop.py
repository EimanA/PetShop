from datetime import datetime
from time import sleep
from colorama import Fore

import homework
from main import Cat, Dog, Data


def log_stats(func):
    """
    Decorate the given function with time stamps

    :param func: a function to wrap/decorate
    :return: wrapped function
    """

    def wrap_func(*args, **kwargs):
        before = datetime.now()
        print(Fore.BLUE + "\nThe execution beginning time =", before.strftime("%m/%d/%Y, %H:%M:%S"))
        result = func(*args, **kwargs)
        after = datetime.now()
        print(Fore.BLUE + "\nThe execution ending time =", after.strftime("%m/%d/%Y, %H:%M:%S"))
        print(f"Elapsed Time in milliseconds = {(after - before).microseconds // 1000}\n")
        return result

    return wrap_func


@log_stats
def save_test():
    """
    Saves/Commits a test scenario for a single instantiation of the Cat and Dog classes in the database
    """
    try:
        data = Data("database")
        data.begin_tran()
    except Exception as e:
        print(e)

    else:
        try:
            cat = Cat("Marie")
            data.insert("Cat", cat)

            dog = Dog("Pluto")
            data.insert("Dog", dog)
        except Exception as e:
            print(e)
        else:
            data.commit()


@log_stats
def save_pet_shop():
    """
    Saves/Commits a test scenario for 5 instantiations of the Cat and Dog classes with default names in the database
    """
    try:
        data = Data("database")
        data.begin_tran()
    except Exception as e:
        print(e)

    else:
        try:
            for _ in range(3):  # inserting 3 cats with no initial names in the db
                data.insert("Cat", Cat())

            for _ in range(3):  # inserting 3 dogs with no initial names in the db
                data.insert("Dog", Dog())
        except Exception as e:
            print(e)
        else:
            data.commit()


def main():
    """
    Create an internal sqlite database from scrach and Drive the execution of the two methods above(save_test and
    save_pet_shop)
    """
    try:
        # made a new database from scratch
        homework.init_db()
    except Exception as e:
        print(e)
    else:
        sleep(3)
        save_test()
        save_pet_shop()


if __name__ == '__main__':
    main()
