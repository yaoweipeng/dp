import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

plt.style.use('seaborn-talk')
# plt.rcParams['font.size'] = 16

# constants for normalization
n0 = 0.1
me = 9.1e-31
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp
e0 = me*c*wp/qe
b0 = e0/c

# simulation domain
nx = 2000
ny = 2000
lx = 100
ly = 100

# figure domain (set by grid)
grid_min_x = 0
grid_max_x = 200
grid_min_y = 470
grid_max_y = 530

Gx = np.linspace(0,lx,nx)
Gy = np.linspace(0,ly,ny)
gx = Gx[grid_min_x:grid_max_x+1]
gy = Gy[grid_min_y:grid_max_y+1]
# Gx = np.linspace(0,10,200)
# Gy = np.linspace(23.5,26.5,60)
# gx = Gx[0:200]
# gy = Gy[0:60]


ggx1 = int(nx/2-100)
ggx2 = int(nx/2+100)
ggy1 = int(ny/4-30)
ggy2 = int(ny/4+30)


# figure parameters
fs = 16
jetcmap = plt.cm.get_cmap("magma_r", 9) #generate a jet map with 10 values 
jet_vals = jetcmap(np.arange(9)) #extract those values as an array 
jet_vals[0] = [1.0, 1, 1.0, 1] #change the first value 
newcmap = mpl.colors.LinearSegmentedColormap.from_list("newjet", jet_vals) 


# plot function

def plotfig(folder, varname, norm):

	file = '/Users/yaowp/Desktop/'

	for i in range(12):
		ii = i+1
		fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
		datafile = sdf.read(fname)

		Data = datafile.__dict__[varname].data/norm
		data = Data[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1]
		# data = Data[ggx1:ggx2,ggy1:ggy2]
		
		# plt.figure(figsize=(11,5))
		plt.figure()
		fig = plt.imshow(
			data.transpose(),
			extent=[min(gx),max(gx),min(gy),max(gy)],
			aspect='1',
			# cmap=newcmap,
			origin="lower",
			interpolation='nearest',
			vmin = -0.1,
			vmax = 0.1,
			)
		fig.set_cmap('bwr')
		# plt.margins(0,0)
		plt.title('{}, normed by {:.3e} $T$'.format(varname, norm))
		
		plt.xlabel('x/$\lambda_e$')
		plt.ylabel('y/$\lambda_e$')
		plt.colorbar()
		plt.savefig(file+folder+'/'+varname+'n_'+str(ii)+'.png',bbox_inches='tight')  # n means normalized
		plt.close()

fn = 'sbl'   				 # folder name
# vn = 'Electric_Field_Ey'         # variable name
vn = 'Magnetic_Field_Bz'         # variable name
nm = b0           				 # normalized constant

plotfig(fn, vn, nm)