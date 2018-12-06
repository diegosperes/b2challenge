from unittest import TestCase

from challenge import Magic, is_prime


class PrimeNumberTestCase(TestCase):

    def test_validate_number_one(self):
        self.assertTrue(is_prime(1))

    def test_validate_number_two(self):
        self.assertTrue(is_prime(2))

    def test_validate_number_three(self):
        self.assertTrue(is_prime(3))

    def test_validate_prime_number(self):
        numbers = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
        for number in numbers:
            self.assertTrue(is_prime(number))

    def test_validate_not_prime_number(self):
        numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27]
        for number in numbers:
            self.assertFalse(is_prime(number))
 

class MagicTestCase(TestCase):
    def test_get_magic_numbers(self):
        magic = Magic([(0, 50)])
        self.assertEqual([1, 4, 9, 25, 49], magic.numbers)

    def test_get_magic_numbers_with_more_than_one_interval(self):
        magic = Magic([(8, 27), (49, 49)])
        self.assertEqual([9, 25, 49], magic.numbers)

    def test_get_amount_of_magic_numbers(self):
        magic = Magic([(-2300, 2300)])
        self.assertEqual(16, magic.amount)

    def test_get_amount_of_magic_numbers_with_more_than_one_interval(self):
        magic = Magic([(-2300, 0), (0, 2300)])
        self.assertEqual(16, magic.amount)
