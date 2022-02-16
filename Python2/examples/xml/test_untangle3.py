import untangle

o = untangle.parse("pom.xml")

p = o.project.groupId
print(p.cdata)
