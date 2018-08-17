import xml.etree.ElementTree as ET
tree = ET.parse('dumps/enwiktionary-latest-pages-articles.xml')
root = tree.getroot()






def chinese_character_range():
    return range(int('3400', 16), int('4DBF', 16)) + range(int('4E00', 16), int('9fff', 16))
