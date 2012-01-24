#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, re
from math import *

def do_process(ifname):
	n_str = ''
	cnt = 0

	if not os.path.isfile(ifname):
		return

	f = open(ifname, 'r')

	n_str = f.readline()

	if n_str:
		n_str = n_str.strip()

		cnt = int(n_str)
		if cnt < 0:
			cnt = 0

		curr_row = 1
		prime = {'H': 1, 'A': 1, 'C': 2, 'K': 1, 'E': 1, 'R': 1, 'U': 1, 'P': 1}

		for i in xrange(cnt):
			chars = {'H': 0, 'A': 0, 'C': 0, 'K': 0, 'E': 0, 'R': 0, 'U': 0, 'P': 0}
			n_str = f.readline().strip()

			if not n_str:
				break

			for ch in (c for c in n_str if prime.get(c, False)):
				chars[ch] += 1

			word_cnt = min([chars[ch] // prime[ch] for ch in chars])

			print('Case #%d: %d' % (curr_row, word_cnt))
			curr_row += 1

	f.close()


if __name__ == '__main__':
	argv_len = len(sys.argv)

	if argv_len > 1:
		do_process(sys.argv[1])

