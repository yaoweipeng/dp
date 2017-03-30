# Spatial Distribution of densities
# 2D contour
# yaowp, 2017-03-30
# ------------------

# Import packages
import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.style.use('seaborn-talk')
plt.rcParams['font.size'] = 16
# -----------------

# Set constants
n0 = 0.1
me = 9.1e-31
mi = 1*me
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp
# ------------------

# Set simulation parameters
nx = 800
ny = 800
lx = 80
ly = 80
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
for i in range(11):
	file = '/Users/yaowp/Desktop/Data2/'
	ii = i
	fname = file+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
# -------------------

# Get data and normalization
	nbe = datafile.Derived_Number_Density_ele_bm.data/n0
	nae = datafile.Derived_Number_Density_ele_bg.data/n0
	# nbi = datafile.Derived_Number_Density_ion_bm.data/n0
	# nai = datafile.Derived_Number_Density_ion_bg.data/n0
# ------------------

# Pick data from the region we care and transpose for drawing
	NBE  = nbe[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	NAE  = nae[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# NBI  = nbe[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# NAI  = nae[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
# --------------------

# Draw
	# plt.figure(figsize=(16,10))
	fig = plt.imshow(
		NAE+NBE,
		# +NOE1+NOE2+NOE3,
		extent=[min(gx),max(gx),min(gy),max(gy)],aspect='1',
		cmap=newcmap,
		origin='lower',
		interpolation='nearest',
		vmin = 0,
		vmax = 3,
		)
# --------------------

# Make it pretty
	#fig.set_cmap('jet')
	plt.margins(0,0)
	# plt.title('Ex, normed by {:.3e} V/m'.format(e0))
	plt.title('Electron density, normed by {:.1e}'.format(n0)
		+' at '+str(ii*5)+' $\omega_{pe}^{-1}$')
	plt.xlabel('$x/\lambda_e$')
	plt.ylabel('$y/\lambda_e$')
	plt.colorbar()
	plt.savefig(file+'ElecDen'+str(ii)+'.png',bbox_inches='tight')
	plt.close()
# -----------------------