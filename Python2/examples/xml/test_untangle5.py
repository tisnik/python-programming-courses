import untangle

o = untangle.parse("pom.xml")

d = o.project.dependencies

print(len(d))

print(dir(d))

for dep in d.dependency:
    print(dir(dep))

for dep in d.dependency:
    print(dep.artifactId.cdata)
