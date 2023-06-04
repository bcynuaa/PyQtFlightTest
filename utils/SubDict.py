'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-04 22:10:13
 # @ license: Mozilla Public License 2.0
 # @ description: the file contains the function to insert data to a sub-dict
 '''

def insertToSubDict(origin_dict: dict, main_key, sub_key, sub_value) -> None:
    if main_key not in origin_dict:
        origin_dict[main_key] = dict()
        origin_dict[main_key][sub_key] = sub_value
        pass
    else:
        origin_dict[main_key][sub_key] = sub_value
        pass
    pass