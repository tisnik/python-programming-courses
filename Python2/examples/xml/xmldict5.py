import xmltodict

with open("db.public.xml", "r") as fin:
    s = xmltodict.parse(fin.read())

    tables = s["database"]["tables"]

    print(tables)
    for k,v in itemize(tables):
        print(k,v)


   # print(s["root"]["middle"]["#text"])
