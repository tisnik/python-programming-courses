import xml.sax


class XmlHandler(xml.sax.ContentHandler):
    def startElement(self, name, attributes):
        print("Node:", name)


parser = xml.sax.make_parser()
parser.setContentHandler(XmlHandler())

with open("db.public.xml", "r") as fin:
    parser.parse(fin)
