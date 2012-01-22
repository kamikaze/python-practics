#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21.01.2012

@author: kamikaze
'''

from operator import itemgetter
from itertools import groupby

def numbersarr2range(numbers):
    ranges = [list(map(itemgetter(1), g)) for k, g in groupby(enumerate(sorted(numbers)), lambda t: t[0]-t[1])]
    ranges = [str(range_[0]) if range_[0] == range_[-1] else '%s-%s' % (range_[0], range_[-1]) for range_ in ranges]
    return '; '.join(ranges)


def ranges2numbersarr(range_str):
    ranges = [range_.split('-', 1) for range_ in range_str.split(';')]
    ranges = [range(int(limit[0]), int(limit[-1])+1) for limit in ranges]
    return [number for numbers in ranges for number in numbers]
