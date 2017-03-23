import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

plt.style.use('seaborn-white')
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
n0 = 1.8e20
me = 9.1e-31
qe = 1.6e-19
ep = 8.9e-12
c  = 3e8
wp = np.sqrt(n0*qe*qe/me/ep)
ld = c/wp
e0 = me*c*wp/qe
b0 = e0/c

pct = 100
en0 = me*c**2

num_bins = 100

# simulation domain
nx = 350
ny = 350
lx = 350
ly = 350

# figure domain (set by grid)
grid_min_x = 0
grid_max_x = nx
grid_min_y = 0
grid_max_y = ny

Gx = np.linspace(0,lx,nx)
Gy = np.linspace(0,ly,ny)
gx = Gx[grid_min_x:grid_max_x]
gy = Gy[grid_min_y:grid_max_y]


# figure parameters
fs = 16
jetcmap = plt.cm.get_cmap("rainbow", 9) #generate a jet map with 10 values 
jet_vals = jetcmap(np.arange(9)) #extract those values as an array 
jet_vals[0] = [1.0, 1, 1.0, 1] #change the first value 
newcmap = mpl.colors.LinearSegmentedColormap.from_list("newjet", jet_vals) 


file = '/Volumes/yaowp2016/'


for i in range(21):
	ii = i

	folder = 'Data1'
	fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	GamBmE = datafile.Particles_Gamma_subset_ele1_ele_bm.data
	# GamBgE = datafile.Particles_Gamma_subset_ele1_ele_e.data

	nbme, ebme, patches = plt.hist(GamBmE, 
		num_bins, 
		# normed=1, 
		facecolor='red', 
		alpha=0
		)
	plt.semilogy(ebme[1:],
		nbme,
		'r-',
		lw=2,
		label='With Surrd',
		)

	folder = 'Data2'
	fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	GamBmE = datafile.Particles_Gamma_subset_ele1_ele_bm.data
	# GamBgE = datafile.Particles_Gamma_subset_ele1_ele_e.data

	nbme, ebme, patches = plt.hist(GamBmE, 
		num_bins, 
		# normed=1, 
		facecolor='blue', 
		alpha=0
		)
	plt.semilogy(ebme[1:],
		nbme,
		'b--',
		lw=2,
		label='Without Surrd',
		)
	
	plt.xlim(0,100)
	plt.ylim(1,1e5)


	# folder = 'Data3'
	# fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	# datafile = sdf.read(fname)
	# GamBmE = datafile.Particles_Gamma_subset_ele1_ele_bm.data
	# # GamBgE = datafile.Particles_Gamma_subset_ele1_ele_e.data

	# nbme, ebme, patches = plt.hist(GamBmE, 
	# 	num_bins, 
	# 	# normed=1, 
	# 	facecolor='green', 
	# 	alpha=0
	# 	)
	# plt.plot(ebme[1:],
	# 	nbme,
	# 	'm-',
	# 	lw=2,
	# 	label='$ppc=500$',
	# 	)

	# plt.xlim(1,1e2)
	# plt.ylim(1,1e5)

	plt.xlabel('$\gamma$',fontsize=fs)
	plt.ylabel('Part Number',fontsize=fs)
	plt.legend(loc='best', numpoints=1, fancybox=True)
	plt.title('Jet electron spectrum',fontsize=24,fontstyle='normal')
	plt.savefig(file+folder+'/PartSpecBm'+str(ii)+'.png',bbox_inches='tight')  # n means normalized
	plt.close()

