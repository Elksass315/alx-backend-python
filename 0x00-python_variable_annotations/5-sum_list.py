#!/usr/bin/env python3


"""_
    Complex types - list of floats
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
        type-annotated function sum_list which takes a list input_list of
        floats as argument and returns their sum as a float.
        """
    return sum(input_list)
