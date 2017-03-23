import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

n0 = 1
me = 9.1e-31
mi = 100*me
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp

nx = 2000
ny = 2000
lx = 100
ly = 100

fs = 16

grid_min_x = 0
grid_max_x = nx
grid_min_y = 0
grid_max_y = ny

Gx = np.linspace(0,lx,nx)
Gy = np.linspace(0,ly,ny)
gx = Gx[grid_min_x:grid_max_x+1]
gy = Gy[grid_min_y:grid_max_y+1]

jetcmap = plt.cm.get_cmap("magma_r", 9) #generate a jet map with 10 values "rainbow"
jet_vals = jetcmap(np.arange(9)) #extract those values as an array 
jet_vals[0] = [1.0, 1, 1.0, 1] #change the first value 
newcmap = mpl.colors.LinearSegmentedColormap.from_list("mine", jet_vals) 

for i in range(12):

	file = '/Users/yaowp/Desktop/sbl/'
	ii = i+1
	fname = file+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	nbe = datafile.Derived_Number_Density_averaged_ele1.data/n0
	nae = datafile.Derived_Number_Density_averaged_ele2.data/n0
	nbi = datafile.Derived_Number_Density_averaged_ion1.data/n0
	nai = datafile.Derived_Number_Density_averaged_ion2.data/n0
	# noe1 = datafile.Derived_Number_Density_ele_o1.data/n0
	# noe2 = datafile.Derived_Number_Density_ele_o2.data/n0
	# noe3 = datafile.Derived_Number_Density_ele_o3.data/n0

	NBE  = nbe[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	NAE  = nae[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	NBI  = nbe[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	NAI  = nae[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# NOE1 = noe1[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# NOE2 = noe2[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
	# NOE3 = noe3[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()

	plt.figure(figsize=(11,5))

	fig = plt.imshow(
		# gx,gy,
		NAI+NBI-NAE-NBE,
		# +NOE1+NOE2+NOE3,
		extent=[min(gx),max(gx),min(gy),max(gy)],aspect='1',
		cmap='bwr',
		origin="lower",
		interpolation='nearest',
		vmin = -2e-16,
		vmax = 2e-16,
		)
	#fig.set_cmap('jet')
	plt.margins(0,0)
	# plt.title('Ex, normed by {:.3e} V/m'.format(e0))
	plt.title('Charge density, normed by {:.3e}'.format(n0))
	plt.xlabel('x/$\lambda_e$',fontsize=fs)
	plt.ylabel('y/$\lambda_e$',fontsize=fs)
	plt.colorbar()
	plt.savefig(file+'/cd_'+str(ii)+'.png',bbox_inches='tight')
	plt.close()