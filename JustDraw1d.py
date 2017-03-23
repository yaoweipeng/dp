import matplotlib.pyplot as plt
import numpy as np


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

time = [0, 250, 500, 750, 1000, 1250, 1500]

TeC1 = np.load('tec1.npy')
TeS1 = np.load('tes1.npy')
TeC2 = np.load('tec2.npy')
TeS2 = np.load('tes2.npy')
# TfeC1 = np.load('tfec1.npy')
# TfeS1 = np.load('tfes1.npy')
# TfeC2 = np.load('tfec2.npy')
# TfeS2 = np.load('tfes2.npy')
# TpeC1 = np.load('tpec1.npy')
# TpeS1 = np.load('tpes1.npy')
# TpeC2 = np.load('tpec2.npy')
# TpeS2 = np.load('tpes2.npy')

dec1 = (TeC1-TeC1[0])/TeC1[0]
des1 = (TeS1-TeS1[0])/TeS1[0]
dec2 = (TeC2-TeC2[0])/TeC2[0]
des2 = (TeS2-TeS2[0])/TeS2[0]

plt.figure(figsize=(8,5))
ax = plt.subplot()
ax.plot(time, dec1,'r-',   lw=2, label='rel-cal')
ax.plot(time, des1,'r--',  lw=2, label='rel-sys')
ax.plot(time, dec2,'b-',   lw=2, label='nrel-cal')
ax.plot(time, des2,'b--',  lw=2, label='nrel-sys')
plt.xlabel('time($\omega_{pe}^{-1}$)',fontsize=24)
plt.ylabel('$\Delta E$',fontsize=24)
plt.legend(loc='best', numpoints=1, fancybox=True)
plt.title('energy conservation',fontsize=32,fontstyle='normal')

# plt.show()
plt.savefig('EneCons.png',bbox_inches='tight')  # n means normalized
plt.close()