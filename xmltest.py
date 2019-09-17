import xml.etree.ElementTree as ET


with open('googleplayappstest.xml') as f:
    xml = f.read()

tree = ET.fromstring(xml)
'''
print(tree)
print(numpy.matrix(tree))
'''
for i in range(33):
    print("%30s %20s %5s %8s %8s %13s %6s %6s %12s %18s %11s %18s %15s" % (tree[i][0].text, tree[i][1].text, tree[i][2].text, tree[i][3].text, tree[i][4].text, tree[i][5].text, tree[i][6].text, tree[i][7].text, tree[i][8].text, tree[i][9].text, tree[i][10].text, tree[i][11].text, tree[i][12].text))
