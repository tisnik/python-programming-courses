# Knihovna Numpy
#
# Přetypování
#
# konstrukce pole přetypováním seznamu

# import hlavního balíčku knihovny Numpy
import numpy

# vytvoření běžného seznamu
l = [1, 2, 3, 4]

# přetypování (konstrukce pole daného typu)
a = numpy.float16(l)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)