import xmltodict
import pprint

with open("test5.xml", "r") as fin:
    s = xmltodict.parse(fin.read())

    p = s["root"]
    m = p["middle"]

    pprint.pprint(m)
