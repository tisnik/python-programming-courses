import xml.sax


class XmlHandler(xml.sax.ContentHandler):

    def startElement(self, name, attributes):
        if name == "table":
            print("Node:", name)
            for (k,v) in attributes.items():
                print("\t", k, v)


parser = xml.sax.make_parser()
parser.setContentHandler(XmlHandler())

with open("db.public.xml", "r") as fin:
    parser.parse(fin)
