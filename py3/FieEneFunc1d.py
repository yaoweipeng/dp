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

en0 = 0.5*ep*ld**2

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
gx = Gx[grid_min_x:grid_max_x]
gy = Gy[grid_min_y:grid_max_y]


# figure parameters
fs = 16
jetcmap = plt.cm.get_cmap("rainbow", 9) #generate a jet map with 10 values 
jet_vals = jetcmap(np.arange(9)) #extract those values as an array 
jet_vals[0] = [1.0, 1, 1.0, 1] #change the first value 
newcmap = mpl.colors.LinearSegmentedColormap.from_list("newjet", jet_vals) 



# define array
sex = np.ones(7)
sey = np.ones(7)
sez = np.ones(7)
sbx = np.ones(7)
sby = np.ones(7)
sbz = np.ones(7)
tfe_cal = np.ones(7)
tfe_sys = np.ones(7)
time = np.ones(7)


# plot function

def plotfig(folder):

	file = '/Volumes/yaowp2016/'

	for i in range(7):
		ii = i*5
		fname = file+folder+'/'+str(ii).zfill(4)+'.sdf'
		datafile = sdf.read(fname)

		# Data = datafile.__dict__[varname].data/norm
		Ex = datafile.Electric_Field_Ex.data
		Ey = datafile.Electric_Field_Ey.data
		Ez = datafile.Electric_Field_Ez.data
		Bx = datafile.Magnetic_Field_Bx.data*c
		By = datafile.Magnetic_Field_By.data*c
		Bz = datafile.Magnetic_Field_Bz.data*c
		
		# data = Data[grid_min_x:grid_max_x,grid_min_y:grid_max_y]
		sex[i] = np.sum(Ex**2)*en0 
		sey[i] = np.sum(Ey**2)*en0 
		sez[i] = np.sum(Ez**2)*en0 
		sbx[i] = np.sum(Bx**2)*en0 
		sby[i] = np.sum(By**2)*en0 
		sbz[i] = np.sum(Bz**2)*en0 


		tfe_cal[i] = sex[i]+sey[i]+sez[i]+sbx[i]+sby[i]+sbz[i]
		tfe_sys[i] = datafile.Total_Field_Energy_in_Simulation__J_.data
		time[i] = i*ts


	plt.figure(figsize=(8,5))

	ax = plt.subplot()
	ax.plot(time, tfe_cal,'o-',  lw=2, label='tfe_cal')
	ax.plot(time, tfe_sys,'s--', lw=2, label='tfe_sys')
	plt.xlabel('time($\omega_{pe}^{-1}$)',fontsize=fs)
	plt.ylabel('energy($J$)',fontsize=fs)
	plt.legend(loc='best', numpoints=1, fancybox=True)
	plt.title('total field energy',fontsize=24,fontstyle='normal')

	
	plt.savefig(file+folder+'/plots/'+'FieldEnergy.png',bbox_inches='tight')  # n means normalized
	plt.close()

fn = 'njbx0.02'   				 # folder name
# vn = 'Electric_Field_Ez'         # variable name
# nm = e0           				 # normalized constant

plotfig(fn)