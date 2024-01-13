#!/usr/bin/env python3
'''Typed function'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Construct a multiplying function'''
    def rec_funct(n: float) -> float:
        '''Constructed function'''
        return n * multiplier
    return rec_funct
