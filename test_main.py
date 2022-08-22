import io
from unittest import TestCase, mock
from colorama import Fore

from main import Cat, Dog, Data


class TestCat(TestCase):
    def test_cat_initial_age(self):
        """
        Test if in 100 instantiation of the Cats class, there exist an initial age out of the range (5 to 10) and if 5
        to 10 will be included
        """
        count_tens = 0
        count_fives = 0
        for _ in range(100):
            cat = Cat()
            age = cat.get_age()
            if age == 10:
                count_tens += 1
            elif age == 5:
                count_fives += 1
            self.assertTrue(10 >= age >= 5)
        self.assertTrue(count_tens != 0)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_cat_speak_no_value_supplied(self, mock_stdout):
        """
        Test if speak default arg("meow") value will be printed after calling speak method on the cat object
        """

        cat = Cat()
        cat.speak()
        expected_output = Fore.YELLOW + "meow\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_cat_speak_with_supplied_value(self, mock_stdout):
        """
        Test if provided speak arg will be printed after calling speak method on the cat object
        """

        cat = Cat()
        cat.speak("What?")
        expected_output = Fore.YELLOW + "What?\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_cat_speak_with_supplied_value(self):
        """
        Test if age increases from its initial value each 5 times that call method is called on the cat (or any
        animal) object
        """

        cat = Cat()
        initial_age = cat.get_age()
        for _ in range(4):
            cat.speak()
            self.assertEqual(cat.get_age(), initial_age)
        cat.speak()
        expected_age_after_5_speak = initial_age + 1
        self.assertEqual(cat.get_age(), expected_age_after_5_speak)
        for _ in range(5):
            cat.speak()
        expected_age_after_10_speak = initial_age + 2
        self.assertEqual(cat.get_age(), expected_age_after_10_speak)

    def test_dog_names(self):
        """
        Test if changing the dog name will work correctly (i.e. changed, added to the list, resulted in a right average
        length)
        """
        goofy = Dog("Ted")
        new_name = "Goofy"
        goofy.set_name(new_name)

        self.assertEqual(goofy.name, new_name)
        self.assertEqual(goofy.get_average_name_length(), 4)

    def test_dog_insertion_in_sqlite_db(self):
        """
        Test if the transaction for the Create (insert) operation into the db works correctly
        """
        new_name = "Goofy"
        goofy = Dog(new_name)
        goofy.set_age(12)
        goofy.set_favorite_food("peanut butter")

        data = Data("database")
        data.begin_tran()
        data.insert("Dog", goofy)
        data.commit()

        data2 = Data("database")
        data2.begin_tran()
        result = data2.cur.execute(f"SELECT name, age, favorite_food FROM Dog WHERE NAME = ?", (new_name, )).fetchone()
        data2.commit()
        expected = ('Goofy', 12, 'peanut butter')
        self.assertEqual(result, expected)
