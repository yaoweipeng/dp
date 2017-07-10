import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.style.use('seaborn-paper')

def cm2inch(value):
    return value/2.54


n0 = 1.18e31
me = 9.1e-31
mi = 1*me
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp

nx = 5000
ny = 3000
lx = 5000
ly = 3000

# fs = 16

grid_min_x = 500
grid_max_x = 2999
grid_min_y = 500
grid_max_y = 2499

Gx = np.linspace(0,lx,nx)
Gy = np.linspace(0,ly,ny)
gx = Gx[grid_min_x:grid_max_x+1]
gy = Gy[grid_min_y:grid_max_y+1]

file = '/Volumes/yaowp2016/flow-n1-q/'
ii = 15
fname = file+str(ii).zfill(4)+'.sdf'
datafile = sdf.read(fname)
nbe = datafile.Derived_Number_Density_ele_bm.data/n0
nae = datafile.Derived_Number_Density_ele_e.data/n0
nqe = datafile.Derived_Number_Density_ele_qed.data/n0
nph = datafile.Derived_Number_Density_pho.data/n0

NBE  = nbe[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
NAE  = nae[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
NQE  = nqe[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
NPH  = nph[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()

file = '/Volumes/yaowp2016/flow-n/'
ii = 15
fname = file+str(ii).zfill(4)+'.sdf'
datafile = sdf.read(fname)
nbe1  = datafile.Derived_Number_Density_ele_bm.data/n0
nae1  = datafile.Derived_Number_Density_ele_e.data/n0
NBE1  = nbe1[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()
NAE1  = nae1[grid_min_x:grid_max_x+1,grid_min_y:grid_max_y+1].transpose()


fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
fig.subplots_adjust(right=0.8)

ax  = axs[0, 0]
ax1 = ax.imshow(np.log10(NBE1+NAE1+1),
	# extent=[500,2500,500,2500],
	extent=[min(gx),max(gx),min(gy),max(gy)],
	aspect='0.6',
	cmap='magma',
	origin="lower",
	interpolation='nearest',
	vmin = 0,
	vmax = 1,
	)
ax.set_adjustable('box-forced')
# plt.xlabel('x/$\lambda_e$')
# ax.ylabel('y/$\lambda_e$')

ax  = axs[1, 0]
ax2 = ax.imshow(np.log10(NBE+NAE+1),
	# extent=[500,2500,500,2500],
	extent=[min(gx),max(gx),min(gy),max(gy)],
	aspect='',
	cmap='magma',
	origin="lower",
	interpolation='nearest',
	vmin = 0,
	vmax = 1,
	)

ax  = axs[1, 1]
ax3 = ax.imshow(np.log10(NBE+NAE+NQE+1),
	# extent=[500,2500,500,2500],
	extent=[min(gx),max(gx),min(gy),max(gy)],
	aspect='0.6',
	cmap='magma',
	origin="lower",
	interpolation='nearest',
	vmin = 0,
	vmax = 1,
	)


ax  = axs[0, 1]
ax4 = ax.imshow(np.log10(NPH/10+1),
	# extent=[500,2500,500,2500],
	extent=[min(gx),max(gx),min(gy),max(gy)],
	aspect='0.6',
	cmap='magma',
	origin="lower",
	interpolation='nearest',
	vmin = 0,
	vmax = 1,
	)

cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(ax1, cax=cbar_ax)
# plt.colormaps()
# ax1.set_cmap('magma')
plt.xlabel('y/$\lambda_e$')
plt.ylabel('$\lg(n_e/n_0)$')
plt.savefig('/Users/yaowp/Desktop/jet-density-11'+str(ii)+'.pdf',
	bbox_inches='tight',
	format='pdf',
	dpi=250)


# fig = plt.imshow(
# 	# gx,gy,
# 	NAI+NBI-NAE-NBE,
# 	# +NOE1+NOE2+NOE3,
# 	extent=[min(gx),max(gx),min(gy),max(gy)],aspect='1',
# 	cmap='bwr',
# 	origin="lower",
# 	interpolation='nearest',
# 	vmin = -2e-16,
# 	vmax = 2e-16,
# 	)
# #fig.set_cmap('jet')
# plt.margins(0,0)
# # plt.title('Ex, normed by {:.3e} V/m'.format(e0))
# plt.title('Charge density, normed by {:.3e}'.format(n0))
# plt.xlabel('x/$\lambda_e$',fontsize=fs)
# plt.ylabel('y/$\lambda_e$',fontsize=fs)
# plt.colorbar()
# plt.savefig(file+'/cd_'+str(ii)+'.png',bbox_inches='tight')
# plt.close()