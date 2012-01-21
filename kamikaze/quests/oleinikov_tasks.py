#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21.01.2012

@author: kamikaze
'''

from operator import itemgetter
from itertools import groupby

def __get_ranges(seq):
    sequence_generator = (
                          list(map(itemgetter(1), g)) for k, g in
                          groupby(enumerate(sorted(seq)), lambda t: t[0]-t[1])
                          )

    for range_ in sequence_generator:
        if range_[0] == range_[-1]:
            yield str(range_[0])
        else:
            yield '%s-%s' % (range_[0], range_[-1])

def numbersarr2range(numbers):
    return '; '.join(__get_ranges(numbers))