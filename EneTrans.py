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
TeF1 = np.ones(Num)
TeF2 = np.ones(Num)
TeF3 = np.ones(Num)
TeP1 = np.ones(Num)
TeP2 = np.ones(Num)
TeP3 = np.ones(Num)
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
	TeF1[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
	TeP1[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data
# ----------------------

# Read SDF file
folder = 'Data1'
for i in range(Num):
	
	fname = file+folder+'/'+str(i).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
# -----------------------

# Get data
	time[i] = i*5
	TeF2[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
	TeP2[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data
# -----------------------

# Read SDF file
folder = 'Data2'
for i in range(Num):
	fname = file+folder+'/'+str(i).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
# ------------------------
	
# Get data
	time[i] = i*5
	TeF3[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
	TeP3[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data
# -------------------------


# Draw figure
plt.figure(figsize=(8,5))
ax = plt.subplot()
ax.semilogy(time, TeP1,'r-',  lw=2, label='$T_e=5keV$, Part' )
ax.semilogy(time, TeP3,'b-',  lw=3, label='$T_e=50eV$, Part' )
ax.semilogy(time, TeP2,'m-',  lw=2, label='$T_e=0$,    Part' )
ax.semilogy(time, TeF1,'r--', lw=2, label='$T_e=5keV$, Field')
ax.semilogy(time, TeF3,'b--', lw=3, label='$T_e=50eV$, Field')
ax.semilogy(time, TeF2,'m--', lw=2, label='$T_e=0$,    Field')
# -------------------------

# Make it pretty
plt.xlabel('time($\omega_{pe}^{-1}$)')
plt.ylabel('Energy in $J$')
# plt.ylim(0,1.2)
plt.legend(loc='best', numpoints=1, fancybox=True, fontsize=16)
# plt.grid(b=True,which='major',axis='both')
plt.title('energy transfer')
plt.savefig(file+'EneTrans.pdf',bbox_inches='tight')
plt.close()
# --------------------------


