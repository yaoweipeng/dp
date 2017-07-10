# Spatial Distribution of Fields
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
# ------------------

# Set constants
n0 = 0.1
me = 9.1e-31
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp
e0 = me*c*wp/qe
b0 = e0/c
# --------------------

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


# plot function
def plotfig(folder, varname, norm):

	# Read SDF file
	file = '/Users/yaowp/Desktop/'
	for i in range(11):
		ii = i
		fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
		datafile = sdf.read(fname)
	# -------------------

		# Get data
		Data = datafile.__dict__[varname].data/norm
		data = Data[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
		# ------------------
		
		# Draw
		plt.imshow(
			data,
			extent=[min(gx),max(gx),min(gy),max(gy)],
			aspect='1',
			cmap='bwr',
			origin='lower',
			interpolation='nearest',
			vmin = -0.5,
			vmax = 0.5,
			)
		# ------------------

		# Make it pretty
		# fig.set_cmap('bwr')
		plt.margins(0,0)
		plt.title('{}, normed by {:.1e}'.format(varname, norm))
		plt.xlabel('$x/\lambda_e$')
		plt.ylabel('$y/\lambda_e$')
		plt.colorbar()
		plt.savefig(file+folder+'/'+varname+'n_'+str(ii)+'.png',bbox_inches='tight')  # n means normalized
		plt.close()
		# -------------------
# ---------------------

# Input 
fn = 'Data2'   				 # folder name
vn = 'Electric_Field_Ex'         # variable name
nm = e0
# vn = 'Magnetic_Field_Bz'         # variable name
# nm = b0           				 normalized constant

plotfig(fn, vn, nm)
# ---------------------




