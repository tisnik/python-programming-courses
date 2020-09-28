# Knihovna Numpy
#
# Přetypování
#
# konstrukce pole přetypováním seznamu

# import hlavního balíčku knihovny Numpy
import numpy

# vytvoření běžného seznamu
l = [1, "foo", 3, False, None]

# přetypování (konstrukce pole daného typu)
a = numpy.int64(l)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)
