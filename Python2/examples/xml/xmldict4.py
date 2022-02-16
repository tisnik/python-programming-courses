import xmltodict

with open("test5.xml", "r") as fin:
    s = xmltodict.parse(fin.read())

    p = s["root"]["middle"]["@popis"]

    print(p)
