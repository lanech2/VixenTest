#!python.exe
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
import uuid

top = Element('TimedSequenceData')
top.set('version', '2')
top.set("xmlns:a", "http://www.w3.org/2001/XMLSchema")
top.set("xmlns:i", "http://www.w3.org/2001/XMLSchema-instance")
top.set('xmlns', "http://schemas.datacontract.org/2004/07/VixenModules.Sequence.Timed")
modIID = SubElement(top, 'ModuleInstanceId')
modIID.set('xmlns:d1p1', "http://schemas.microsoft.com/2003/10/Serialization/Arrays")
modIID.set('xmlns', "")
modIID.text = str(uuid.uuid4())
modTID = SubElement(top, 'ModuleTypeId')
modTID.text = str(uuid.uuid4())
length = SubElement(top, 'Length')
length.set('xmlns', "")
length.text = 'PT1M'
ver = SubElement(top, 'Version')
ver.set('xmlns', "")
ver.text = '0'
data = SubElement(top, '_dataModels')
eff = SubElement(top, '_effectNodeSurrogates')
eff.set('xmlns', "")
fil = SubElement(top, '_filterNodeSurrogates')
fil.set('xmlns', "")
med = SubElement(top, '_mediaSurrogates')
med.set('xmlns', "")
sel = SubElement(top, '_selectedTimingProviderSurrogate')
sel.set('xmlns', "")
selProv = SubElement(sel, 'ProviderType')
selSrc = SubElement(sel, 'SourceName')
marks = SubElement(top, 'MarkCollections')
tpp = SubElement(top, 'TimePerPixel')

tree = ET.parse("./Sequence/1-Glorias.xml")
root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)

for node in root.iter('EffectNodeSurrogate'):
    eff.append(node)
    # ID = node.find('InstanceId').text
    # ST = node.find('StartTime').text
    # print(ID, ST)

ElementTree(top).write('out.xml', encoding='utf-8', xml_declaration=True)
