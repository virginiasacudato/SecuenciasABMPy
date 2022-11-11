import math
import random

import requests


def binaryRepresentation(n, stack):
    stack.append(n)
    if n > 1:
        return binaryRepresentation(math.floor(n / 2), stack)
    binary = []
    for i in range(len(stack)):
        binary.append(stack[i] % 2)
    return binary


def scenarios(formulas):
    valuations = []
    for i in range(2 ** len(formulas)):

        def valuation(j, i=i):

            if type(j) == int:
                if not j < len(binaryRepresentation(i, [])):
                    return False
                #print(binaryRepresentation(i, [])[j])
                return binaryRepresentation(i, [])[j] == 1
            if j[0] == "~":
                return not valuation(j[2])
            if j[1] == "&":
                return valuation(j[1]) and valuation(j[3])
            if j[1] == "v":
                return valuation(j[1]) or valuation(j[3])

        valuations.append(valuation)
    return valuations

dictionary = ['A','B','D','E','F','G','H','I', 'a']
a = scenarios([0, 1, 2])
c = []
test_cases = []
for b in a:
    #print(b(0), b(1), b(2))
    c.append((b(0), b(1), b(2)))



    #r = requests.post('http://localhost:3002/absenceCalculus/run', data={"test_id": [b(0), b(1)]})

#def switch_restrictions():
#    for par_cases in test_cases:
#        if par_cases[0] == 'I':


#qswitch_restrictions()