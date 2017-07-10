# Phase space of jet and ambient species
# 2D scatter
# yaowp, 2017-03-29
# ------------------

# Import packages
import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.style.use('seaborn-talk')
# -----------------

# Set constants
n0 = 0.1
me = 9.1e-31
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp
# -----------------

# Read SDF file
file = '/Users/yaowp/Desktop/'

for i in range(11):
	ii = i*1

	folder   = 'Data'
	fname    = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
# -------------------

# Get data
	PosBmE = datafile.Grid_Particles_subset_ele1_ele_bm.data
	PxBmE  = datafile.Particles_Px_subset_ele1_ele_bm.data/me/c
# -------------------

# Draw species 1
	xx = PosBmE[0]/ld
	# yy = PosBmE[1]/ld
	pp = PxBmE
	plt.scatter(xx,
		pp,
		c          = 'red',
		# lw=2,
		label      = 'jet electron',
		alpha      = 0.3,
		edgecolors = 'none',
		)
# ---------------------

# Get data
	PosBmE = datafile.Grid_Particles_subset_ele1_ele_bg.data
	PxBmE  = datafile.Particles_Px_subset_ele1_ele_bg.data/me/c
# ---------------------

# Draw species 2
	xx = PosBmE[0]/ld
	# yy = PosBmE[1]/ld
	pp = PxBmE
	plt.scatter(xx,
		pp,
		c          = 'blue',
		# lw=2,
		label      = 'ambient electron',
		alpha      = 0.3,
		edgecolors = 'none',
		)
# ---------------------

# Make it pretty
	plt.xlim(0,80)
	plt.ylim(-5,25)
	plt.xlabel('$x/\lambda_e$')
	plt.ylabel('$P_x/(m_ec)$')
	plt.legend(loc='best', numpoints=1, fancybox=True)
	plt.title('jet electron x-px at '+str(ii*5)+' $\omega_{pe}^{-1}$')
	# plt.show()
	plt.savefig(file+folder+'/plots/PartSpec'+str(ii)+'.png',
		bbox_inches='tight')
	plt.close()
# ---------------------

