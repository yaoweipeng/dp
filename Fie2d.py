import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

n0 = 0.1
me = 9.1e-31
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp

e0 = me*c*wp/qe
b0 = e0/c



nx = 4000
ny = 4000
lx = 800
ly = 800

fs = 16

grid_min_x = 0
grid_max_x = nx
grid_min_y = 0
grid_max_y = ny

Gx = np.linspace(0,lx,nx)
Gy = np.linspace(0,ly,ny)
gx = Gx[grid_min_x:grid_max_x+1]
gy = Gy[grid_min_y:grid_max_y+1]

jetcmap = plt.cm.get_cmap("rainbow", 9) #generate a jet map with 10 values 
jet_vals = jetcmap(np.arange(9)) #extract those values as an array 
jet_vals[0] = [1.0, 1, 1.0, 1] #change the first value 
newcmap = mpl.colors.LinearSegmentedColormap.from_list("newjet", jet_vals) 

for i in range(7):

	file = '/Volumes/yaowp2016/njbx0.02/'
	ii = (i)*5
	fname = file+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	# Ex = datafile.Electric_Field_Ex.data/e0
	# Ey = datafile.Electric_Field_Ey.data/e0
	# Ez = datafile.Electric_Field_Ez.data/e0
	# Bx = datafile.Magnetic_Field_Bx.data/b0
	# By = datafile.Magnetic_Field_By.data/b0
	Bz = datafile.Magnetic_Field_Bz.data/b0
	
	# ex = Ex[grid_min_x:grid_max_x,grid_min_y:grid_max_y]
	# ey = Ey[grid_min_x:grid_max_x,grid_min_y:grid_max_y]
	# ez = Ez[grid_min_x:grid_max_x,grid_min_y:grid_max_y]
	# bx = Bx[grid_min_x:grid_max_x,grid_min_y:grid_max_y]
	# by = By[grid_min_x:grid_max_x,grid_min_y:grid_max_y]
	bz = Bz[grid_min_x:grid_max_x,grid_min_y:grid_max_y] 
	
	plt.figure(figsize=(11,5))

	fig = plt.imshow(bz.transpose(),
		extent=[min(gx),max(gx),min(gy),max(gy)],aspect='1',
		# cmap=newcmap,
		origin="lower",
		interpolation='nearest',
		vmin = -2,
		vmax = 2,
		)
	fig.set_cmap('bwr')
	plt.margins(0,0)
	plt.title('Bz, normed by {:.3e} T'.format(b0))
	# plt.title('Ez, normed by {:.3e} V/m'.format(e0))
	plt.xlabel('x/$\lambda_e$',fontsize=fs)
	plt.ylabel('y/$\lambda_e$',fontsize=fs)
	plt.colorbar()
	plt.savefig(file+'/plots/bzn_'+str(ii)+'.png',bbox_inches='tight')  # n means normalized
	plt.close()
