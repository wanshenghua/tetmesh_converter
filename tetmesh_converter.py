#python 3
#File name: tetmesh_converter.py
#Description: 
#	convert the tet-mesh files provided by Dr. Yang Liu to our .tm files.

from __future__ import print_function
import sys


def help():
    print('Tet-mesh converter to convert .tet format to .tm format.')
    print('Ver 0.01 Build 20130417')
    print('Author: Shenghua Wan @ Louisiana State University')
    print("Contact: wanshenghua 'at' gmail 'dot' com")
    print()
    print('Format: tetmesh_converter.py name.tet > name.tm')

#main function    
file_name = ''
if len(sys.argv) != 2 :
    help()
    sys.exit(-1)
else :
    file_name = sys.argv[1]

#read the tet-mesh file
contents = ''
with open(file_name, 'r') as f:
    contents = f.readlines()


#parse the file
#vertex number line
vertex_num_line = contents[0].split()
num_vertex = int(vertex_num_line[0])
#cell number line
cell_num_line = contents[1].split()
num_cell = int(cell_num_line[0])
#print vertex list
for i in range(0, num_vertex):
    print ('Vertex ' + str(i) + ' ' + contents[i + 2], end='')
#print cell list
for i in range(0, num_cell):
    cell_line = contents[i + num_vertex + 2].split()
    print('Tetrahedron ' + str(i) + ' ' + ' '.join(cell_line[1:]))
#print a blank line at the end of file
print()

