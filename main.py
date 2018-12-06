import timeit

from challenge import Magic


if __name__ == '__main__':
    code = """amount = Magic([(0, 10 ** 10)]).amount"""
    times = timeit.repeat(stmt=code, number=10, globals=globals())
    print(sum(times) / len(times))
