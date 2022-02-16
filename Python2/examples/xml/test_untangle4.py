import untangle

o = untangle.parse("pom.xml")

p = o.project
print(p.get_elements())
