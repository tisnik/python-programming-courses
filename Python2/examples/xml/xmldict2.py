import xmltodict
import pprint

with open("pom.xml", "r") as fin:
    s=xmltodict.parse(fin.read())

    pprint.pprint(s)
