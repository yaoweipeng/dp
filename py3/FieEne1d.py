import sdf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

plt.style.use('seaborn-white')

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
ts = 10
te = 300

en0 = 0.5*ep*ld**2

# simulation domain
nx = 2500
ny = 3000
lx = 500
ly = 600

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
time = np.ones(7)
tfe_sys = np.ones(7)
tpe_sys = np.ones(7)
te_sys = np.ones(7)
# plot function


file = '/Volumes/yaowp2016/'
folder = 'aj'

for i in range(7):
	ii = i*5
	fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
	datafile = sdf.read(fname)

	tfe_sys[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
	tpe_sys[i] = datafile.Total_Particle_Energy_in_Simulation__J_.data
	te_sys[i] = tfe_sys[i]+tpe_sys[i]
	time[i] = i*ts*5


plt.figure(figsize=(8,5))

ax = plt.subplot()
ax.plot(time, tpe_sys,'r--', lw=2, label='Part')
ax.plot(time, tfe_sys,'b--', lw=2, label='Field')
ax.plot(time, te_sys,'m-', lw=2, label='All')
# ax.plot(time, tfe3,'s-.', lw=2, label='bx=5')
plt.xlabel('time($\omega_{pe}^{-1}$)',fontsize=fs)
plt.ylabel('energy($J$)',fontsize=fs)
plt.legend(loc='best', numpoints=1, fancybox=True)
plt.title('Energy Evolution',fontsize=24,fontstyle='normal')

plt.savefig(file+folder+'/'+'EneEvo.png',bbox_inches='tight')
plt.close()