#!/usr/bin/env python

from collections import defaultdict
from heapq import heapify, heappop, heappush
import random
import string

def encode(symbol_frequency):
    heap = [[weight, [symbol, ""]] for symbol, weight in symbol_frequency.items()]
    heapify(heap)

    while len(heap) > 1:
        low = heappop(heap)
        high = heappop(heap)

        for bits in low[1:]:
            bits[1] = '0' + bits[1]
        for bits in high[1:]:
            bits[1] = '1' + bits[1]
        heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    return sorted(heappop(heap)[1:], key=lambda f: (len(f[-1]), f))

txt = "".join( [random.choice(string.letters) for i in xrange(15)] )
symbol_frequency = defaultdict(int)

for char in txt:
    symbol_frequency[char] += 1

huffman = encode(symbol_frequency)
print "Intial String:", txt
print "="*35 + "\n"
print "Symbol\tWeight\tHuffman Code"
print "-"*35
for i in huffman:
    print "%s\t%s\t%s" % (i[0], symbol_frequency[i[0]], i[1])
