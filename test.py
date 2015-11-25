#!python.exe
import sys
import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import Element, SubElement, ElementTree
# import uuid
import newSequence as seq
from xml.dom import minidom

tree = ET.parse("./Sequence/1-Glorias.xml")
root = tree.getroot()

# iterate through the EffectNodeSurrogate element in the source file (Design).
# for each StartTime I need to create a new file and append these nodes into
#   the '_effectNodeSurrogate' element of the target file
# Then I need to find each associated data model and append it to the
#   '_dataModels' element of the target file
currStartTime = 0
for node in root.iter('EffectNodeSurrogate'):
    startTime = node.find('StartTime').text
    if startTime != currStartTime:
        currStartTime = startTime
        blank = seq.createBlankSequence()
    blank.find('_effectNodeSurrogates').append(node)
    # ID = node.find('InstanceId').text
    # ST = node.find('StartTime').text
    # print(ID, ST)

xmlstr = minidom.parseString(ET.tostring(blank)).toprettyxml(indent="   ")
with open("out.xml", "w") as f:
    f.write(xmlstr)
# ElementTree(blank).write('out.xml', encoding='utf-8', xml_declaration=True)
