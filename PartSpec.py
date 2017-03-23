import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

plt.style.use('seaborn-poster')
# plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['font.sans-serif'] = 'Tahoma'
# # plt.rcParams['font.monospace'] = 'Ubuntu Mono'
# plt.rcParams['font.size'] = 10
# plt.rcParams['axes.labelsize'] = 10
# plt.rcParams['axes.labelweight'] = 'bold'
# plt.rcParams['xtick.labelsize'] = 8
# plt.rcParams['ytick.labelsize'] = 8
# plt.rcParams['legend.fontsize'] = 10
# plt.rcParams['figure.titlesize'] = 12


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

tt = 1/wp
ts = 20
te = 500

pct = 10
en0 = me*c**2

num_bins = 1000

# simulation domain
nx = 4000
ny = 4000
lx = 800
ly = 800

# figure domain (set by grid)
grid_min_x = 0
grid_max_x = nx
grid_min_y = 0
grid_max_y = ny

Gx = np.linspace(0,lx,nx)
Gy = np.linspace(0,ly,ny)
gx = Gx[grid_min_x:grid_max_x+1]
gy = Gy[grid_min_y:grid_max_y+1]


# figure parameters
fs = 16
jetcmap = plt.cm.get_cmap("rainbow", 9) #generate a jet map with 10 values 
jet_vals = jetcmap(np.arange(9)) #extract those values as an array 
jet_vals[0] = [1.0, 1, 1.0, 1] #change the first value 
newcmap = mpl.colors.LinearSegmentedColormap.from_list("newjet", jet_vals) 



# define array
# EneBmE = np.ones(7)
# EneBmI = np.ones(7)
# EneBgE = np.ones(7)
# EneBgI = np.ones(7)
# Tpe1 = np.ones(7)
# Tpe2 = np.ones(7)
# Tpe3 = np.ones(7)

# time   = np.ones(7)


# plot function


file = '/Users/yaowp/Desktop/'


for i in range(26):
	ii = i

	folder = 'aj-ext2'
	fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	GamBmE = datafile.Particles_Gamma_subset_ele1_ele_bm.data
	# GamBgE = datafile.Particles_Gamma_subset_ele1_ele_bg.data

	nbme, ebme, patches = plt.hist(GamBmE, 
		num_bins, 
		# normed=1, 
		facecolor='red', 
		alpha=0
		)
	plt.loglog(ebme[1:],
		nbme,
		'r-',
		lw=2,
		label='jet',
		)

	folder = 'aj-ext2'
	fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	GamBmE = datafile.Particles_Gamma_subset_ele1_ele_bg.data
	# GamBgE = datafile.Particles_Gamma_subset_ele1_ele_bg.data

	nbme, ebme, patches = plt.hist(GamBmE, 
		num_bins, 
		# normed=1, 
		facecolor='red', 
		alpha=0
		)
	plt.loglog(ebme[1:],
		nbme,
		'b-',
		lw=2,
		label='amb',
		)
	plt.ylim(1,1e7)
	plt.xlabel('$\gamma$')
	plt.ylabel('Part Number')
	plt.legend(loc='best', numpoints=1, fancybox=True)
	plt.title('Jet electron spectrum',fontstyle='normal')
	plt.savefig(file+folder+'/PartSpecBm'+str(ii)+'.png',bbox_inches='tight')  # n means normalized
	plt.close()

