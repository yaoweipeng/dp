import sdf
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-paper')
plt.rcParams['font.size'] = 24

def cm2inch(value):
    return value/2.54


Num = 26
TeS1 = np.ones(Num)
TeS2 = np.ones(Num)
TeS3 = np.ones(Num)
part1 = np.ones(Num)
part2 = np.ones(Num)
pho1 = np.ones(Num)
pho2 = np.ones(Num)
time   = np.ones(Num)
file = '/Users/yaowp/code/merge/epoch2d/'

me = 9.1e-31
c = 3e8

# print(e0)

folder = 'Data0'
for i in range(Num):
	ii = i
	time[i] = ii/10
	fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)

	TeS1[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data
	fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	Gam1 = datafile.Particles_Gamma_subset_part_ele.data
	Wgt1 = datafile.Particles_Weight_subset_part_ele.data
	Gam2 = datafile.Particles_Gamma_subset_part_ion.data
	Wgt2 = datafile.Particles_Weight_subset_part_ion.data
	Gam3 = datafile.Particles_Gamma_subset_part_ele0.data
	Wgt3 = datafile.Particles_Weight_subset_part_ele0.data
	Gam4 = datafile.Particles_Gamma_subset_part_ion0.data
	Wgt4 = datafile.Particles_Weight_subset_part_ion0.data
	
	Gam5 = 0
	Wgt5 = 0
	Gam6 = 0
	Wgt6 = 0
	Px7  = 0
	Py7  = 0
	Pz7  = 0
	Wgt7 = 0

	if i>=1:
		Gam5 = datafile.Particles_Gamma_subset_part_eleq.data
		Wgt5 = datafile.Particles_Weight_subset_part_eleq.data
		Gam6 = datafile.Particles_Gamma_subset_part_ionq.data
		Wgt6 = datafile.Particles_Weight_subset_part_ionq.data
		Px7  = datafile.Particles_Px_subset_part_pho.data
		Py7  = datafile.Particles_Py_subset_part_pho.data
		Pz7  = datafile.Particles_Pz_subset_part_pho.data
		Wgt7 = datafile.Particles_Weight_subset_part_pho.data
	
	part1[i] = np.sum((Gam1-1)*me*c*c*Wgt1)*10 \
		     + np.sum((Gam2-1)*me*c*c*Wgt2)*10 \
			 + np.sum((Gam3-1)*me*c*c*Wgt3)*10 \
			 + np.sum((Gam4-1)*me*c*c*Wgt4)*10 \
			 + np.sum((Gam5-1)*me*c*c*Wgt5)*10 \
			 + np.sum((Gam6-1)*me*c*c*Wgt6)*10 
	pho1[i] = np.sum(np.sqrt(Px7**2+Py7**2+Pz7**2)*c*Wgt7)*10


# folder = 'Data1'
# for i in range(Num):
# 	time[i] = i*10
# 	fname = file+folder+'/'+str(i).zfill(4)+'.sdf'
# 	datafile = sdf.read(fname)

# 	TeS1[i] = datafile.Total_Field_Energy_in_Simulation__J_.data+datafile.Total_Particle_Energy_in_Simulation__J_.data
	
folder = 'Data'
for i in range(Num):
	ii = i
	time[i] = ii/10
	fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)

	TeS2[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data
	
	fname = file+folder+'/6'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
	Gam1 = datafile.Particles_Gamma_subset_part_ele.data
	Wgt1 = datafile.Particles_Weight_subset_part_ele.data
	Gam2 = datafile.Particles_Gamma_subset_part_ion.data
	Wgt2 = datafile.Particles_Weight_subset_part_ion.data
	Gam3 = datafile.Particles_Gamma_subset_part_ele0.data
	Wgt3 = datafile.Particles_Weight_subset_part_ele0.data
	Gam4 = datafile.Particles_Gamma_subset_part_ion0.data
	Wgt4 = datafile.Particles_Weight_subset_part_ion0.data
	Gam5 = 0
	Wgt5 = 0
	Gam6 = 0
	Wgt6 = 0
	Px7  = 0
	Py7  = 0
	Pz7  = 0
	Wgt7 = 0

	if i>=1:
		Gam5 = datafile.Particles_Gamma_subset_part_eleq.data
		Wgt5 = datafile.Particles_Weight_subset_part_eleq.data
		Gam6 = datafile.Particles_Gamma_subset_part_ionq.data
		Wgt6 = datafile.Particles_Weight_subset_part_ionq.data
		Px7  = datafile.Particles_Px_subset_part_pho.data
		Py7  = datafile.Particles_Py_subset_part_pho.data
		Pz7  = datafile.Particles_Pz_subset_part_pho.data
		Wgt7 = datafile.Particles_Weight_subset_part_pho.data

	part2[i] = np.sum((Gam1-1)*me*c*c*Wgt1)*10 \
		     + np.sum((Gam2-1)*me*c*c*Wgt2)*10 \
			 + np.sum((Gam3-1)*me*c*c*Wgt3)*10 \
			 + np.sum((Gam4-1)*me*c*c*Wgt4)*10 \
			 + np.sum((Gam5-1)*me*c*c*Wgt5)*10 \
			 + np.sum((Gam6-1)*me*c*c*Wgt6)*10 
	pho2[i] = np.sum(np.sqrt(Px7**2+Py7**2+Pz7**2)*c*Wgt7)*10


# print('TeS1 = ',TeS1)
plt.figure(figsize=(cm2inch(8.5), cm2inch(6)))
ax = plt.subplot()
ax.plot(time, TeS1,'k-',  lw=1, label='w/o merge')
ax.plot(time, part1,'b-',  lw=1, label='w/o merge')
ax.plot(time, pho1,'r-',  lw=1, label='w/o merge')
ax.plot(time, TeS2,'ko',  lw=1, markersize=3, markeredgewidth=1, markeredgecolor='k', markerfacecolor='None',label='w merge')
ax.plot(time, part2,'bo',  lw=1, markersize=3, markeredgewidth=1, markeredgecolor='b', markerfacecolor='None',label='w merge')
ax.plot(time, pho2,'ro',  lw=1, markersize=3, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None',label='w merge')

plt.xlim(0,2.5)
plt.ylim(0,2.5e3)

plt.xlabel('time($\omega_{pe}^{-1}$)')
plt.ylabel('Energy[$J$]')
plt.legend(loc='best', numpoints=1, fancybox=True)
# print(TeS1[0])
# plt.grid(b=True,which='major',axis='both')
# plt.show()
# plt.title('energy conservation',fontsize=32,fontstyle='normal')
plt.savefig('EneCons.pdf',bbox_inches='tight')  # n means normalized
plt.close()