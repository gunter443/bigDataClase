#!/usr/bin/python3

import sys

costeMaximo = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)
    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", costeMaximo)
        oldKey = thisKey;  # creo que sobra esta liña
        costeMaximo = 0

    oldKey = thisKey
    costeMaximo = costeMaximo if costeMaximo > thisSale else thisSale

# Escribe o último par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey, "\t", costeMaximo)