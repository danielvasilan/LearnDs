import sys
import graphviz as gv
import xml.etree.ElementTree as ET

def getEntityAttr(entityType):
	switcher = {
		"fact": {"color": "red", "shape": "box"},
		"dim": {"color": "blue", "shape": "ellipse"},
		"hub": {"color": "blue", "shape": "box"},
		"sat": {"color": "green", "shape": "ellipse"},
		"lnk": {"color": "red", "shape": "hexagon"},
		"biz": {"color": "green", "shape": "ellipse"}
        
	}
	return switcher.get(entityType, "black")

def printGraph():
	grf = gv.Digraph(comment='The Round Table')
	grf.engine = 'dot' # neato circo dot
	grf.attr(rankdir='TB', splines='line', rank='same')

	grf  #doctest: +ELLIPSIS

	# read the xml cfg
	tree = ET.parse('cfg.xml')
	root = tree.getroot()

	layerNo = 0
	for layer in root.findall('Layer'):
		layerNo += 1
		clusterName = 'cluster'+layer.attrib['name']
		
		with grf.subgraph(name = clusterName, node_attr={'shape': 'ellipse'}) as cluster:
			cluster.attr(label = layer.attrib['name'] + ' Layer')
		
			prevNodeName = ''
			entityNo = 0
			for entity in layer.iter('Entity'):
		
				print (layer.attrib['name']+' ' + entity.attrib['name'])

				entityNo += 1
				nodePos = str(layerNo) + ',' + str(entityNo)+'!'
				entityAttr = getEntityAttr(entity.attrib['schema'])
				if entity.attrib['type'] == 'view': 
					cluster.node(entity.attrib['name'], style='dashed', color=entityAttr['color'], shape=entityAttr['shape'], group=layer.attrib['name'], tooltip=entity.find('Command').text.replace('\n', '&#10;'))
				else:
					cluster.node(entity.attrib['name'], color=entityAttr['color'], shape=entityAttr['shape'], group=layer.attrib['name'])

				# if any dependencies defined, add them
				if 'dependencies' in entity.attrib:
					for dep in entity.attrib['dependencies'].split(';'):
						cluster.edge(dep, entity.attrib['name'], style='dashed')
				
				if prevNodeName != '':
					cluster.edge(prevNodeName, entity.attrib['name'], color='invis')
				prevNodeName = entity.attrib['name']
				
			for txn in layer.iter('Transformation'):
				cluster.node(txn.attrib['name'], color='gray', shape='box', style='filled')
				if 'sourceEntities' in txn.attrib:
					for srcEnt in txn.attrib['sourceEntities'].split(';'):
						cluster.edge(srcEnt, txn.attrib['name'])
				if 'targetEntities' in txn.attrib:
					for trgEnt in txn.attrib['targetEntities'].split(';'):
						cluster.edge(txn.attrib['name'], trgEnt)
		
	print(grf.source)  # doctest: +NORMALIZE_WHITESPACE

	#grf.view()

	grf.render('test-output/round-table.gv', view=False)  


def printLayerER (layerName):
	# read the xml cfg
	tree = ET.parse('cfg.xml')
	root = tree.getroot()
	
	g = gv.Digraph('g', node_attr={'shape': 'none', 'height': '.1'})
	
	for entity in root.findall("Layer[@name='" + layerName + "']/Entities/Entity"):
		tableLabel = '<<table border="0" cellspacing="0">'
		tableLabel += '<tr><td border="1" bgcolor="blue">' + entity.attrib['name'] + '</td></tr>'
		for attr in entity.iter('Attribute'):
			tableLabel += '<tr><td port="' + attr.attrib["name"] + '" border="1">' + attr.attrib["name"] + '</td></tr>'
	
		tableLabel += '</table>>'
		
		g.node(entity.attrib['name'], tableLabel)
	
	for entity in root.findall("Layer[@name='" + layerName + "']/Entities/Entity"):
		for rel in entity.findall("Relation"):
			g.edge(entity.attrib["name"]+":"+rel.attrib["attribute"] , rel.attrib["fkEntity"]+":"+rel.attrib["fkAttribute"])
		
	
	
	g.render('test-output/Layer-ER-diag.gv', view=True)  

############# test 

# printGraph()

printLayerER ('DIM')

