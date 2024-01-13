#!/usr/bin/env python3 
'''Typed lists'''


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Sums a mixed list'''
    return sum(mxd_lst)