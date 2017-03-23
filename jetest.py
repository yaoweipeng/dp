import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

plt.style.use('seaborn-white')
plt.rcParams['font.size'] = 16

Num = 31
TeS1 = np.ones(Num)
TeS2 = np.ones(Num)
TeS3 = np.ones(Num)
time   = np.ones(Num)
file = '/Users/yaowp/Google Drive/jisuanwuli/'

folder = 'Data0'
for i in range(Num):
	time[i] = i*10
	ii = i
	fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)

	TeS1[i] = datafile.Total_Field_Energy_in_Simulation__J_.data+datafile.Total_Particle_Energy_in_Simulation__J_.data


# folder = 'Data1'
# for i in range(Num):
# 	time[i] = i*10
# 	fname = file+folder+'/'+str(i).zfill(4)+'.sdf'
# 	datafile = sdf.read(fname)

# 	TeS1[i] = datafile.Total_Field_Energy_in_Simulation__J_.data+datafile.Total_Particle_Energy_in_Simulation__J_.data
	
# folder = 'Data2'
# for i in range(Num):
# 	time[i] = i*10
# 	fname = file+folder+'/'+str(i).zfill(4)+'.sdf'
# 	datafile = sdf.read(fname)

# 	TeS2[i] = datafile.Total_Field_Energy_in_Simulation__J_.data+datafile.Total_Particle_Energy_in_Simulation__J_.data


# print('TeS1 = ',TeS1)
plt.figure(figsize=(8,5))
ax = plt.subplot()
# ax.plot(time, (TeS3-TeS3[0])/TeS3[0],'m:',  lw=2, label='1200x1200')
ax.plot(time, (TeS1)/TeS1[0],'r-',  lw=2, label='benchmark')
# ax.plot(time, (TeS2-TeS2[0])/TeS2[0],'b--',  lw=2, label='400x400')
plt.xlabel('time($\omega_{pe}^{-1}$)')
plt.ylabel('$\Delta E$')
plt.ylim(0,1.2)
plt.legend(loc='best', numpoints=1, fancybox=True, fontsize=16)
plt.grid(b=True,which='major',axis='both')
# plt.title('energy conservation',fontsize=32,fontstyle='normal')
plt.savefig('EneCons1.png',bbox_inches='tight')  # n means normalized
plt.close()