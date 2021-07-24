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
sys.path.insert(0, r'/home/marcelofidelix/Desktop/New Folder')

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

p5 = '''
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
'''

f = open('coord.txt', 'r')

s = f.read()

f.close()

l = s.split('\n')
l = [el for el in l if el != '']

for i in range(len(l)):
	p2 += 'Vertex_'+str(i)+' = geompy.MakeVertex('+l[i]+')' + '\n'

for i in range(len(l)):
	p4 += 'geompy.addToStudy('+ ' Vertex_'+str(i) + ", 'Vertex_" + str(i)+"' )"  + '\n'
	

file_content = p1+p2+p3+p4+p5

print(file_content)

f = open('output.py', 'w')

f.write(file_content)

