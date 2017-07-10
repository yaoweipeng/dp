import sdf
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-paper')

num_bins = 50
me = 9.1e-31
c = 3e8

file = '/Users/yaowp/code/merge/epoch2d/'

ii = 15

folder = 'Data0'
fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
datafile = sdf.read(fname)
px = datafile.Particles_Px_subset_part_pho.data/me/c

nbme, ebme, patches = plt.hist(px, 
	num_bins, 
	# normed=1, 
	facecolor='red', 
	alpha=0
	)
plt.semilogy(ebme[1:],
	nbme,
	'r-',
	lw=1,
	label='No merge',
	)

folder = 'Data'
fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
datafile = sdf.read(fname)
px = datafile.Particles_Px_subset_part_pho.data/me/c

nbme, ebme, patches = plt.hist(px, 
	num_bins, 
	# normed=1, 
	facecolor='red', 
	alpha=0
	)
plt.semilogy(ebme[1:],
	nbme,
	'ro',
	lw=1,
	markersize=3, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None',
	label='Merge',
	)
# plt.ylim(1,1e7)
plt.xlabel('$P_x$[$m_ec$]')
plt.ylabel('Number of Photons')
plt.legend(loc='best', numpoints=1, fancybox=True)
# plt.savefig(file+folder+'/PartSpecBm'+str(ii)+'.png',bbox_inches='tight')  # n means normalized
# plt.close()
plt.show()
