# Knihovna Numpy
#
# explicitní specifikace typu všech prvků pole
# (interně se provádí přetypování)

import numpy

# konstrukce pole
a = numpy.array(range(10), dtype=numpy.float)

# tisk obsahu pole na standardní výstup
print(a)
