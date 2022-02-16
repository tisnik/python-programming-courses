import xmltodict

with open("test5.xml", "r") as fin:
    s=xmltodict.parse(fin.read())

    print(s)
