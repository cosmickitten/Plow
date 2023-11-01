
from functools import wraps
import logging
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(
            f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


class Utils():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Utils, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.insert = 0
        self.select = 0
        self.records = 0

    def set_null(self):
        self.insert = 0
        self.select = 0
        self.records = 0

    def count_queries(self, insert=0, select=0, records=0):
        self.insert = self.insert + insert
        self.select = self.select + select
        self.records = self.records + records
        self.queries = {
            'insert': self.insert,
            'select': self.select,
            'records': self.records,
        }

    def count_of_queries(self):
        s= ''
        for key , value in self.queries.items():
            s = s + (f'\n{key}: {value} ')

        return s
