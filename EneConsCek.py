# Energy conservation check
# 1D Plot
# yaowp, 2017-03-29
# ------------------

# Import packages
import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.style.use('seaborn-talk')
plt.rcParams['font.size'] = 16
# -------------------

# Allocate array
Num = 11
TeS1 = np.ones(Num)
TeS2 = np.ones(Num)
TeS3 = np.ones(Num)
time   = np.ones(Num)
# --------------------

# Read SDF file
file = '/Users/yaowp/Desktop/'
folder = 'Data'
for i in range(Num):
	ii = i
	
	fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
# ---------------------

# Get data
	time[i] = i*5
	TeS1[i] = datafile.Total_Field_Energy_in_Simulation__J_.data+datafile.Total_Particle_Energy_in_Simulation__J_.data
# ----------------------

# Read SDF file
folder = 'Data1'
for i in range(Num):
	
	fname = file+folder+'/'+str(i).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
# -----------------------

# Get data
	time[i] = i*5
	TeS2[i] = datafile.Total_Field_Energy_in_Simulation__J_.data+datafile.Total_Particle_Energy_in_Simulation__J_.data
# -----------------------

# Read SDF file
folder = 'Data2'
for i in range(Num):
	fname = file+folder+'/'+str(i).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
# ------------------------
	
# Get data
	time[i] = i*5
	TeS3[i] = datafile.Total_Field_Energy_in_Simulation__J_.data+datafile.Total_Particle_Energy_in_Simulation__J_.data
# -------------------------


# Draw figure
plt.figure(figsize=(8,5))
ax = plt.subplot()
ax.plot(time, (TeS1)/TeS1[0],'r-',  lw=2, label='$T_e=5keV$')
ax.plot(time, (TeS3)/TeS3[0],'b--', lw=2, label='$T_e=50eV$')
ax.plot(time, (TeS2)/TeS2[0],'m:',  lw=2, label='$T_e=0$')
# -------------------------

# Make it pretty
plt.xlabel('time($\omega_{pe}^{-1}$)')
plt.ylabel('$\Delta E$')
plt.ylim(0,1.2)
plt.legend(loc='best', numpoints=1, fancybox=True, fontsize=16)
# plt.grid(b=True,which='major',axis='both')
plt.title('energy conservation')
plt.savefig(file+'EneCons.pdf',bbox_inches='tight')
plt.close()
# --------------------------


