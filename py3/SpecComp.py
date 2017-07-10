import sdf
# import numpy
import matplotlib.pyplot as pyplot

pyplot.style.use('seaborn-poster')
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

# fs = 16
fname = '/Volumes/yaowp2016/aj/60030.sdf'
datafile = sdf.read(fname)

gambm = datafile.Particles_Gamma_subset_ele1_ele_bm.data
gambg = datafile.Particles_Gamma_subset_ele1_ele_bg.data

# gamo1 = datafile.Particles_Gamma_subset_ele1_ele_o1.data
# gamo2 = datafile.Particles_Gamma_subset_ele1_ele_o2.data
# gamo3 = datafile.Particles_Gamma_subset_ele1_ele_o3.data
# gamo = gamo1+gamo2+gamo3

num_bins = 100
nbme, ebme, patches = pyplot.hist(gambm, 
	num_bins, 
	# normed=1, 
	facecolor='red', 
	alpha=0
	)
pyplot.loglog(ebme[1:],
	nbme,
	'r-',
	# lw=2,
	label='Jet',
	)
nbge, ebge, patches = pyplot.hist(gambg, 
	num_bins, 
	# normed=1, 
	facecolor='red', 
	alpha=0
	)
pyplot.loglog(ebge[1:],
	nbge,
	'b-',
	# lw=2,
	label='Amb',
	)
# noe, eoe, patches = pyplot.hist(gamo, 
# 	num_bins, 
# 	# normed=1, 
# 	facecolor='red', 
# 	alpha=0
# 	)
# pyplot.loglog(eoe[1:],
# 	noe,
# 	'g-',
# 	lw=2,
# 	label='Surd',
# 	)
pyplot.xlabel('$\gamma$')
pyplot.ylabel('Part Number')
pyplot.legend(loc='best', numpoints=1, fancybox=True)
pyplot.title('Spectrum Components',fontstyle='normal')
pyplot.savefig('/Users/yaowp/Desktop/SpecComp.png',bbox_inches='tight')  # n means normalized
pyplot.close()