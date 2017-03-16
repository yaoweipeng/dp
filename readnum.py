import re
import matplotlib.pyplot as pyplot
import numpy

def GetNumAndPlot(infile):
	with open(infile) as fp:
		# b = numpy.zeros(26)
		for result in re.findall('Part Num:          11(.*?)\n', fp.read(), re.S):
			print(result)
	# pyplot.plot(b)
	# pyplot.show()



GetNumAndPlot('a.txt')


