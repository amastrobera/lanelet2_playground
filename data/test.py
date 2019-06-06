#! python

from xml.etree import ElementTree as et
from sys import argv, exit


if __name__ == "__main__":

    if len(argv) < 2:
        print("--- xml test line strings ---")
        print("$ python test,py <osm_file>")
        exit(1)

    tree = et.parse(argv[1])
    root = tree.getroot()

    nodes = {n.attrib["id"]: (n.attrib["lat"], n.attrib["lon"]) for n in root.findall("node") }
    print("found %d nodes" % len(nodes))

    ways = root.findall("way")
    print("found %d ways" % len(ways))
    for w in ways:
        print("points of the way \"%s\" " % w.attrib["id"])
        for p in w.findall("nd"):
            lat, lon = nodes[p.attrib["ref"]]
            print("    * %s (%s, %s)," % (p.attrib["ref"], lat, lon))



