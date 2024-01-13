#!/usr/bin/env python3
'''To kv lists'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Tuple conversion from str'''
    return (k, float(v ** 2))
