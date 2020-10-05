# Knihovna Numpy
#
# Změna tvaru pole - vytvoření matice s jediným řádkem

# běžná matice se dvěma řádky a třemi sloupci
a = array([[1, 2, 3], [4, 5, 6]])

# změna tvaru matice na jediný řádek
b = reshape(a, (1, 6))

# tisk původní matice
print(a)

# tisk nové matice
print(b)
