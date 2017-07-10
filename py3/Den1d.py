import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

n0 = 0.1
me = 9.1e-31
mi = 1*me
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp

e0 = me*c*wp/qe
b0 = e0/c

nx = 2500
ny = 3000
lx = 500
ly = 600

fs = 16

wd = 125
grid_min_x = int(0)
grid_max_x = int(nx)
grid_min_y = int(ny/2-wd)
grid_max_y = int(ny/2+wd)

Gx = np.linspace(0,lx,nx)
Gy = np.linspace(0,ly,ny)
gx = Gx[grid_min_x:grid_max_x+1]
gy = Gy[grid_min_y:grid_max_y+1]

jetcmap = plt.cm.get_cmap("rainbow", 9) #generate a jet map with 10 values 
jet_vals = jetcmap(np.arange(9)) #extract those values as an array 
jet_vals[0] = [1.0, 1, 1.0, 1] #change the first value 
newcmap = mpl.colors.LinearSegmentedColormap.from_list("newjet", jet_vals) 

for i in range(7):

	file = '/Volumes/yaowp2016/aj/'
	ii = (i)*5
	fname = file+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	nbe = datafile.Derived_Number_Density_ele_bm.data/n0
	nae = datafile.Derived_Number_Density_ele_bg.data/n0

	Bx = datafile.Magnetic_Field_Bx.data/b0
	By = datafile.Magnetic_Field_By.data/b0
	Bz = datafile.Magnetic_Field_Bz.data/b0
	Ex = datafile.Electric_Field_Ex.data/e0
	Ey = datafile.Electric_Field_Ey.data/e0
	Ez = datafile.Electric_Field_Ez.data/e0

	NBE = nbe[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1]
	NAE = nae[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1]

	ex = Ex[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1]
	ey = Ey[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1]
	ez = Ez[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1]
	bx = Bx[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1]
	by = By[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1]
	bz = Bz[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1] 


	snbe = NBE.sum(axis=1)/2/wd
	snae = NAE.sum(axis=1)/2/wd
	sex  = ex.sum(axis=1)/2/wd
	sey  = ey.sum(axis=1)/2/wd
	sez  = ez.sum(axis=1)/2/wd
	sbx  = bx.sum(axis=1)/2/wd
	sby  = by.sum(axis=1)/2/wd
	sbz  = bz.sum(axis=1)/2/wd

	se = np.sqrt(sex**2+sey**2+sez**2)
	sb = np.sqrt(sbx**2+sby**2+sbz**2)


	plt.figure(figsize=(11,5))

	plt.plot(
		gx, 
		se.transpose()*5,
		lw=2,
		color='green',
		linestyle='--',
		# marker='o',
		label='10$\epsilon_E$',
		)
	plt.plot(
		gx, 
		sb.transpose()*5,
		lw=2,
		color='cyan',
		linestyle='--',
		# marker='o',
		label='10$\epsilon_B$',
		)
	plt.plot(
		gx, 
		snbe.transpose(),
		lw=2,
		color='red',
		linestyle='-',
		# marker='s',
		label='$n_{bm}$',
		)
	plt.plot(
		gx, 
		snae.transpose(),
		lw=2,
		color='blue',
		linestyle='-',
		# marker='s',
		label='$n_{bg}$',
		)
	#fig.set_cmap('jet')
	plt.margins(0,0)
	axes = plt.gca()
	# axes.set_xlim([xmin,xmax])
	axes.set_ylim([0,3.2])
	# plt.title('Ex, normed by {:.3e} V/m'.format(e0))
	plt.title('Axial distribution, normed by {:.3e}'.format(n0))
	plt.xlabel('x/$\lambda_e$',fontsize=fs)
	plt.ylabel('$n_0$ and $\epsilon_0$',fontsize=fs)
	plt.legend(loc='best', numpoints=1, fancybox=True)
	# plt.colorbar()
	plt.savefig(file+'/axial_dist'+str(ii)+'.png',bbox_inches='tight')
	# plt.show()
	plt.close()