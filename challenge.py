import math
import functools


@functools.lru_cache(maxsize=10 ** 5)
def is_prime(number):
    """
    This function take advantage of memoize concept, save 100K key value in memory RAM (~ 5.2 MB).
    Also is possible to optimize the code using the concept of composite numbers and square root.
    http://mathandmultimedia.com/2012/06/02/determining-primes-through-square-root/
    """
    is_prime = True
    if 1 >= number:
        is_prime = False
    else:
        end = int(math.sqrt(number) + 1)
        for i in range(2, end):
            if number % i == 0:
                is_prime = False
                break
    return is_prime


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
        numbers = set()
        for begin, end in self._intervals:
            end += 1
            begin = 0 if begin < 0 else begin
            for magic in self._get_next_number(begin, end):
                if end >= magic >= begin:
                    numbers.add(magic)
        return numbers

    def __init__(self, intervals):
        self._intervals = set(intervals)

    def _get_next_number(self, begin, end):
        """
        Return a magic number.

        A prime numbers can be generate by 6 * n - 1 or 6 * n + 1 math expression, whereas some result
        aren't a prime number and number must be bigger than 3.
        Sample:
            6 * 4 - 1 = 23 (is a prime number)
            6 * 4 + 1 = 25 (isn't a prime number)
        """
        step = self._get_step(begin)
        if step == 0:
            step = 1
            for integer in [2, 3]:
                if end >= integer:
                    yield integer ** 2

        number = 0
        while end > number:
            for integer in [6 * step - 1, 6 * step + 1]:
                if is_prime(integer):
                    number = integer ** 2
                    yield number
            step += 1

    def _get_step(self, begin):
        step = int(math.sqrt(begin))
        step = int((step - 1) / 6)
        return 0 if step < 0 else step
