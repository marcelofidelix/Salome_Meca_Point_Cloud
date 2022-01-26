#!/usr/bin/env python3

p1 = '''
#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.4.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/marcelofidelix')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)

OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
'''

p2 = ''

p3 = '''
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
'''

p4 = ''
p5 = ''

p6 = '''
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
'''

f = open('/home/marcelofidelix/Documents/teste_salome_meca/coord.txt', 'r')
s = f.read()
f.close()

l = s.split('\n')
l = [el for el in l if el != '']

for i in range(len(l)):
	p2 += 'Vertex_'+str(i)+' = geompy.MakeVertex('+l[i].replace(' ', ',')+')'+'\n'

for i in range(len(l)):
	p4 += 'geompy.addToStudy('+ ' Vertex_' + str(i) + ", 'Vertex_" + str(i) + "' )" + '\n'

for i in range(len(l)-1):
	p5 += 'Line_' + str(i) + ' = geompy.MakeLineTwoPnt('+ ' Vertex_' + str(i) + ',' + ' Vertex_' + str(i+1) + ")" + '\n'
	
for i in range(len(l)-1):
	p5 += 'geompy.addToStudy('+ ' Line_' + str(i) + ", 'Line_" + str(i) + "' )" + '\n'

file_content = p1 + p2 + p3 + p4 + p5 + p6

open('script.py', 'w')

f = open('script.py', 'w')

f.write(file_content)

f.close()