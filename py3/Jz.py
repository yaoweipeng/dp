# Spatial Distribution of current densities
# 2D contour
# yaowp, 2017-05-05
# ------------------

# Import packages
import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.style.use('seaborn-talk')
plt.rcParams['font.size'] = 24
# -----------------

# Set constants
n0 = 1e32
me = 9.1e-31
mi = 1*me
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp
j0 = qe*n0*15*c
# ------------------

# Set simulation parameters
nx = 480
ny = 480
lx = 60
ly = 60
# -------------------

# Set draw region
grid_min_x = 0
grid_max_x = nx
grid_min_y = 0
grid_max_y = ny

Gx = np.linspace(0,lx,nx)
Gy = np.linspace(0,ly,ny)
gx = Gx[grid_min_x:grid_max_x+1]
gy = Gy[grid_min_y:grid_max_y+1]
# -------------------

# Create pretty colormap
jetcmap = plt.cm.get_cmap("magma_r", 9) #generate a jet map with 10 values "rainbow"
jet_vals = jetcmap(np.arange(9)) #extract those values as an array 
jet_vals[0] = [1.0, 1, 1.0, 1] #change the first value 
newcmap = mpl.colors.LinearSegmentedColormap.from_list("mine", jet_vals) 
# --------------------

# Read SDF file
for i in range(1):
	file = '/Users/yaowp/Desktop/mr480/'
	ii = i+7
	fname = file+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
# -------------------

# Get data and normalization
	# nbe = datafile.Derived_Number_Density_ele_bm.data/n0
	# nae = datafile.Derived_Number_Density_ele_bg.data/n0
	# nbi = datafile.Derived_Number_Density_ion_bm.data/n0
	# nai = datafile.Derived_Number_Density_ion_bg.data/n0
	# jx  = datafile.Current_Jx.data/j0
	# jy  = datafile.Current_Jy.data/j0
	jz  = datafile.Current_Jz.data/j0
# ------------------

# Pick data from the region we care and transpose for drawing
	# NBE  = nbe[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# NAE  = nae[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# NBI  = nbe[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# NAI  = nae[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# Jx   = jx[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# Jy   = jy[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	Jz   = jz[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
# --------------------

	# J = np.sqrt(Jx*Jx+Jy*Jy+Jz*Jz)

# Draw
	# plt.figure(figsize=(16,10))
	fig = plt.imshow(
		Jz,
		# +NOE1+NOE2+NOE3,
		extent=[min(gx),max(gx),min(gy),max(gy)],aspect='1',
		cmap=newcmap,
		origin='lower',
		interpolation='nearest',
		# vmin = 0,
		# vmax = 10,
		)
# --------------------

# Make it pretty
	#fig.set_cmap('jet')
	plt.margins(0,0)
	# plt.title('|J|, normed by {:.3e} V/m'.format(j0))
	plt.title('Current density, normed by {:.1e}'.format(j0)
		+' at '+str(ii*20)+' $\omega_{pe}^{-1}$')
	plt.xlabel('$x/\lambda_e$')
	plt.ylabel('$y/\lambda_e$')
	plt.colorbar()
	plt.show()
	# plt.savefig(file+'CurrDen'+str(ii)+'.pdf',bbox_inches='tight')
	# plt.close()
# -----------------------