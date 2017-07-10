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
mpl.rcParams['font.size'] = 24
# -------------------

# Allocate array
Num = 2
TeF1 = np.ones(Num)
TeF2 = np.ones(Num)
TeF3 = np.ones(Num)
TeP1 = np.ones(Num)
TeP2 = np.ones(Num)
TeP3 = np.ones(Num)
# TeAl = np.ones(Num)
time   = np.ones(Num)
# --------------------

# Read SDF file
file = '/Users/yaowp/Desktop/'
folder = 'test'
for i in range(Num):
	ii = i+12
	
	fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)
# ---------------------

# Get data
	time[i] = i*25
	TeF1[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
	TeP1[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data
	TeAl    = TeF1[0]+TeP1[0]
# ----------------------

# # Read SDF file
# folder = 'Data1'
# for i in range(Num):
	
# 	fname = file+folder+'/'+str(i).zfill(4)+'.sdf'
# 	datafile = sdf.read(fname)
# # -----------------------

# # Get data
# 	time[i] = i*5
# 	TeF2[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
# 	TeP2[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data
# # -----------------------

# # Read SDF file
# folder = 'Data2'
# for i in range(Num):
# 	fname = file+folder+'/'+str(i).zfill(4)+'.sdf'
# 	datafile = sdf.read(fname)
# # ------------------------
	
# # Get data
# 	time[i] = i*5
# 	TeF3[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
# 	TeP3[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data
# # -------------------------


# Draw figure
plt.figure(figsize=(8,5))
ax = plt.subplot()
ax.semilogy(time, TeP1/TeAl,'r-',  lw=2, label='Part' )
# ax.semilogy(time, TeP3,'b-',  lw=3, label='$T_e=50eV$, Part' )
# ax.semilogy(time, TeP2,'m-',  lw=2, label='$T_e=0$,    Part' )
ax.semilogy(time, TeF1/TeAl,'b--', lw=2, label='Field')
# ax.semilogy(time, TeF3,'b--', lw=3, label='$T_e=50eV$, Field')
# ax.semilogy(time, TeF2,'m--', lw=2, label='$T_e=0$,    Field')
# -------------------------

# Make it pretty
plt.xlabel('time($\omega_{pe}^{-1}$)')
plt.ylabel('Energy in $J$')
plt.ylim(1e-2,1.2)
plt.legend(loc='best', numpoints=1, fancybox=True)
plt.grid(b=True,which='major',axis='y')
plt.title('Energy Transfer')
# plt.show()
plt.savefig(file+'EneTrans.pdf',bbox_inches='tight')
plt.close()
# --------------------------


