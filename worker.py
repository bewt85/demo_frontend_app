#!/usr/bin/env python

import time

i=99
count_lookup = {
    0: "no"
}.get
bottle_lookup = {
    1: "bottle"
}.get

def verse(i):
    count = count_lookup(i, str(i))
    next_count = count_lookup(i-1, str(i-1))
    bottle = bottle_lookup(i, "bottles")
    next_bottle = bottle_lookup(i-1, "bottles")
    return "{0} {1} of beer on the wall; {0} {1} of beer; take one down, pass it around; {2} {3} of beer on the wall".format(count, bottle, next_count, next_bottle)
   
while 1:
    print(verse(i))
    i = 99 if i == 1 else i-1
    time.sleep(2)
