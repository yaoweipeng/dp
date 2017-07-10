import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

plt.style.use('seaborn-white')
# plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['font.sans-serif'] = 'Tahoma'
# # plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 16
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
en1 = 0.5*ep*ld**2

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
# fs = 24
jetcmap = plt.cm.get_cmap("rainbow", 9) #generate a jet map with 10 values 
jet_vals = jetcmap(np.arange(9)) #extract those values as an array 
jet_vals[0] = [1.0, 1, 1.0, 1] #change the first value 
newcmap = mpl.colors.LinearSegmentedColormap.from_list("newjet", jet_vals) 



# define array
EneBmE = np.ones(7)
EneBmI = np.ones(7)
EneBgE = np.ones(7)
EneBgI = np.ones(7)
sex = np.ones(7)
sey = np.ones(7)
sez = np.ones(7)
sbx = np.ones(7)
sby = np.ones(7)
sbz = np.ones(7)
TpeC1 = np.ones(7)
TpeS1 = np.ones(7)
TfeC1 = np.ones(7)
TfeS1 = np.ones(7)
TpeC2 = np.ones(7)
TpeS2 = np.ones(7)
TfeC2 = np.ones(7)
TfeS2 = np.ones(7)
TeC1 = np.ones(7)
TeS1 = np.ones(7)
TeC2 = np.ones(7)
TeS2 = np.ones(7)


time   = np.ones(7)


# plot function



file = '/Volumes/yaowp2016/'

folder = 'nj'
for i in range(7):
	ii = i*5
	time[i] = i*ts
	
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

	fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	Ex = datafile.Electric_Field_Ex.data
	Ey = datafile.Electric_Field_Ey.data
	Ez = datafile.Electric_Field_Ez.data
	Bx = datafile.Magnetic_Field_Bx.data*c
	By = datafile.Magnetic_Field_By.data*c
	Bz = datafile.Magnetic_Field_Bz.data*c
	sex[i] = np.sum(Ex**2)*en1 
	sey[i] = np.sum(Ey**2)*en1 
	sez[i] = np.sum(Ez**2)*en1 
	sbx[i] = np.sum(Bx**2)*en1 
	sby[i] = np.sum(By**2)*en1 
	sbz[i] = np.sum(Bz**2)*en1 

	TpeC1[i] = EneBmE[i]+EneBmI[i]+EneBgE[i]+EneBgI[i]
	TfeC1[i] = sex[i]+sey[i]+sez[i]+sbx[i]+sby[i]+sbz[i]
	TfeS1[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
	TpeS1[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data


folder = 'nj_non'
for i in range(7):
	ii = i*5
	time[i] = i*ts

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

	fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	Ex = datafile.Electric_Field_Ex.data
	Ey = datafile.Electric_Field_Ey.data
	Ez = datafile.Electric_Field_Ez.data
	Bx = datafile.Magnetic_Field_Bx.data*c
	By = datafile.Magnetic_Field_By.data*c
	Bz = datafile.Magnetic_Field_Bz.data*c
	sex[i] = np.sum(Ex**2)*en1 
	sey[i] = np.sum(Ey**2)*en1 
	sez[i] = np.sum(Ez**2)*en1 
	sbx[i] = np.sum(Bx**2)*en1 
	sby[i] = np.sum(By**2)*en1 
	sbz[i] = np.sum(Bz**2)*en1 

	TpeC2[i] = EneBmE[i]+EneBmI[i]+EneBgE[i]+EneBgI[i]
	TfeC2[i] = sex[i]+sey[i]+sez[i]+sbx[i]+sby[i]+sbz[i]
	TfeS2[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
	TpeS2[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data

TeC1 = TpeC1+TfeC1
TeS1 = TpeS1+TfeS1
TeC2 = TpeC2+TfeC2
TeS2 = TpeS2+TfeS2

np.save('tpec1.npy', TpeC1)
np.save('tpes1.npy', TpeS1)
np.save('tfec1.npy', TfeC1)
np.save('tfes1.npy', TfeS1)
np.save('tpec2.npy', TpeC2)
np.save('tpes2.npy', TpeS2)
np.save('tfec2.npy', TfeC2)
np.save('tfes2.npy', TfeS2)

np.save('tec1.npy', TeC1)
np.save('tes1.npy', TeS1)
np.save('tec2.npy', TeC2)
np.save('tes2.npy', TeS2)


# plt.figure(figsize=(8,5))
# ax = plt.subplot()
# ax.plot(time, TpeC1,'r-',   lw=2, label='tbc-cal')
# ax.plot(time, TpeS1,'r--',  lw=2, label='tbc-sys')
# ax.plot(time, TpeC2,'b-',   lw=2, label='pbc-cal')
# ax.plot(time, TpeS2,'b--',  lw=2, label='pbc-sys')
# plt.xlabel('time($\omega_{pe}^{-1}$)',fontsize=24)
# plt.ylabel('energy($J$)',fontsize=24)
# plt.legend(loc='best', numpoints=1, fancybox=True)
# plt.title('total system energy',fontsize=32,fontstyle='normal')

# plt.show()
# plt.savefig(file+folder+'/plots/'+'TotalEnergyComp.png',bbox_inches='tight')  # n means normalized
# plt.close()

