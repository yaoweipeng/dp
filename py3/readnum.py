import re
import numpy

from tempfile import TemporaryFile

out = TemporaryFile()

def GetNumAndPlot(infile):
	with open(infile) as fp:
	    for result in re.findall('Part Num:           7(.*?)\n', fp.read(), re.S):
	    	print(result)

GetNumAndPlot('mer.txt')

