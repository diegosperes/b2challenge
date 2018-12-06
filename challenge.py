import math
import functools


@functools.lru_cache(maxsize=10 ** 5)
def is_prime(number):
    """
    This function take advantage of memoize concept, save 100K key value in memory RAM (~ 5.2 MB).

    A prime numbers can be generate by 6 * n - 1 or 6 * n + 1 math expression, whereas some result
    aren't a prime number and number must be bigger than 3.
    Sample:
        6 * 4 - 1 = 23 (is a prime number)
        6 * 4 + 1 = 25 (isn't a prime number)

    Also is possible to optimize the code using the concept of composite numbers and square root.
    http://mathandmultimedia.com/2012/06/02/determining-primes-through-square-root/
    """
    first = (number - 1) / 6
    second = (number + 1) / 6
    is_prime = number > 1 and (first.is_integer() or second.is_integer())
    if is_prime:
        end = int(math.sqrt(number) + 1)
        for i in range(2, end):
            if number % i == 0:
                is_prime = False
                break
    return is_prime or number in {2, 3}


class Magic:
    """
    This class will generate magic numbers respecting the initial intervals.
    Magic number is a positive number that the result of square root is a prime number.

    Magic([(-50, 50), (0, 100)])
    """
    @property
    def amount(self):
        return len(self.numbers)

    @property
    @functools.lru_cache(maxsize=1)
    def numbers(self):
        numbers = []
        for begin, end in self._intervals:
            end += 1
            begin = 0 if begin < 0 else begin
            numbers += [number for number in range(begin, end) if self._is_magic(number)]
        return numbers

    def __init__(self, intervals):
        self._intervals = intervals

    def _is_magic(self, magic):
        number = math.sqrt(magic)
        if number.is_integer():
            return is_prime(number)
        return False
