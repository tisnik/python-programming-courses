import xml.sax


class XmlHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.in_table = False

    def startElement(self, name, attributes):
        if name == "table":
            print("Found table:", attributes["name"])
            self.in_table = True

        if self.in_table and name == "column":
            print("\tColumn:", attributes["name"])
            for (k,v) in attributes.items():
                print("\t\t", k, v)

    def endElement(self, name):
        if name == "table":
            self.in_table = False


parser = xml.sax.make_parser()
parser.setContentHandler(XmlHandler())

with open("db.public.xml", "r") as fin:
    parser.parse(fin)
