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

tt = 1/wp
ts = 50*5
te = 1500

pct = 100
en0 = me*c**2

# simulation domain
nx = 3500
ny = 3500
lx = 3500
ly = 3500

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
EneBmE = np.ones(7)
EneBmI = np.ones(7)
EneBgE = np.ones(7)
EneBgI = np.ones(7)
Tpe1 = np.ones(7)
Tpe2 = np.ones(7)
Tpe3 = np.ones(7)

time   = np.ones(7)


# plot function



file = '/Volumes/yaowp2016/'

folder = 'nj'
for i in range(7):
	ii = i*5
	fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)

	GamBmE = datafile.Particles_Gamma_subset_ele1_ele_bm.data
	GamBmI = datafile.Particles_Gamma_subset_ion1_ion_bm.data
	GamBgE = datafile.Particles_Gamma_subset_ele1_ele_e.data
	GamBgI = datafile.Particles_Gamma_subset_ion1_ion_e.data

	WgtBmE = datafile.Particles_Weight_subset_ele1_ele_bm.data
	WgtBmI = datafile.Particles_Weight_subset_ion1_ion_bm.data
	WgtBgE = datafile.Particles_Weight_subset_ele1_ele_e.data
	WgtBgI = datafile.Particles_Weight_subset_ion1_ion_e.data


	EneBmE[i] = np.sum((GamBmE-1)*en0*np.mean(WgtBmE))*pct
	EneBmI[i] = np.sum((GamBmI-1)*en0*np.mean(WgtBmI))*pct
	EneBgE[i] = np.sum((GamBgE-1)*en0*np.mean(WgtBgE))*pct
	EneBgI[i] = np.sum((GamBgI-1)*en0*np.mean(WgtBgI))*pct

	Tpe1[i] = EneBmE[i]+EneBmI[i]+EneBgE[i]+EneBgI[i]
	
	time[i] = i*ts


folder = 'njbx0.02'
for i in range(7):
	ii = i*5
	fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)

	GamBmE = datafile.Particles_Gamma_subset_ele1_ele_bm.data
	GamBmI = datafile.Particles_Gamma_subset_ion1_ion_bm.data
	GamBgE = datafile.Particles_Gamma_subset_ele1_ele_e.data
	GamBgI = datafile.Particles_Gamma_subset_ion1_ion_e.data

	WgtBmE = datafile.Particles_Weight_subset_ele1_ele_bm.data
	WgtBmI = datafile.Particles_Weight_subset_ion1_ion_bm.data
	WgtBgE = datafile.Particles_Weight_subset_ele1_ele_e.data
	WgtBgI = datafile.Particles_Weight_subset_ion1_ion_e.data


	EneBmE[i] = np.sum((GamBmE-1)*en0*np.mean(WgtBmE))*pct
	EneBmI[i] = np.sum((GamBmI-1)*en0*np.mean(WgtBmI))*pct
	EneBgE[i] = np.sum((GamBgE-1)*en0*np.mean(WgtBgE))*pct
	EneBgI[i] = np.sum((GamBgI-1)*en0*np.mean(WgtBgI))*pct

	Tpe2[i] = EneBmE[i]+EneBmI[i]+EneBgE[i]+EneBgI[i]

folder = 'njbx5'
for i in range(7):
	ii = i*5
	fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)

	GamBmE = datafile.Particles_Gamma_subset_ele1_ele_bm.data
	GamBmI = datafile.Particles_Gamma_subset_ion1_ion_bm.data
	GamBgE = datafile.Particles_Gamma_subset_ele1_ele_e.data
	GamBgI = datafile.Particles_Gamma_subset_ion1_ion_e.data

	WgtBmE = datafile.Particles_Weight_subset_ele1_ele_bm.data
	WgtBmI = datafile.Particles_Weight_subset_ion1_ion_bm.data
	WgtBgE = datafile.Particles_Weight_subset_ele1_ele_e.data
	WgtBgI = datafile.Particles_Weight_subset_ion1_ion_e.data


	EneBmE[i] = np.sum((GamBmE-1)*en0*np.mean(WgtBmE))*pct
	EneBmI[i] = np.sum((GamBmI-1)*en0*np.mean(WgtBmI))*pct
	EneBgE[i] = np.sum((GamBgE-1)*en0*np.mean(WgtBgE))*pct
	EneBgI[i] = np.sum((GamBgI-1)*en0*np.mean(WgtBgI))*pct

	Tpe3[i] = EneBmE[i]+EneBmI[i]+EneBgE[i]+EneBgI[i]





plt.figure(figsize=(8,5))

ax = plt.subplot()
ax.plot(time, Tpe1,'o-',  lw=2, label='nj')
ax.plot(time, Tpe2,'s--', lw=2, label='njbx=0.02')
ax.plot(time, Tpe3,'s--', lw=2, label='njbx=5')
plt.xlabel('time($\omega_{pe}^{-1}$)',fontsize=fs)
plt.ylabel('energy($J$)',fontsize=fs)
plt.legend(loc='best', numpoints=1, fancybox=True)
plt.title('total particle energy',fontsize=24,fontstyle='normal')


plt.savefig(file+folder+'/plots/'+'PartEnergyComp.png',bbox_inches='tight')  # n means normalized
plt.close()

