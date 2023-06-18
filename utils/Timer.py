'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-18 16:32:19
 # @ license: Mozilla Public License 2.0
 # @ description: the file contains functions for timer used in the program
 '''

import time

def timer(func)-> None:
    def func_wrapper(*args, **kwargs):
        start_time: float = time.time()
        result = func(*args, **kwargs)
        end_time: float = time.time()
        time_pass: float = end_time - start_time
        func_name: str = func.__name__
        print("time cost: ", time_pass, "s in function: ", func_name)
        return result
        pass
    return func_wrapper
    pass